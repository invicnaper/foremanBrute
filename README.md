[![GitHub license](https://img.shields.io/badge/license-GPLv2-blue.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/author-naper-blue.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
[![GitHub license](https://img.shields.io/badge/version-0.0.1-orange.svg)](https://raw.githubusercontent.com/Facetracker-project/facetracker-core/master/COPYING)
# foremanBrute
a script that allows you To bruteForce the login page of Foreman

This README would normally document whatever steps are necessary to get foremanBrute up and running.

### What is this repository for? ###

* foremanBrute allows you To bruteForce the login page of Foreman
* Version 0.0.1

### Screen ###

![alt text](https://nsa40.casimages.com/img/2019/01/16/190116014227605236.png "foremanBrute screen0")
![alt text](https://nsa40.casimages.com/img/2019/01/16/190116014227872813.png "foremanBrute screen1")

# Install Using Vagrant ?
you must have Vagrant installed on your machine, for Debian based OS use :

    $ sudo apt-get install vagrant
    
install virtualBox as a provider for Vagrant

    $ sudo apt-get install virtualbox
    
    $ vagrant plugin install virtualbox
    
then you can Vagrant up

    $ vagrant up
    
the vagrantfile is configured to use Puppet as a provisonner, which allows you to quickly install dependencies and try foremanbrute.

after the vagrant up you can ssh to foremanBrute using

    $ vagrant ssh
    
then run foremanBrute using 

    $ sudo foremanBrute
    
![alt text](https://nsa40.casimages.com/img/2019/01/16/190116015010818105.png "foremanBrute vagrant")

# Install manually ?
to use foremanBrute , you need to install thoses packages :
  * requests
  * beautifulsoup
  
# Linux (Ubuntu) / MAC OSx
pip to install bs
  
    $ pip install beautifulsoup
    
    $ pip install requests
    
    
# How to use ?
you can run foremanBrute using 

      $ foremanBrute.py --help
      
![alt text](https://nsa40.casimages.com/img/2019/01/16/190116020409791640.png "foremanBrute help")

using a username with a password list

      $ foremanBrute.py -l admin -p passwordlist -u https://192.168.40.30/users/login -m "Incorrect username or password"

### Contributors ###

* Hamza Bourrahim
