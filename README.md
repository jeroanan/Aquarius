Aquarius
========
Aquarius is an EBook management tool with a web front-end. Users will be able to browse their ebook collection using a web browser or an OPDS-enabled application. Aquarius is written in Python 3.

Installing Aquarius
===================
Aquarius doesn't install as such -- just start it from any directory as described next.

Starting Aquarius
=================
Aquarius is started by running bootstrapper.py in the Aquarius directory. Before running, config.py can be edited to change the web server port and address.

Current Features
================
Currently, Aquarius can:

* Provide console-based searches
* Give a web front-end accessible by a web browser. It doesn't look very nice or do much yet.
* Give an OPDS front-end that is browsable by compatible applications. The OPDS interface allows the user to browse books by title and search for books. Books can then be downloaded.

Upcoming features
=================
* A proper database is needed. At the moment it just gets some hardcoded data from hardcodedpersistence.py. This has enabled me to focus on other functionality and leave defining a proper database until the software is a little more mature. I hope this will allow me to define the bulk of what's required in the database up-front, rather than constantly making changes.

* The web-based interface as it stands is pretty rudimentary. Need to make nice slick pages and bring that whole side of the interface up to the same level as the OPDS interface. Web pages will be written using HTML5.

Architecture
============
There are four main areas in Aquarius:

1. The main application. This is everything not in any other package.
2. Output. Takes care of presenting content to the user. Accessed by the application through the output factory.
3. Persistence. Takes care of storing and retrieving data. Accessed by the application through the persistence factory.
4. Objects. Domain-specific objects for representing data in the system, e.g. books, book types, authors etc.

When the application is run, main runs the output and persistence factories. Control is then passed to output. Main passes an instance of itself when control is passed, and output calls main with requests for data, which main delegates to output.

Development Philosophy
======================
Development, where at all possible, is being undertaken using a red-green-refactor test-driven development approach, i.e.:

1. Begin writing a unit test to test a use case. Write just enough of a test to fail/not build
2. Write just enough production code to satisfy the test/clear the build error
3. Repeat 1&2 until the use case is satisfied
4. Refactor what you've written where necessary to keep the code clean

I expect to maintain pretty good/excellent test coverage throughout the development of Aquarius.

Coding conventions -- Might follow PEP8 at some point. I'm not greatly bothered though, as long as things are neat/consistent enough.

Docstrings -- I don't care for docstrings much, particularly at the function level. Things should be named clearly enough and be single responsibility enough that most docstrings become redundant.

Dependencies
============

* Python 3
* Cherrypy
* jinja2
* sqlite

Further Reading
===============

* http://opds-spec.org/specs/opds-catalog-1-1-20110627/ -- OPDS specification 1.1. Aquarius will be kept up-to-date with the latest OPDS spec as they become available.

* http://www.cherrypy.org/ -- The most excellent CherryPy minimalist Python web framework.
