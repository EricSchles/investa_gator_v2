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

ToDos:

Facial Recognition:

To see what the Facial Recognition front end looks like head to the root of the project and type:

`python run.py`

This will start up the server.  Head over to [http://localhost:5000/index2](http://localhost:5000/index2).  As you can see this page asks you two match two pictures - the picture on the left should be of a missing person, the picture on the right should come from a website showing pictures of women and men who are sex workers.  The intention is to be able to draw a connection between people who were missing and people who ended up as prostitutes.  There is a high likelihood that if you were declared missing, you probably being sex trafficked.  

Right now I have a [CBIR](https://github.com/EricSchles/cbir) and a [cbir that compares faces](https://github.com/EricSchles/cbir_opencv).  The face compare CBIR works with the above route, we still need to figure out what to do with the background CBIR.  My guess is this tool will be used only by law enforcement and so we create a mechanism for uploading a folder of pictures and comparing it against another set of pictures with the same background.  And then classify specific pictures as having the same background.  

So this is our first to do - create a front end for uploading two sets of folders and then returning the photos with the same background as the target set.  

The second piece of this is building a database of missing persons pictures.  The other piece, building up a database of pictures from prostitution websites is easy (and basically already done).  All that needs to be done is creating a mechanism for efficiently storing and accessing these pictures, ideally from a database rather than a file system, for processing.  Another piece of this is downloading these pitures from the internet.

Social network analysis:

There is a ton to do here in the following areas -

implementing graph algorithms to do automated social network analysis
create visualizations of said social networks
decide on what constitutes a connection in a social network for the purposes of human trafficking.

Visualization of data:

Using the existing tool, we essentially have the first step of any statistical analysis - the data.  Now we need a set of visualizations to understand and interpret the data.  This is an open question and should be up to the specific individuals developing the tools.  However further and directed analysis is probably wise here as well.

Pattern finding:

This set of todos involves understanding the larger patterns in the data set.  This means doing time series analysis, policy analysis, economic analysis, and a few other key things.  The idea here is to understand what are the determining factors that lead to rise and fall in the supply of commericial sex and what proportion of this commericial sex is human trafficking.  The idea is that magnitudinally human trafficking will be much lower than commericial sex, however proportionally, we can say that there is a correlation between commercial sex and human trafficking, this is verified by internal data, which unfortunately must be taken at face value.  






