# Linux Server Security Useful Commands

- date: 2015-06-27 22:31
- tags: server, security
- category: tricks

---------------------------------

When suspecting your server is broken into, below is some tricks to do the server audit.

### 1. Use "last" command to check login sessions

```bash

$ last
terryoy  pts/0        58.251.197.153   Sat Jun 27 21:42   still logged in   
terryoy  pts/2        113.116.1.68     Tue Jun 23 14:40 - 16:14  (01:34)    
terryoy  pts/0        113.116.1.68     Tue Jun 23 14:38 - 16:14  (01:35)    
terryoy  pts/0        183.16.85.159    Tue Jun 23 09:37 - 14:02  (04:24)    
terryoy  pts/0        183.16.197.223   Mon Jun 22 17:47 - 20:10  (02:22)    
terryoy  pts/6        183.16.195.96    Thu Jun 18 11:08 - 15:23  (04:14)    
terryoy  pts/5        183.16.195.96    Thu Jun 18 11:08 - 15:23  (04:14)    
terryoy  pts/2        183.16.190.37    Thu Jun 18 10:37 - 13:06  (02:29)    
terryoy  pts/0        183.16.190.37    Thu Jun 18 10:01 - 13:01  (02:59)    

```

### 2. Use "lastlog" to check all user's last login time

```bash

$ lastlog
Username         Port     From             Latest
root             pts/2    27.45.56.68      Sat Feb 21 15:21:40 +0800 2015
daemon                                     **Never logged in**
bin                                        **Never logged in**
sys                                        **Never logged in**
sync                                       **Never logged in**
games                                      **Never logged in**
man                                        **Never logged in**
lp                                         **Never logged in**
mail                                       **Never logged in**
news                                       **Never logged in**
uucp                                       **Never logged in**
proxy                                      **Never logged in**

```

### 3. Check "/var/log/auth.log"

```bash

$ sudo less /var/log/auth.log
...
Jun 27 21:35:01 iZ940ou5p7nZ CRON[14089]: pam_unix(cron:session): session closed for user root
Jun 27 21:42:55 iZ940ou5p7nZ sshd[14108]: Accepted password for terryoy from 58.251.197.153 port 62430 ssh2
Jun 27 21:42:55 iZ940ou5p7nZ sshd[14108]: pam_unix(sshd:session): session opened for user terryoy by (uid=0)
Jun 27 21:45:01 iZ940ou5p7nZ CRON[14187]: pam_unix(cron:session): session opened for user root by (uid=0)
Jun 27 21:45:01 iZ940ou5p7nZ CRON[14187]: pam_unix(cron:session): session closed for user root
Jun 27 21:53:30 iZ940ou5p7nZ sudo:  terryoy : TTY=pts/0 ; PWD=/home/terryoy ; USER=root ; COMMAND=/usr/bin/apt-get install acct
Jun 27 21:53:30 iZ940ou5p7nZ sudo: pam_unix(sudo:session): session opened for user root by terryoy(uid=0)
Jun 27 21:53:39 iZ940ou5p7nZ sudo: pam_unix(sudo:session): session closed for user root
...

```

### 4. Use "acct" for system accounting

The "acct" package is a set of utilities for system accounting. 

    * ac, print stats about user's connect time
    * accton, turn process accounting on or off
    * last, listing of last logged in users
    * lastcomm, print info about previous executed commands
    * sa, summarize accounting info
    * dump-utmp, print an utmp file in human readable format
    * dump-acct, print an acct file in human readable format

```bash

# list user's login session time by date
$ ac -p -d

# display user's last commands
$ lastcomm <user_name>

```


### Reference to secure ubuntu server

https://www.ftmon.org/blog/secure-ubuntu-server/


