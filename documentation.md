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

OR

You can make use of my totally awesome custom installer (which leverages pip)

`python install_requirements.py --ls =`

You could also go through and type out `sudo pip install [package name]`.  Totally your choice :)

###Extra set up stuff

Once you have everything dowloaded, you'll still need to do a few things:

1) create the database
2) download the nltk corpus
3) twilio credentials - you'll need to sign up for twilio and create your own creds there
twilio.creds is of the form (username,password).  Both username and password are strings.  They were saved with pickle.  

##ToDos:

Facial Recognition:

###High Level

To see what the Facial Recognition front end looks like head to the root of the project and type:

`python run.py`

This will start up the server.  Head over to [http://localhost:5000/index2](http://localhost:5000/index2).  As you can see this page asks you two match two pictures - the picture on the left should be of a missing person, the picture on the right should come from a website showing pictures of women and men who are sex workers.  The intention is to be able to draw a connection between people who were missing and people who ended up as prostitutes.  There is a high likelihood that if you were declared missing, you probably being sex trafficked.  

Right now I have a [CBIR](https://github.com/EricSchles/cbir) and a [cbir that compares faces](https://github.com/EricSchles/cbir_opencv).  The face compare CBIR works with the above route, we still need to figure out what to do with the background CBIR.  My guess is this tool will be used only by law enforcement and so we create a mechanism for uploading a folder of pictures and comparing it against another set of pictures with the same background.  And then classify specific pictures as having the same background.  

So this is our first to do - create a front end for uploading two sets of folders and then returning the photos with the same background as the target set.  

The second piece of this is building a database of missing persons pictures.  The other piece, building up a database of pictures from prostitution websites is easy (and basically already done).  All that needs to be done is creating a mechanism for efficiently storing and accessing these pictures, ideally from a database rather than a file system, for processing.  Another piece of this is downloading these pitures from the internet.

###Specific tasks

* Implementing Deep Learning Facial Recognition Algorithms
* Finish the Facial Recognition Front End
* Build a database of missing persons pictures
* Improve accuracy of current opencv facial comparison algorithm by building a stronger dataset of faces
* Improve the cbir's indexing by using binary search or something faster than linear search

Social network analysis:

This section of the project hasn't even been prototyped yet.  The ideal system will take in disperate data from social websites of a few categories:

* facebook-like websites
* okcupid-like websites
* tinder-like phone apps
* linkedin-like websites
* Messageboard websites
* craigslist/backpage websites
* twitter-like websites
* blogs

From this data we need to decide on appropriate criterion for a connection between two entities, below are some suggestions on criterion:

Definition: entity - a post, like on backpage or craigslist or some other similar site; a profile or user account, like on okcupid, tinder, facebook, linkedin or a message board.

* two entities sharing a phone number 
* two entities sharing the same email address
* two entities sharing the same domain (assuming it's not gmail, yahoo or another extremely common one)
* two entities sharing the same handle across multiple domains - this will only be true for messageboards/dating websites/twitter
* two entities sharing the same address across multiple domains
* two entities sharing a close enough writing style

Once we have a good notion of connection we should be able to do social network analysis:
Because I am not an expert in SNA I don't know what the best algorithms to implement are.  My recommendation is to look at [networkx's algorithms section for ideas](https://networkx.github.io/documentation/latest/reference/index.html) also, note that networkx has an implementation of the page rank algorithm (which for some reason is not listed in the reference) that I would believe to be useful, this [code makes use of page rank](https://github.com/EricSchles/text_classify/blob/master/text_classify/textrank.py)

Visualization of data:

Specific Infrastructure to dos:
* create a flask-app for the data visualization:
	* download and add all the necessary d3/c3 files to the static folder
	* set up an api to feed into the visualizations
	* set up templates for each visualization, where the fields are malliable

* Specific Visualization to dos:
	* Discrete Graph Visualization: The networkx/vincent graph visualization suite should be ideal for this kind of task.  However d3 may also be useful.
	* GIS Graph: For this I'd recommend either geodjango/postGIS or [this configuration of tools](https://2015.foss4g-na.org/sites/default/files/slides/Installation%20Guide_%20Spatial%20Data%20Analysis%20in%20Python.pdf)  
	* Classical Graphs and descriptive statistics: Here a combation of CSS type face and C3 is probably best
		* bar charts
		* pie charts
		* time series charts
		* line graphs
		* scatter plots
	* other map ideas:
		* coloring of different related entities

Pattern finding:

This set of todos involves understanding the larger patterns in the data set.  This means doing time series analysis, policy analysis, economic analysis, and a few other key things.  The idea here is to understand what are the determining factors that lead to rise and fall in the supply of commericial sex and what proportion of this commericial sex is human trafficking.  The idea is that magnitudinally human trafficking will be much lower than commericial sex, however proportionally, we can say that there is a correlation between commercial sex and human trafficking, this is verified by internal data, which unfortunately must be taken at face value.  

API Integrations
All data are desireable at the national and local level
* Economic data:
	* housing statistics:
		* number of housing starts
		* percentage of low income housing to total housing
		* number of houses
		* number of apartments
	* jobs numbers
	* proportion of skilled versus unskilled laborers
	* distribution of wealth:
		* percentage of wealthy versus poor 
		* magnitude of wealth of top 1%,5%,10% compared to the bottom 50%
* Demographic data:
	* percentage of males/females in the population
	* percentage of people in each age group:
		* children
		* young adults
		* middle aged/family age
		* older
	* race statistics - percentage of each ethnicity
	* percentage of people with internet access:
		* percentage with high speed internet
		* dial up/ slow internet
		* percentage without internet access
* Law Statistics:
	* Total violent amount of violent/non-violent crime
	* Percentage of violent versus non-violent crime
	* Number of gang arrests per year
	* Percentage change in the number of gang arrests from year to year
	* Total number of prostitution arrests per year
	* Total number of promoting arrests per year
	* Total number of human trafficking arrests per year
	* Total number of domestic violence cases per year
	* Total number of minority deaths by police
* Educational Statistics:
	* Percentage of people graduating from middle school
	* Percentage of people graduating from high school
	* Percentage of people graduating from college
	* Percentage of people graduating from a masters
	* Percentage of people graduating from a PhD
	* average reading scores on standardized tests over time
	* average math scores on standardized tests over time
	* comparison of local scores to national average
* Other interesting statistics:
	* number of charities operating in the area
	* number of libraries per person
	* number of schools per person
	* number of hospitals per person
	* number of afterschool non-profits per person
	* ratio children under age of 18 to number mentors/youth volunteers
	* number of superfund sites
* Backpage/Craigslist:
	* Number of sex work related posts per day - weekday/weekend
	* Total number of posts per day - weekday/weekend
	* number of unique users in sex work section
	* number of ads in sex work section
	* percentage of active versus inactive users in sex work section 
	Definition: an active user is someone who is posting multiple times in a given day/week 
	Note: we may want to break this out into something more categorical/granular
* Twitter:
	* number of sex related conversations on twitter
	* number of sex work related conversations on twitter
	* number of users who have discussed sex on twitter
	* number of users who have discussed sex work on twitter
	* number of pro-sex work users on twitter
	* number of anti-sex work users on twitter
	* percentage of sex related to sex work related conversations on twitter. Question - how often are these from the same users?
	* percentage of sex work related conversations to anti-human trafficking conversations on twitter.
* Facebook
	* number of sex related groups
		* number of members per group
	* number of pimp groups
		* number of members per group

Why this data?

Human Trafficking does not happen in a vacuum it is the confluence of a number of contributing factors that allow for the climate of sex trafficking to occur.  To understand how to address human trafficking from a policy level we need to know what contributing factors are the largest contributors and therefore building a understanding of human trafficking data and various socioeconomic-political factors will allows us to understand their correlation.

Visualization:

Heat Maps:
	* a heat map of how sex conversations flow across users
	* Questions:
		* how do these conversations start?
		* how do these conversations propagate from user to user?
		* who are the central users to these conversations?
		* on average how many users engage actively in a sexually related conversation?
		* on average how many users engage actively in a sex work related conversation?
		* on average how many users engage actively in a pro-sex work conversation?
		* on average how many users engage actively in a anti-sex work conversation?
		* on average how many users engage actively in content that could be human trafficking?
		* on average how many users engage actively in content creation or generation that is anti-human trafficking?
Classical statistics:

	* How has the change in wealth, economic standing and quality of life lead to a change in the amount of sex trafficking on the internet?

	* What is the interplay between the amount of sex on the internet and the amount of sex trafficking on the internet?  How do they move together/how do they diverge?

	* How do the number of mentorship opportunities effect the amount of sex trafficking that happens in an area?
	* How do the number of mentorship opportunities effect the amount of Sex based conversations that happen in an area?

	* Time Series of comparison of education and rise of commerical sex on the internet in america:
		* various time series of each educational statistic against rise of commercial sex on in the internet
	* Time Series of wealth by distribution and rise of commerical sex on the internet in america
	* Time Series of law statistics and rise of commerical sex on the internet in america
	* Time Series of Law,economic factors,and housing factors against the amount of sex trafficking on the internet
* Time Series of the amount of Sex that is discussed on the internet and the amount of sex trafficking on the internet


Map making:

The idea here is to take in a set of data, extract all information that could relate to geographic information - addresses, phone numbers, ip addresses, email addresses and map this to a lat/long and then map this to a location.  This visualization would tie into financial data and other data that human traffickers generate in due course.  The intention would be to visualization a story of time so that investigators could figure out what happened in minutes and then prosecute.  

To Dos here:
* set up geodjango app - https://github.com/EricSchles/pygotham_2015/blob/master/README.md
* create a data standard for how to store:
	* ip addresses
	* phone numbers
	* addresses
	* email addresses
	* lat/long
* create parsers that will create canonical representations of each data point within an entity (as defined in the last step):
	* These parses will do named-entity recognition on addresses, phone numbers, and lat/long

Providence generation:

A custom database that stores documents and pulls out important information from said document on upload.  The document search engine does entity recognition and pulls out names, businesses, phone numbers, email addresses, social media account information, addresses, and other "hard attributes" automatically and generates a json object with all relevant information which can be shown to end users and automatically draws connections between documents.  

This is primarily a design project and the team working on this will need to come up with ideas on what needs to be done and how to do it.


