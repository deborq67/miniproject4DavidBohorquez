### INF601 - Advanced Programming in Python
### David Bohorquez
### Mini Project 4
 
 
# Organelle Search: Django Port
 
A Django version of the search engine that shows the most incomplete
DNA records of organelle genomes from Genbank.<br>

![OrganelleSearchHome.png](https://i.ibb.co/whbXry0L/Organelle-Search-Home.png)

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
The search bar will not accept any input until you log in. Before doing any searches, click here on the `Register` button: <br>

![OrganelleSearchHome.png](https://i.ibb.co/5gH0SmXP/Organelle-Search-Home.png) <br>

You will be asked to put an email and a password. **Please put a valid email in here.** <br>

After you make an account, you will automatically be logged in and can initiate searches.

Once you're logged in, you also have the ability to change your password in this new port. This option is located
on the left side of the black bar.

### Searches

You can search any eukaryotic organism you want on this search engine. Be it a
mushroom, a cat, or a potato you can see what results pop up. For maximum results,
I highly suggest you use the scientific name of the organism you want to look up. <br>

If you get no results, you can always click on the header logo to start a new search. <br>

![OrganelleResults.png](https://i.ibb.co/zWc09ZJm/Organelle-Search-Result.png) <br>



Need some ideas of what to search for? Try these organisms:
 * *Felis catus* - Domestic cat
 * *Canis lupus* - Wolf
 * *Solanum tuberosum* - Potato
 * *Amanita phalloides* - Death Cap Mushroom

### History

You may have noticed that at the end of the top black bar, there is an option that
says `History`. As the name suggests, this button lets you view your entire
search history including results with no records. It will also show the time stamp
of when said search was executed. <br>

![OrganelleHistory.png](https://i.ibb.co/zVmGVrs6/Organelle-Base-History.png) <br>

If you have a Django admin account, you can also visit the Django admin page to view, delete,
and edit the search histories of users, including yours. Specifically, you can edit the amount
of records found and the search term itself if you so choose.

### Downloads

New to the Django port, as you may have noticed from the above screenshots, is the ability to download both your 
history and search results in a CSV format. Every time you try to download, you will always get a confirmation
dialogue prompting you to confirm your choice. After confirming, you will be redirected to a download page.

## Getting Started

### Installing

This program was made using Python 3.13.11.
 
### Dependencies
 
The requirements.txt file has all the dependencies needed.
The next section will tell you how to install it.
 
### Executing the Program
 
Due to the more complex nature of this project, a few extra steps will
be needed to appropriately prepare the files. <br>

First, download the `organellebasedjango.zip` and extract the `organellebasedjango`
directory from it. *Go to the `organellebase` folder inside it.*

* From the directory, get all your dependencies by executing this line on Python:
```
pip install -r requirements.txt
```
* Afterwards, you must make the tables Organelle Search uses to display results, keep track of users,
and display history.
* Execute these commands:
```
python manage.py makemigrations
python manage.py migrate
```

Optionally, if you want access to the admin interface and also bypass the
regular register system, you can also make an admin user by executing:

```
python manage.py createsuperuser
```
You will still be asked for an email using this method however.
<br>
<br>
<br>
Finally, execute this line:
```
python manage.py runserver
```
If all goes well, you should see an output of:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 03, 2026 - 04:22:17
Django version 6.0.3, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
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

* **Why are the CSV fields named differently from the table shown?**

The CSV files and tables are both generated from the models themselves. The difference is that the tables 
are set with a custom field to make it easier for a user to understand. The CSV leaves the unchanged model field
names in place.

## Authors
 
* David Bohorquez
 
## Version History

* v1.0: Released as organellebasedjango.zip.
 
## License
 
This project is licensed under the GNU General Public License - see the LICENSE.md file for details
 
## Acknowledgments
 
* [Fayette Reynolds for the background image.](https://www.pexels.com/photo/cell-seen-under-microscope-11198505/)
* [Bootstrap Template for Search Bar](https://bootstrapexamples.com/@anonymous/search-bar-with-search-icon-in-bootstrap-5-2)
* [Bootstrap Template for Error Page](https://bootstrapexamples.com/@valeria/404-page-template-2)
* [This Ernst Haeckel drawing for the logo: it's public domain.](https://pdimagearchive.org/images/b46b8d91-a0b4-4134-8268-1660285ab735/)
* [Modified Heroic Template used for base.html](https://github.com/startbootstrap/startbootstrap-heroic-features)
* [Register and Login System](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
* [Bootstrap Navbar Documentation](https://getbootstrap.com/docs/4.0/components/navbar/#text)
* [Bootstrap Modal Documentation](https://getbootstrap.com/docs/5.3/components/modal/)
