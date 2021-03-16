# Setup SSH Identity Key Login in Linux

- date: 2014-01-08 15:40
- tags: linux, shell
- category: tricks

----------------------------

This example is about how to create a new user and enable SSH public-key authentication in Ubuntu Server. It is necessary if your server is open to the public on internet.

## 1. Create a New User on Server
In a traditional way, people use the command "useradd" to create user account, then together with other commands to setup the group, the home folder for the user.

```bash
$ useradd terry
$ passwd terry
$ mkdir /home/terry
$ chown -R terry:users /home/terry
```
In a debian way, there is one command which does it all: "adduser".

```bash
$ adduser edmund
Adding user 'edmund' ...
Adding new group 'edmund' (1001) ...
Adding new user 'edmund' (1001) with group 'edmund' ...
Creating home directory '/home/edmund' ...
Copying files from '/etc/skel' ...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for edmund
Enter the new value, or press ENTER for the default
	Full Name []: 
	Room Number []: 
	Work Phone []: 
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] 
```

## 2. Generate SSH Key and Apply to Server
With SSH key login, user require a public/private key pairs to authenticate the login. SSH can use both "RSA" and "DSA" keys, however according to the [ubuntu guide](https://help.ubuntu.com/community/SSH/OpenSSH/Keys#Key-Based_SSH_Logins), "RSA" is the only recommended choice for new keys. 

First thing you should keep in mind, the private key should **NOT** allow to be accessed by anybody else(e.g. set "700" with chmod). We will create the RSA keys in your **local** machine, then copy the public key to the **remote** server.

```bash
$ mkdir ~/.ssh
$ chmod 700 ~/.ssh		# set access right only to user self
$ ssh-keygen -t rsa 	# **or you could use "ssh-keygen -t rsa -b 4096" for more secure login, default is 2048**.
Generating public/private rsa key pair.
Enter file in which to save the key (/home/edmund/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/edmund/.ssh/id_rsa.
Your public key has been saved in /home/edmund/.ssh/id_rsa.pub.

# next copy the public key to server. you can use a one-command way or manually copy the key to server.
$ ssh-copy-id user@machine		# one-command way
# manually way: copy the public key to server, and add it to authorized_key
$ scp ~/.ssh/id_rsa.pub user@machine:~/.ssh/my_rsa.pub
$ ssh user@machine
$ cd ~/.ssh
$ cat my_rsa.pub >> authorized_keys
```

## 3. Update SSH Daemon configuration on Server
On the remote machine, currently the password authentication is still enabled, so we need to enable the RSA Authentication and disable the Password Authentication for the better security.

Open **/etc/ssh/sshd_config** on server, find(or add) the below items and set the values:
```
PubkeyAuthentication yes
RSAAuthentication yes
PasswordAuthentication no
```
Next restart ssh service: ``` $ sudo service ssh restart ```
Now try login in the local machine:
```
$ ssh user@machine 	# Or,
$ ssh -i id_rsa user@machine
```
If your key matches, you will directly go into the console shell, or else you will get the following error info, which means you configuration applied successfully.
```
Permission denied (publickey).
```
If you want to revoke an authorized key for some user, you can find the user's public key in **"~/.ssh/authorized_keys"** and remove it.


------------------------

#### _Extra Bonus: below is a small trick to use the keys to encrypt/decrypt text for daily use._

```bash
# encrypt a text file, and output to a file
$ openssl enc -aes-256-cbc -e -in textfile.txt -out encrypted.txt -pass pass:some_password
# decrypt a text file, and output to a file(else it will print to the console)
$ openssl enc -aes-256-cbc -d -in encrypted.txt -out textfile.txt -pass pass:some_password

# encode in base64 (the "enc" option let you specify a cipher, e.g. "-base64" here)
$ openssl enc -base64 -e -in tetfile.txt
$ openssl enc -base64 -e <<< "Encode this text please"
$ openssl base64 -e <<< "Encode this text please"
# decode in base64
$ openssl base64 -d <<< "RW5jb2RlIHRoaXMgdGV4dCBwbGVhc2UK" 
```
