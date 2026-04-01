from Bio import Entrez, SeqIO
from io import StringIO
import pandas as pd
import time

'''
Purpose: This script calculates the ambiguity percentage (percent of non A, T, C, or G
values in a DNA sequence) and sorts by the records by those with the highest (in other
words the most error prone records are shown first.)
'''


def initiate_search(search_term, email):
    # Email is a requirement by NCBI, the API provider.

    Entrez.email = email

    query = (f'"{search_term}"[Organism]' +
             ' AND ((mitochondrion[filter] OR chloroplast[filter] OR plastid[filter]) AND "complete genome"[Title])'
             )

    # Entrez.esearch fetches IDs necessary to get record title and DNA sequence.

    handle = Entrez.esearch(db="nuccore", term=query, retmax=10000)
    record = Entrez.read(handle)
    handle.close()

    total_records = int(record['Count'])

    if total_records == 0:
        return pd.DataFrame(), 0

    # Get summaries for ONLY 500 records maximum.

    id_list = record["IdList"][:500]

    # Get records and place in a dataframe.

    handle = Entrez.esummary(db="nuccore", id=",".join(id_list), retmax=500)
    summaries = Entrez.read(handle)
    handle.close()

    records = []
    for index, summary in enumerate(summaries):
        records.append({
            "Entry": index,
            "Accession": summary['AccessionVersion'],
            "Title": summary['Title'],
            "BP Length": int(summary['Length']),
            "Updated": summary['UpdateDate'],
        })

    df = pd.DataFrame(records)

    # Use IDs to fetch DNA sequences in batches of 100 and only do around 3 requests per second.
    # This is to keep within the API limits.

    seq_dict = {}
    for i in range(0, len(id_list), 100):
        batch = id_list[i:i + 100]
        handle = Entrez.efetch(db="nuccore", id=",".join(batch), rettype="fasta", retmode="text")
        fasta_data = handle.read()
        handle.close()

        for record in SeqIO.parse(StringIO(fasta_data), "fasta"):
            seq_dict[record.id.split(".")[0]] = str(record.seq)

        print(f"Fetched {min(i + 100, len(id_list))}/{len(id_list)} sequences...")
        time.sleep(0.34)

    # Adds full DNA sequence to the table.

    df["FullSequence"] = df["Accession"].str.split(".").str[0].map(seq_dict)

    # Find the percentage of ambiguity.

    def ambiguity_percentage(seq):
        # This helps prevent crashes if a sequence is missing.
        if not seq:
            return None
        ambiguous = sum(1 for base in seq if base not in "ATGCatgc")
        return round((ambiguous / len(seq)) * 100, 2)

    df["Ambiguity Percentage"] = df["FullSequence"].map(ambiguity_percentage)

    df = df.sort_values("Ambiguity Percentage", ascending=False)

    # Drops column containing full sequence as it is no longer needed.

    df = df.drop('FullSequence', axis=1)

    return df, total_records