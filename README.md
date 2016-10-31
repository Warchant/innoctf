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

More about platform: [picoctf wiki](./GettingStarted.md).


Setting Up
------------
```bash
$ git clone https://github.com/Warchant/innoctf && cd innoctf
$ export VAGRANT_PATH=/innoctf
$ sudo mkdir -p db            # must be owned by root:root! 
$ sudo mkdir -p logs/nginx    # must be owned by root:root!
$ docker-compose up
```

## Creating problems

Refer to [problems.md](./problems.md) instruction.

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
$ cd ${VAGRANT_PATH}/web
$ sudo jekyll build
```


Loading the Example Problems (In the vagrant VM)
------------
1. Run `cd ${VAGRANT_PATH}/api`
2. Run `python3 api_manager.py -v problems load /vagrant/example_problems/ graders/ ../problem_static/`
3. Run `python3 api_manager.py autogen build 100`



Getting Started
---------------

A detailed explanation of the basics of the picoCTF Platform 2 can be found in our [Getting Started Guide](GettingStarted.md).
