Title
=====

Fully Test-Driven Web Development with Django and Selenium

Description
===========

tl; dr:

 * The concept: run through the official Django tutorial, but with full TDD
 * Includes browser-based testing with Selenium, using the new WebDriver API
 * In-depth unit-testing, including the Django Test Client
 * Discussions of TDD philosophy: what to test, what not to test, how to test

http://www.tdd-django-tutorial.com/

https://github.com/hjwp/Test-Driven-Django-Tutorial

 * Come prepared! you’ll need **git**, **firefox**, **python2.7**, **django1.4** and **selenium** installed.


Abstract
========

Fully Test-Driven Django with Selenium
--------------------------------------

*AKA “The Django Pony vs The Testing Goat”*

This tutorial is aimed primarily at people who want to learn about one or many of:

 * Django
 * Selenium
 * Test-Driven-Development

So it’s aimed at beginners of one kind or another – if you are already well versed in all three, then you may not get much out of it.

The idea is to run through the steps covered by the official Django tutorial, covering the essentials of Django from a beginner’s point of view. However, at each stage, instead of “just” writing the Django code required to build our site, we first write tests.

And we don’t just write unit tests! We start by writing “functional” or “acceptance” tests, using Selenium - which means driving a real browser, and checking the actual behaviour of the site as it is rendered, from the user’s point of view.

Why should you listen to me, I hear you ask?
--------------------------------------------

Well, I was lucky enough to get my first “proper” software development job about two years ago with a bunch of Extreme Programming fanatics, who’ve thoroughly inculcated me into their cult of Test-Driven development. Believe me when I say I’m contrary enough to have questioned every single practice, challenged every single decision, moaned about every extra minute spent doing “pointless” tests instead of writing “proper” code. But I’ve come round to the idea now, and whenever I’ve had to go back to some of my old projects which don’t have tests, boy have I ever realised the wisdom of the approach. So, I’ve learnt from some really good people, and the learning process is still fresh in my mind, and most importantly, I still have the passion of a recent convert!

Pre-requisites
--------------

Come with the following pre-installed on your laptop please:

 * Git
 * Firefox
 * Python 2.7
 * setuptools/easy_install/pip then:
 * pip install django
 * pip install selenium
 * pip install mock



Video of this workshop at EuroPython 2012
-----------------------------------------

https://www.youtube.com/watch?v=WfyoC0h9QKA



Additional information
======================

Background
----------

I've been doing these tutorials for just over a year now - I've done several in London, at PyCon UK and most recently and EuroPython; you can see the latter on the video link below.

I definitely enjoy giving them. Some of it is because of a natural exuberance, but most of it is due to the pleasure of sharing knowledge - I think the kind of TDD that we practice at Resolver is unusually rigorous, and after many months of griping about how unnecessary it all seems, I've really come to see the wisdom of it all. TDD is a good thing, and we should all be doing more of it, but I know that sometimes there is a barrier -- certainly in my experience of learning Python (from Dive Into Python), reading about TDD left me thinking "well that sounds like a really good idea", but when it came to putting into practice I somehow just didn't do it... I think partially because it was just a bit too unfamiliar, I didn't quite know where to start. I get the feeling that's something a lot of people experience, and these tutorials are meant to give people "a place to start".  Starting from scratch, putting the building blocks in place one by one, showing how you can use TDD from the very start of a project, and these tutorials are meant to give people "a place to start".  Starting from scratch, putting the building blocks in place one by one, showing how you can use TDD from the very start of a project.


How I run the sessions
----------------------

I present using a console - usually I set the projector up to have a terminal full-screened to it, and I use screen to have a copy of that terminal visible on my laptop screen. That means people can follow along with the actual command-lines I need to execute, and see my edit sessions in vi.  Aside from that, I get people to check-out a copy of my tutorial repo, which has tags for the various stages of the tutorial, and includes the full text of my written tutorials, which they can use to crib from where necessary.


In terms of how I run the classes, I want to make sure that "everyone gets it" - so in effect we go at the speed of the slowest person.  I've found people react well to that, the idea that no-one is left behind, but there are some risks and downsides:  software/hardware/config/bugs you just can't resolve, faster learners getting bored, and the general fact that, the larger the class, the more problems you have, so the slower everything goes.

So, I like to put in place some mitigation practices:

1. The tutorial is split into stages, and each stage is self-contained.  As a last resort, someone who gets hopelessly lost at an early stage can start the next stage "from fresh", by doing a git checkout from the tutorial repo...  But it also means that I can have the whole class "skip ahead", to skip over intermediary steps that are less interesting, or less relevant to what's being learnt.

2. I have a few "advanced challenges" to give to the faster learners, to keep them busy while I go round and help the slower learners

3. I try to team up with a co-presenter, who also goes round and helps people (see below)

4. In big classes, I ask people to "pair program", or work in teams, to bring the "effective" headcount down - I like to keep it below 20 teams.  That also helps because you'll usually find that people who are a bit more experienced can help out the beginners.


Aside from that, I just like to keep things lively and entertaining.  Here's what a past attendee said:



"HUGE thanks for your great presentation at europython. I loved your presentation style (especially how you jumped on various chairs and tables)"

http://www.tdd-django-tutorial.com/blog/articles/2012/tutorials-updated-django-14-and-its-weird-new-fold/#comment-612104353

(no chairs or tables were harmed during the tutorial)


Audience / prerequisites
------------------------

There really are no real skills required from the audience - it's aimed at beginners, whether they're new to Django, Selenium, TDD or even Python (that's happened several times!)

On the other hand, having people arrive with all the necessary software preinstalled is a big help, so that's why I've tried to highlight the pre-req installs in the descriptions above.  No matter what you do though, someone always arrives unprepared, and what I tend to do is get them to pair up with someone with a working laptop


Co-presenter / Assistants
-------------------------

I'm keen to have a co-presenter, especially if we anticipate a larger class size.  I'm hoping I can call on Jonathan Hartley, who's done it with me before, and is a regular PyCon attendee & presenter... But he has a new baby, so failing that I should be able to rope in one of my colleagues from PythonAnywhere.  A "tutorial assistant" could potentially work, as long as they were familiar with the material (ie, if they could find time to go through the tutorial online)



Video of this workshop at EuroPython 2012
-----------------------------------------

https://www.youtube.com/watch?v=WfyoC0h9QKA

Skip to about 9 mins in for it to actually begin.  Sound occasionally fails, technical problems with the EP2012 a/v setup I guess.  

Here's another video of me presenting a lightning talk on a different topic (PythonAnywhere) at PyConUK

https://www.youtube.com/watch?v=e6NLAbgmRZ4


