# Udacity-FSND-Prj3.1
Log Analysis Project

1. Prepare Vagrant environment

1.1 Install VirtualBox

Download and instrall the platform package for your current operating system via: https://www.virtualbox.org/wiki/Downloads

1.2 Install Vagrant

Download and install the Vagrant software via: https://www.vagrantup.com/downloads.html

1.3 Download FSND VM configuration

Either download and unzip the FSND VM configuration file from: https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip or clone the repo: https://github.com/udacity/fullstack-nanodegree-vm

In your terminal, navigate to the folder where configration files are located. Change directory to "vagrant" and start the virtual machine by runnning command "vagrant up".

Once the VM configration is complete, log in your VM by command "vagrant ssh".

1.4 Load the data

Download the datafile from: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip. Unzip the files and place the sql file in your vagrant folder.

In your terminal, log in your vagrant VW and change directory to "vagrant" and then run the following command:

psql -d news -f newsdata.sql

1.5 Run the data analysis python application

Run the python file by runnning: ./news.py
There are 3 sections in the report: 1) Listing of top 3 articles by their view numbers; 2) Listing of authors by the total view numbers of their articles; 3) The date when more than 2% HTTP requests led to errors.

The python program first defines a function to properly reconstitute the data in SQL format. 
Then it executes SQL queries that generate results as required by the project rubric.

The following are codes to create two views used in the main python program:

create view error as select count(*) as num, DATE(log.time) from log where status LIKE '%404%' group by DATE;

create view total as select count(*) as num, DATE(log.time) from log group by DATE;
