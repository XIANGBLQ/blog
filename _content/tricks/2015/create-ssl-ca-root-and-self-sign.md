# Create a Root CA and Self-Sign Certificate for SSL

- date: 2015-02-23 11:03
- tags: server, security
- category: tricks

----------------------------

### 1. Concepts

Nowadays we often have HTTPS protected web access scenario, however it's expensive to purchase a certificates from authority if you're just running a small site. So it's better to create your own certificates and use your own SSL protection.

The steps can be roughly described as below:

    1. Create a private key (as Root CA Key), keep this very private
    2. Self-sign a root certificate
    3. Install root CA on your various workstations
    4. Create a CSR(Certificate Signing Request) for each of your authorized needed circumstances(device, server, client, etc.)
    5. Sign CA with root CA Key


### 2. Generate Root CA(Certificate Authority)

The first part is to create a private key and the CA, which will be used as the root CA to sign certificates.

```bash

## Step 1: Create a private key

# generate a private root key
$ openssl genrsa -out rootCA.key 2048
# (or) generate a private root key with passphrase protection; and if you forgot the password, you need to do everything again
$ openssl genrsa -out rootCA.key 2048 -des3


## Step 2: Self-sign a certificate

$ openssl req -x509 -new -nodes -key rootCA.key -days 3650 -out rootCA.pem
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CN
State or Province Name (full name) [Some-State]:Guangdong
Locality Name (eg, city) []:Shenzhen
Organization Name (eg, company) [Internet Widgits Pty Ltd]:TeaTime Production.
Organizational Unit Name (eg, section) []:IT   
Common Name (e.g. server FQDN or YOUR name) []:Terry Ouyang    
Email Address []:terry.ouyang@gmail.com

```

Now we have a private root key(rootCA.key), and a root CA(rootCA.pem). If you want all the clients/PC/browsers accept your authorized certificate, you need to put your root CA in their local trusted stores(e.g. OS's trusted certificates repositories).


### 3. Create Certificates and Sign with Root CA

For every device you want to authorize, you need to create their own private key, then complete the signed certificate with a certificate signing request(CSR).

```bash

## Step 1: Create the private key

$ openssl genrsa -out device.key 2048

## Step 2: Create the CSR (In this step you must set "Common Name" to your desire host if you're planning to use it as a server's certificate)

$ openssl req -new -key device.key -out device.csr
...
Common Name (e.g. server FQDN or YOUR name) []:terryoy.github.io
...

## Step 3: Create the signed certificate 

$ openssl x509 -req -in device.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out device.crt -days 3650

```

Now you have the certificate private key(device.key) and the self CA signed certificate(device.crt). You can now use them for SSL communications.


### 4. Congifuration for Nginx

Below is an example of enabling the SSL function for the service configuration.
 
```bash

server {
    listen 443;
    ssl on;
    ssl_certificate /etc/nginx/ssl/service.crt;
    ssl_certificate_key /etc/nginx/ssl/service.key;

    ...
}

```

You can also check your server's certificate by the command below:

```bash
$ openssl s_client -connect www.yourexample.com:443
```

### 5. Setup SSL Factory on Android App

There is a good reference on [stackoverflow.com](http://stackoverflow.com/a/6378872) for this problem.

If you're using cocos2d-x 3.3+, it supports that you set a certificate for the HttpClient(globally), which allows you use your own certificate for SSL verification.

```cpp

auto path = FileUtils::getInstance()->fullPathForFilename("my_cacert.pem");
HttpClient::getInstance()->setSSLVerification(path);

```

### 6. ACME Client

_Update@2017: now you can use ACME clients and some free certificate service for personal HTTPS web sites._

AMCE is short for Automatic Certificate Management Environment, which requires you to run a client on your server to provide checking of the ownership of your server and domain name, and provide signed certificates based on the result.

Check out more information for the Free SSL/TLS Certificates: <https://letsencrypt.org>


