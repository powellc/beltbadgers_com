.. _installation:

============
Installation
============
:Author: Colin Powell <colin.powell@gmail.com>
:Date: $Date: 2013-10-16 11:50:00 +0500 $
:Revision: $Revision: 1
:Description: How to install beltbadgers.com site code

The easiest way to get started with BeltBadgers.com is to run the ansible
playbook included. Firstly set your server's IP address in the ansible/hosts
file, then::

  ansible-playbook -i hosts provision.yml

Alternatly, if you'd like to set it up locally just to test it you can just
use vagrant to bring it up. First make sure you have Virtualbox an Vagrant 
installed, then::

  vagrant up

Should be good to go! The fixtures file includes some starter tests and will
set the admin user/password up as: admin/belted
