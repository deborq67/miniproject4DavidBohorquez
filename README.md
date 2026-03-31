### INF601 - Advanced Programming in Python
### David Bohorquez
### Mini Project 4
 
 
# Organelle Ambiguity Search
 
A search engine that shows the most incomplete
DNA records of organelle genomes from Genbank.<br>

![OrganelleSearchHome.png](https://i.ibb.co/chVzX9zS/Organelle-Search-Home.png)

## Description

All DNA sequences contain four distinct bases: adenine (A), thymine (T), 
cytosine (C), and guanine (G). A DNA sequence uploaded to a genetic
databank like NCBI GenBank most likely looks like the following:

```
GCTTATTCTCTATGCGGGG
```
Sometimes, however, due to either the quality of the DNA sample, the sequencing
technology, or human error, ambiguities arise and are usually represented by
letters that are not A, T, C, or G. Take, for example, the first 2 `N`s in 
this sequence:

```
NNACTAATGACTAATCAGC
```
Calculating ambiguity can be done by taking these other letters and dividing them by
the total length of the DNA sequence. Since the complete genetic structure of a specimen
is typically a very long structure, this project instead uses the complete mitochondrial
and/or chloroplast records(if they exist) of any organism you want since their sequence
lengths are only a very small fraction of a complete organism's genome.

## How to Use

To make a search, you *need to make an account with an email and password.*
If you try and make a search without being logged in, you will automatically
be redirected to the login page. Before doing any searches, click here on the `Register` button: <br>

![OrganelleSearchHome.png](https://i.ibb.co/hJfzx0qB/Organelle-Register.png) <br>

You will be asked to put an email and a password. **Please put a valid email in here.** <br>

After you make an account you can log in either manually or be redirected to log in via a search attempt.

### Searches

You can search any eukaryotic organism you want on this search engine. Be it a
mushroom, a cat, or a potato you can see what results pop up. For maximum results,
I highly suggest you use the scientific name of the organism you want to look up. <br>

If you get no results, don't worry: you'll just get a page that tells you to start a new search. <br>

![OrganelleResults.png](https://i.ibb.co/4nGDNNWv/Organelle-Results.png) <br>

When you're done looking at the results, click the `New Search` button again
to go back to the home page. <br>

Need some ideas of what to search for? Try these organisms:
 * *Felis catus* - Domestic cat
 * *Canis lupus* - Wolf
 * *Solanum tuberosum* - Potato
 * *Amanita phalloides* - Death Cap Mushroom

### History

You may have noticed that to the right of `New Search` there is an option
says `History`. As the name suggests, this button lets you view your entire
search history including invalid results. It will also show the time stamp
of when said search was executed. <br>

![OrganelleHistory.png](https://i.ibb.co/TqH77P7T/Organelle-History.png) <br>

## Getting Started

### Installing

This program was made using Python 3.13.11.
 
### Dependencies
 
The requirements.txt file has all the dependencies needed.
The next section will tell you how to install it.
 
### Executing the Program
 
Due to the more complex nature of this project, a few extra steps will
be needed to appropriately prepare the files. <br>

First, download the `organellebaseflask.zip` and extract the `organellebaseflask`
directory from it. *This will be the working directory you will execute Python from.*

* From the directory, get all your dependencies by executing this line on Python:
```
pip install -r requirements.txt
```
* Afterwards, you must make the tables Organelle Search uses to display results and keep track of users. Execute this:
```
flask --app organellebaseflask init-db
```
* Finally, execute this line:
```
flask --app organellebaseflask 
```
If all goes well, you should see an output of:
```
* Serving Flask app 'organellebaseflask'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
```
Visit the address and the page should look like the first screenshot. You have
successfully deployed Organelle Search on your own device!

## Help

* **Why do I have to make an account to search?**

Because the API (Entrez in this case) requires an email in order to conduct a search. The email
you use to make your account is the one that is used for said search to be executed.

* **Why is the program so slow?**

Once again, it's because of API limits. Without an API key, the maximum amount of requests you
can make is 3 per second. Same reason the maximum amount of results shown is 500.
This has already been accounted for in the script and a limit was placed so even if
you misspell your email, you shouldn't be blocked. However, please try to put a valid email.

## Authors
 
* David Bohorquez
 
## Version History

* Released as organellebaseflask.zip.
 
## License
 
This project is licensed under the GNU General Public License - see the LICENSE.md file for details
 
## Acknowledgments
 
* [Fayette Reynolds for the background image.](https://www.pexels.com/photo/cell-seen-under-microscope-11198505/)
* [Bootstrap Template for Search Bar](https://bootstrapexamples.com/@anonymous/search-bar)
* [Bootstrap Template for Error Page](https://bootstrapexamples.com/@valeria/404-page-template-2)
* [Modified Heroic Template used for base.html](https://github.com/startbootstrap/startbootstrap-heroic-features)
* [Register and Login System](https://learndjango.com/tutorials/django-login-and-logout-tutorial
)