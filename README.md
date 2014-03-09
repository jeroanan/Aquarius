[![Coverage Status](https://coveralls.io/repos/jeroanan/Aquarius/badge.png)](https://coveralls.io/r/jeroanan/Aquarius) [![Build Status](https://travis-ci.org/jeroanan/Aquarius.png?branch=master)](https://travis-ci.org/jeroanan/Aquarius)

Aquarius
========
Aquarius is an ebook management tool with a web front-end. Users will be able to browse their ebook collection using a web browser or an OPDS-enabled application. Aquarius is written in Python 3.

Installing Aquarius
===================
Aquarius doesn't install as such -- just start it from any directory as described next.

Starting Aquarius
=================
Aquarius is started by running BootStrapper.py in the Aquarius directory. Before running, Config.py should be edited to change the web server port and address.


Architecture
============
There are five main areas in Aquarius:

1. The main application. This is everything not in any other package.
2. Output. Takes care of presenting content to the user. Accessed by the application through the output factory.
3. Persistence. Takes care of storing and retrieving data. Accessed by the application through the persistence factory.
4. Objects. Domain-specific objects for representing data in the system, e.g. books, book types, authors etc.
5. Book harvesting. Finds books for inclusion in the persistence module.

When the application is run, main runs the output and persistence factories. Control is then passed to output. Main passes an instance of itself when control is passed, and output calls main with requests for data, which main delegates to output.

Development Philosophy
======================
Development, where at all possible, is being undertaken using a red-green-refactor test-driven development approach, i.e.:

1. Begin writing a unit test to test a use case. Write just enough of a test to fail/not build
2. Write just enough production code to satisfy the test/clear the build error
3. Repeat 1&2 until the use case is satisfied
4. Refactor what you've written where necessary to keep the code clean

I expect to maintain pretty good/excellent test coverage throughout the development of Aquarius. As of 2014-02-19, test coverage is over 90%, plus some bits of the generated HTML pages that coverage cannot count.

Docstrings -- I don't care for docstrings much, particularly at the function level. Things should be named clearly enough and be single responsibility enough that most docstrings become redundant.

Dependencies
============

* Python 3

The following can be gotten using pip3:

* PyPDF2
* jinja2
* Cherrypy
* sqlite

Helping
=======
After a bit of a hiatus (see JOURNAL), I am planning work to be done in the issue tracker. Feel free to have a look and pitch in if you feel you can help.

Further Reading
===============

* http://opds-spec.org/specs/opds-catalog-1-1-20110627/ -- OPDS specification 1.1. Aquarius will be kept up-to-date with the latest OPDS spec as they become available.
* http://www.cherrypy.org/ -- The most excellent CherryPy minimalist Python web framework.
