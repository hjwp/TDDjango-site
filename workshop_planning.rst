Workshop outline
================

intro

 - who i am, resolver etc

 - who knows what:
     - django?
     - unit testing?
     - selenium?

 - plan - to run through contents of Django tutorial
    - ie, a polls/voting app

     - I will distribute the functional test runner

     - I will also distribute comments-only versions of the FTs
       - these will contain a few hints
       - feel free to tweak, but not too muuch!

     - We'll go through 4 stages, if you don't quite finish a stage,
       you can pull from my repo - will have tags

     - We'll do the first stage together - I'll do it in front of you

     - Can do second stage as well if it works well, or just go ahead...

     - the approach: full TDD:
       - no code before tests

       - fts first - Selenium

       - then unit tests - unittest & Django Test Client

(20 mins)

 - outline
   - set up, make sure everyone has ft runner, project etc (10 mins)

   - PART 1: BASIC ADMIN SITE - setup admin site, add Poll model (136 LOC)

     - do together.

     - unit testing models

     - __unicode__ (and verbose_name?)
     
   - PART 2: HOME PAGE POLLS LISTING

     - do together.

     - pre-prepared: FT + code for inline admin, choice model etc.

     - FT specc'd out as comments

     - (94LOC)

   - PART 3: VOTE ON A POLL

     - free for all, but:

     - give out unit test for poll view 

     - let ppl find their own way around forms.py

   - PART 4: FORM PROCESSING (if time)

     - tbc

   - some discussion topics
     - testing philosophy... "testing constants"
       - example: max_length... verbose_name...

     - databases and fixtures for FTs
     

Materials:
  - ft runner

  - webdriver docs

  - django docs
    - general
    - the test client

  - useful unit test methods
