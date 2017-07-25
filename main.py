# use repl.it for compiling
# http library that allows python to access webpages, easy and fast xml and html library in python, same as soup 4 but easier and faster to pick up
# ideal for static webpages
from lxml import html
import requests
# should help with rate limiting
from ratelimit import *
import requests
# allows you to analyze the contents of the page (python parsing library), specifically for messy sites
from bs4 import BeautifulSoup
from urllib2 import urlopen
# web automation library, open up the browser and navigate to desired pages
import selenium
# DO RESEARCH ON THIS LIBRARY TO UNDERSTAND EXACTLY WHAT IT DOES 07-19-17, sounds useful refer to reseources
import scrapy

# set up retrieving the contents from each indvidual webpage
# EV google search webpage content, find another library, other possible solutions include xgoogle and json
# replace with bs4 library for google search scraping and jdpower
# be careul with rate limiting (the amount of requests that are allowed for a webpage)
googleEVSearchWebpage = request.get('https://www.google.com/#q=electric+vehicles')
googleSearchTree = html.fromstring(googleEVSearchWebpage.content)

# EV google plus search webpage content
googlePlusEVSearchWebpage = request.get('https://plus.google.com/+Cool-electric-cars')
googlePlusEVSearchTree = html.fromstring(googlePlusEVSearchWebpage.content)

# jdpower search webpage content
jdpowerSearchWebpage = request.get('https://plus.google.com/+Cool-electric-cars')
jdpowerSearchTree = html.fromstring(jdpowerSearchWebpage.content)

# extract and print names of evs from plugincars
from bs4 import BeautifulSoup
import urllib2

plugincarsUrl = raw_inputs("www.plugincars.com/cars")

plugincarsR = requests.get("http://"+plugincarsUrl)

plugincarsData = plugincarsR.text

#plugincarsContent = urllib2.urlopen(plugincarsUrl).read()

plugincarsSoup = BeautifulSoup(plugincarsData)

print plugincarsSoup.prettify()

print plugincarsSoup.title.string
