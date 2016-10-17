# InnoCTF

picoCTF-Platform 2
-----------

The picoCTF Platform 2 is the infrastructure on which picoCTF runs. The 
platform is designed to be easily adapted to other CTF or programming 
competitions.

picoCTF Platform 2 targets Ubuntu 14.04 LTS but should work on just about 
any "standard" Linux distribution. It would probably even work on 
Windows. MongoDB must be installed; all default configurations should 
work.

More about platform: [picoctf wiki](https://github.com/picoCTF/picoCTF-platform/wiki).

Setting Up
------------
```bash
$ ssh vagrant@188.130.155.34 -p 6174 # connect to vagrant VM
$ devploy                            # to reload web server, apply config, etc
```

Creating news
------------
All posts are in the folder `/home/vagrant/web/_posts`. 

To create new post:

  - Create new file with name `YYYY-MM-DD-postname.markdown at `/home/vagrant/web/_posts`
  - Add this header:
```
---
title:  "Name of the post"  # post title
date:   2015-01-01 17:29:23 # date 
categories: ctfs awesome    # category
---
```
  - Use Markdown to fill post content.
  - Publish post:
```bash
# run this inside VM
$ jekyll-reload-pages 
```


Loading the Example Problems (In the vagrant VM)
------------
1. Run `cd ~/api`
2. Run `python3 api_manager.py -v problems load /vagrant/example_problems/ graders/ ../problem_static/`
3. Run `python3 api_manager.py autogen build 100`
4. Run `devploy`


Running the Regression Tests
----------------------------

The platform comes with a series of regression tests that should be run before any change is committed to the API.
To run the tests:

1. `vagrant ssh` into your virtual machine.
2. Run `devploy` to bring up an instance from your latest code.
3. To be able to import the API, `cd api` and run the tests with `./run_tests.sh`
 
All tests should pass with your changes.


Getting Started
---------------

A detailed explanation of the basics of the picoCTF Platform 2 can be found in our [Getting Started Guide](GettingStarted.md).
