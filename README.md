# Udacity-FSND-Prj3.1
Log Analysis Project

The python program first defines a function to properly reconstitute the data in SQL format. 
Then it executes SQL queries that generate results as required by the project rubric.

The following are codes to create two views used in the main python program:

create view error as select count(*) as num, DATE(log.time) from log where status LIKE '%404%' group by DATE;

create view total as select count(*) as num, DATE(log.time) from log group by DATE;
