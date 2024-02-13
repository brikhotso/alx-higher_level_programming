#*SQL - Introduction*

##What’s a database?
A database is an organized collection of structured information or data, typically stored electronically in a computer system. It's designed to efficiently manage, store, retrieve, and manipulate data according to various requirements and constraints.

##What’s a relational database?
A relational database is a type of database that organizes data into tables (or relations) which are interconnected based on predefined relationships. It uses a relational model where data is stored in rows and columns, and relationships between tables are established using keys.

##What does SQL stand for?
SQL stands for Structured Query Language. It's a standard programming language used to manage and manipulate relational databases. SQL is used for tasks such as querying data, updating data, and defining and modifying the structure of databases and their tables.

##What’s MySQL?
MySQL is an open-source relational database management system (RDBMS) that uses SQL. It's widely used for web applications and is known for its reliability, scalability, and ease of use. MySQL is developed, distributed, and supported by Oracle Corporation.

##How to create a database in MySQL?
You can create a database in MySQL using the CREATE DATABASE statement. For example:
sql```
CREATE DATABASE dbname;
```

##What does DDL and DML stand for?

DDL stands for Data Definition Language. It includes SQL commands used to define the structure of a database, such as creating, altering, and dropping database objects like tables, indexes, etc.
DML stands for Data Manipulation Language. It includes SQL commands used to manipulate data within a database, such as inserting, updating, deleting, and querying data.

##How to CREATE or ALTER a table?

To create a table, you use the CREATE TABLE statement. For example:
sql```
CREATE TABLE tablename (
  column1 datatype,
  column2 datatype,
  ...
);
```

To alter a table, you use the ALTER TABLE statement. For example:
sql```
ALTER TABLE tablename
ADD columnname datatype;
```

##How to SELECT data from a table?
You use the SELECT statement to retrieve data from one or more tables. For example:

sql```
SELECT column1, column2
FROM tablename
WHERE condition;
```

##How to INSERT, UPDATE, or DELETE data?

To insert data into a table, you use the INSERT INTO statement. For example:
sql```
INSERT INTO tablename (column1, column2)
VALUES (value1, value2);
```

To update data in a table, you use the UPDATE statement. For example:
sql```
UPDATE tablename
SET column1 = value1
WHERE condition;
```

To delete data from a table, you use the DELETE FROM statement. For example:
sql```
DELETE FROM tablename
WHERE condition;
```

##What are subqueries?
Subqueries, also known as nested queries or inner queries, are SQL queries that are embedded within another query. They can be used within SELECT, INSERT, UPDATE, or DELETE statements to perform operations based on the results of another query.

##How to use MySQL functions?
MySQL provides a variety of built-in functions that can be used to perform operations on data. You can use functions like SUM, COUNT, AVG, MAX, MIN, etc., to perform calculations or aggregate data. You can also use functions for string manipulation, date and time operations, and more. The syntax for using functions depends on the specific function being used.