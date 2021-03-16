# PostgesSQL 9 Administration QuickRef(1) - Exploring Database

- date: 2014-03-06 15:27
- tags: postgresql, database
- category: tricks

----------------------------
The most cheat sheets or quick references I found are organized by knowledge domains, but I would rather like a quick reference organized by tasks. Thus I make this reference.

# Part I: Exploring Database

### 1. Basic Information
Default location of data files (in debian/ubuntu): ```/var/lib/postgresql/9.1/main/```
Data files for an instance:
	base		-	data directory for databases 
	global		-	database catalog tables(shared across databases)
	pg_clog	- transaction status files
	pg_multixact	-	row-level lock status files
	pg_subtrans	-	subtransaction status files	
	pg_tblspc		-	links to external tablespaces
	pg_twophase	-	prepared transaction status
	pg_xlog		-	WAL(Write-Ahead Log) transaction log
Log files: ```/var/log/postgresql/```
	
 
PostgreSQL command line programs:

```bash
# check psql version
$ psql --version
# check configuration variables
$ pg_config
# run a single command
$ psql -c "\d"
```

PSQL text client:

```psql
-- line comment
/ *multi-line comment* /
-- check server version
postgres=# SELECT version();
-- output query result as one column per line
postgres=# \x
```

### 2. Server Stats

```bash
# list databases
$ psql -l
# list tables in a database
$ psql -c "\d" -d somedb
```

``` psql
-- check server uptime
postgres=# SELECT date_trunc('second', current_timestamp - pg_postmaster_start_time()) as uptime;

-- list database names
postgres=# SELECT datname from pg_database;
-- list tables in databases;
postgres=# SELECT table_catalog, table_schema, table_name, table_type from information_schema.tables;
postgres=# \dt+

-- check database size
postgres=# SELECT pg_database_size('somedb');
postgres=# SELECT pg_database_size(current_database());
-- check table size
postgres=# \dt+ some_table
postgres=# SELECT pg_relation_size('some_table');
postgres=# SELECT pg_total_relation_size('some_table'); -- including indexes and other related space
-- list table sizes in order
postgres=# SELECT table_name, pg_total_relation_size(table_name) as size
FROM information_schema.tables NOT IN ('information_schema', 'pg_catalog')
ORDER BY size DESC;

-- check online users/clients
postgres=# SELECT  from pg_stat_activity;
postgres=# SELECT datname, usename, client_addr, client_port FROM pg_stat_activity;

-- track user activities(like check user's pending query)
postgres=# SET track_activities = on;
postgres=# SELECT datname, username, current_query 
FROM pg_stat_activity 
WHERE current_query != '<IDLE>';
postgres=# SELECT current_timestamp - query_start as runtime, datname, usename, current_query 
FROM pg_stat_activity
WHERE current_query != '<IDLE>'
ORDER BY 1 DESC;
postgres=# SELECT datname, usename, current_query
FROM pg_stat_activity
WHERE waiting;

-- check who is blocking the queries
postgres=# SELECT 
	w.current_query as waiting_query,
	w.procpid as w_pid,
	w.usename as w_user,
	l.current_query as locking_query,
	l.procpid as l_pid,
	l.usename as l_user,
	t.schemaname || '-' || t.relname as tablename
FROM pg_stat_activity w
JOIN pg_locks l1 ON w.procpid = l1.pid AND NOT l1.granted
JOIN pg_locks l2 ON l1.relation = l2.relation AND l2.granted
JOIN pg_stat_activity l on l2.pid = l.procpid
JOIN pg_stat_user_tables t ON l1.relation = t.relid
WHERE w.waiting;

-- cancel a query
postgres=# SELECT pg_cancel_backend(some_processid);
-- killing a session
postgres=# SELECT pg_terminate_backend(some_processid);
-- killing "idle in transaction"(e.g. leaving without ending the transaction) sessions
-- (ps, you can schedule this script to be running every minute)
postgres=# SELECT pg_terminate_backend(procpid)
FROM pg_stat_activity
WHERE current_query = '<IDLE> in transaction'
	and current_timestamp - query_start > '10 min';

-- collecting daily usage statistics
postgres=# CREATE TABLE backup_stat_user_tables as 
SELECT current_timestamp as snaptime,
FROM pg_stat_user_tables;
postgres=# INSERT INTO backup_stat_user_tablese
SELECT 

```

### 3. Schema and Table 

```psql
-- Show definition of a table(including References to this table)
postgres=# \d+ some_table
```

(to be continue)
