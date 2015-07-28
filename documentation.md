#Docs

Welcome to the documentation for investa_gator.  The intention of this tool is to automate the analysis and data collection processes related to human trafficking.  Much of the knowledge that went into this tool came out of my time as a researcher fighting slavery.

##Installation

###C++

Unfortunately, at present there are quiet a few dependecies to using the tool.

1) A c++ compiler - if you are on ubuntu or mac this is pretty easy to get:

__on__ __ubuntu__:

`sudo apt-get install build-essential`
`sudo apt-get install g++`

__on__ __mac__:

Download and install xcode [instructions here](https://developer.apple.com/xcode/downloads/)

__on__ __windows__:

Unfortunately there is no "standard" way to install a c++ compiler on windows.  There are a number of options.  I recommend install cygwin and making use of there installer to get g++.  But you could also get visual studios and then make use of the c++ compiler that comes with it.  

###Python packages

You can either install these packages seperately or just make use of the requirements file that comes with this repo, up to you.  In the interest of completeness I include the dependencies here.

* lxml.html
* requests
* unidecode
* textblob
* nltk
* Flask-SQLAlchemy
* SQLAlchemy
* sklearn
* numpy
* pandas
* Flask
* scipy
* networkx

Please note the requirements file has some other packages that I just think everyone should have, but aren't essential for this project :)  Feel free to use the minimial-requirements.txt file if you just want those.

To install the dependencies you can do:

`sudo pip install -r requirements.txt`  _or_ `sudo pip install -r minimum-requirements.txt`

You could also go through and type out `sudo pip install [package name]`.  Totally your choice :)

###Extra set up stuff

Once you have everything dowloaded, you'll still need to do a few things:

1) create the database
2) download the nltk corpus
3) twilio credentials - you'll need to sign up for twilio and create your own creds there
twilio.creds is of the form (username,password).  Both username and password are strings.  They were saved with pickle.  




