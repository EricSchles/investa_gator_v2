from flask import Flask, render_template, redirect,request,url_for
import pickle
# import investigate
from crawler import Scraper
from web import app

@app.route("/",methods=["GET","POST"])
def index():
    #connections found between ads
    #keywords found
    return render_template("index.html")

@app.route("/run",methods=["GET","POST"])
def run():
    scraper = Scraper()
    data = scraper.scrape(auto_learn=True)
    return redirect(url_for("index"))

@app.route("/investigate",methods=["GET","POST"])
def investigator():
    password = request.form.get("password")
    running = request.form.get("long_running")
    if password == "like_i_d_tell_you":
        if running == "long":
            investigate.run()
        else:
            investigate.run(long_running=False)
    return redirect(url_for("index"))

@app.route("/add",methods=["GET","POST"])
def add():
    return render_template("add.html")

@app.route("/add_numbers",methods=["GET","POST"])
def add_numbers():
    numbers = pickle.load( open("numbers.p","rb") )
    network = request.form.get("network")
    number = request.form.get("number")
    if not network in numbers.keys():
        numbers[network] = []
    numbers[network].append(number)
    return redirect(url_for("index"))

@app.route("/add_data",methods=["GET","POST"])
def add_data():
    investigation_type = request.form.get("investigation_type")
    url = request.form.get("url_list")
    urls = url.split(",")
    scraper = Scraper()
    data = scraper.scrape(links=urls,auto_learn=True)
    if investigation_type == "directed":
        keywords = pickle.load( open("keywords.p", "rb"))
        for datum in data:
            keywords += datum["new_keywords"]
        pickle.dump(keywords, open("keywords.p","wb"))
    elif investigation_type == "undirected":
        train = pickle.load( open("train.p","rb"))
        for datum in data:
            train.append((datum["text_body"],"trafficking"))
        pickle.dump( train, open("train.p","wb") )
    return redirect(url_for("index"))

#add routes for visualization of existing datasources
#things to do:
#1) word cloud
#2) frequency of words with a histogram
#3) network graph
#4) number of successful scrapes and number of unsucessful scrapes, for parameter tuning
#5) add google automation - search for phone numbers, email addresses, store results
#6) generate bank requests?

#machine learning stuff:
#add automated analysis
#1) based on historical data, say how likely this add is trafficking
#2) how likely this person is a prostitute
#3) likelihood of age, ethnicity, gender, average number of years they've been trafficked
#4) were they brought into this country?
#5) Do they have children? Do they have children with their trafficker?
#6) likelihood of money laundering

#modeling of financial data
#1) prove money laundering from bank statements

#optimal legislative strategy
#A set of parameters that indicate the success of a given
#case.  Therefore maximal resources are placed into cases as
#more information is discovered.  Thus leading to the maximum number
#of convictions.

#optimal decision making will be made based on past history
