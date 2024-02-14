# SQL_more_queries

## How to create a new MySQL user:
You can create a new MySQL user using the CREATE USER statement. Here's an example:

```
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

Replace 'username' with the desired username and 'password' with the desired password. You can also specify the hostname ('localhost' in this example) from which the user is allowed to connect.

## How to manage privileges for a user to a database or table:
You can manage privileges using the GRANT and REVOKE statements. For example, to grant all privileges to a user on a specific database:

```
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
```

And to revoke privileges:

```
REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'localhost';
```

## What’s a PRIMARY KEY:
A PRIMARY KEY is a column or a set of columns that uniquely identifies each row in a table. It ensures that there are no duplicate rows in the table. Each table can have only one PRIMARY KEY constraint.

## What’s a FOREIGN KEY:
A FOREIGN KEY is a column or a set of columns that establishes a relationship between data in two tables. It ensures referential integrity by enforcing a link between the data in the foreign key column(s) and the primary key or a unique key in another table.

## How to use NOT NULL and UNIQUE constraints:

NOT NULL constraint ensures that a column cannot contain NULL values.
UNIQUE constraint ensures that all values in a column (or a combination of columns) are unique.
Example:

```
CREATE TABLE table_name (
    column1 INT NOT NULL,
    column2 VARCHAR(50) UNIQUE
);
```

## How to retrieve data from multiple tables in one request:
You can use JOIN operations to retrieve data from multiple tables in a single query. For example, using INNER JOIN:

```
SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;
```

## What are subqueries:
Subqueries are SQL queries nested within another query. They are used to perform operations based on the result of another query. For example:

```
SELECT column1 FROM table1 WHERE column2 IN (SELECT column2 FROM table2 WHERE condition);
```

## What are JOIN and UNION:

JOIN: JOIN is used to combine rows from two or more tables based on a related column between them. Types of JOINs include INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.
UNION: UNION is used to combine the result sets of two or more SELECT statements into a single result set, removing duplicate rows by default. There's also UNION ALL, which retains duplicate rows.