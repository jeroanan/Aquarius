Aquarius
========
Aquarius is an ebook management tool with a web front-end. Users will be able to browse their ebook collection using a web browser or an OPDS-enabled application. Aquarius is written in Python 3.

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
* Give a web front-end accessible by a web browser. 
* Give an OPDS front-end that is browsable by compatible applications.

The web and OPDs front-ends allow the user to search for books based on title and author. Search results can then be downloaded. Only ebooks that are in epub format are supported at the moment.

To-Do List
=================

* The web-based interface as it stands is still under development and will evolve as the application matures.

* Get support included for more book formats. As a priority I'd like to get .MOBI and .PDF support.

* Add support for more metadata for epub books.

* The epub class, aquarius/bookformats/epub.py is not dependent on anything else in the application. It could be used by others, so I would like to put it into its own repo and include it in Aquarius as a third-party library. Further development of epub.py would be made by me to support the development of Aquarius. I imagine that in time this will become the case for upcoming classes that handle book formats.

* Look at PEP8 compliance. Even at this stage it would be a fair amount of effort, so it may happen piecemeal/over several days.

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

I expect to maintain pretty good/excellent test coverage throughout the development of Aquarius. As of 2013-12-30, test coverage is at 93%, plus some bits of the generated HTML pages that coverage cannot count.

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
