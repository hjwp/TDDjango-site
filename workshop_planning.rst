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

   - first FT - the admin site (136 LOC)
     
   - second FT part 0 - the inline choices admin (100LOC)
         (give out Gertrude/inlines part?? ~ 50)

   - second FT part 1 - the polls page (94LOC)

   - second FT part 2 - poll page, generating the form
        (give out the unit test?)

   - second FT part 3 - processing the form
     96

   - if time - javascript on button?

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
