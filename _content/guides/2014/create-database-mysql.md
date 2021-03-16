# Creating A New Database in MySql

- date: 2014-06-04 14:40
- tags: database, linux
- category: guides

------------------------------


### 0. Setup

```bash

$ sudo apt-get install mysql-server
$ mysql -u root -p <root_password>

```


### 1. Create the database

```sql

CREATE DATABASE mytestdb;
show databases;

```

### 2. Create a user and grant access

```sql

CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'my_password';

GRANT ALL PRIVILEGES ON mytestdb.* TO 'myuser'@'localhost'; 

-- or alternatively, with more powerful access
GRANT ALL PRIVILEGES ON mytestdb.* TO 'admin'@'%' WITH GRANT OPTION;

```

### 3. Login with the User

```bash

mysql -u myuser -p mytestdb

```

### 4. Import a SQL dump into database

```sql

USE mytestdb;
source db_dump.sql;

```

Or you can use a command line:

```bash

mysql -u dbuser -p [-h host] dbname < dbdump.sql

```

Exporting in command line is similar, using "mysqldump" command:

```bash

mysqldump -u dbuser -p dbname > dbdump.sql

```


