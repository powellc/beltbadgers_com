.. _introduction:

============
Introduction
============
:Author: Colin Powell <colin.powell@gmail.com>
:Date: $Date: 2013-10-16 11:36:00 +0500 $
:Revision: $Revision: 1
:Description: An introduction to beltbadgers.com site code

Welcome to the source code that powers beltbadgers.com! Belt Badgers was 
heavily inspired by `Google Apps Ninja`__. At it's core, it's a system for
managing knowledge-base quizes of increasing difficutly. As a user completes
quizzes, they are awarded increasingly higher "belt" badges that allow
them and other users to recognize their domain expertise.

The site users are broken down into two major groups:

1. Students
2. Masters

When a student joins the site, they are able to access their profile page and
any publicly-accessible tests. They can also be invited to join one or more
dojos, which then gives them access to any tests that are private to the dojos
they are members of.

Masters are the owners of dojos. The first person to create a dojo becomes
the master of that dojo. They can also make other students co-masters of
their dojos. As a master, they control the ability to add new tests to their
dojo as well as set the order tests must be achieved and the belts awarded.

Installation
------------

The beltbadgers.com site code is managed via an ansible playbook and can be
bootstrapped either locally via VirtualBox/Vagrant, or on a remote sever.

For more information, see the :ref:`Installation document <installation>`

.. __`Google Apps Ninja`: https://sites.google.com/a/isb.ac.th/ninjatraining/
