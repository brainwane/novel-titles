#!/usr/bin/python
# Copyright 2013 Sumana Harihareswara, GPL, thanks to https://github.com/bev-a-tron/MyFlaskTutorial

# This should use the Requests library to grab a list of titles of wiki pages in the Electromagnetism
# category, filter out everything that isn't a two-word title, make sets out of the first and second
# words of each title, and then spit out ten mix-and-match nonsense titles. Then Flask should spit that
# into the title parameter for the template in titles.html.
# Test list:
# ['No feigning surprise', 'No well-actuallys', 'No backseat driving', 'No subtle -isms', 'Two strings', 'Quantum heat']

import random
import requests
from flask import Flask,render_template
app_fl = Flask(__name__)

@app_fl.route('/index')
def index_pg():
    electro = "http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&format=json&cmtitle=Category%3AElectromagnetism&cmlimit=150"
    response = requests.get(electro)
    pagetitles = [response.json()["query"]["categorymembers"][i]["title"] for i in range(len(response.json()["query"]["categorymembers"]))]
    adj, noun = massagelist(pagetitles)
    sugg = wackytitles(adj, noun)
    return render_template('titles.html',title=sugg)

def wordcount(phrase):
    return len(phrase.split())

def massagelist(originals):
    originals = [x for x in originals if wordcount(x) == 2]
    first = set([x.split()[0] for x in originals])
    second = set([x.split()[1] for x in originals])
    return first,second

def wackytitles(set1,set2):
    adjectives, nouns = list(set1), list(set2)
    titles = "<ol>"
    for i in range(10):
        titles = titles + "<li>" + random.choice(adjectives) + " " + random.choice(nouns).title() + '</li>'
    titles = titles + "</ol>"
    return titles



if __name__ == '__main__':
    app_fl.run(debug=True)
