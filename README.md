Silly scifi novel titles
========================

`application.py` uses the Requests library to grab a list of titles of wiki pages in the Electromagnetism category, filter out everything that isn't a two-word title, make sets out of the first and second words of each title, and then spit out ten mix-and-match nonsense titles. Then Flask should spit that into the title parameter for the template in titles.html. Every page reload makes another call to the API and thus delivers a fresh set of fake physics-sounding phrases.  Further explanation: http://www.harihareswara.net/sumana/2013/10/09/0

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Possible ways to expand this:
=============================

1. Add options for the reader to ask for biology or geology phrases
1. Add real phrases and make a game challenging the reader to tell true from fake
1. Grab author names and use Queneau assembly to offer mashed-up bylines as well, e.g., "Optical Reluctance by Vandana Bujold"
