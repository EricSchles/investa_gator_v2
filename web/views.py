from flask import Flask, render_template, redirect,request,url_for
import pickle
# import investigate
from crawler.data_grab import Scraper
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

