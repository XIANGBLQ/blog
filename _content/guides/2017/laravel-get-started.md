# Getting Laravel Started

- date: 2017-11-24 10:37
- categories: guides
- tags: php
-----

After I found that PHP7.1 is in-the-box with OSX, it motivates me to start learning PHP(a.k.a. "the best language in the world" :P) and give some try to small projects. What I got from my friend is that [Laravel](https://laravel.com/) is the quite popular web framework for PHP. So now I setting up the development and deployment environment to get started.

### 1.Installing dependencies

On my MBP desktop, it's recommended to use [Valet](https://laravel.com/docs/5.5/valet) if you want just a small additional tools to run it, and connect to existing databases on the machine. Otherwise it would be good to use a virtualbox image [Homestead](https://laravel.com/docs/5.5/homestead) to have an all-in-one setup for development.

While my Ubuntu 16 server, I would like to install dependencies by hand, so I could get familiar with what it takes to run Laravel. Now here's what I tried.

```bash

$ sudo apt install php7.0 php7.0-cli php7.0-zip php7.0-mbstring php7.0-mbstring php7.0-xml

```

Then we need to install [Composer](https://getcomposer.org) to install other php packages. It's like the `pip` to Python and the `npm` to NodeJS.

```bash

# install to $HOME/bin
$ cd ~
$ wget https://getcomposer.org/installer -o composer-setup.php
$ php composer-setup.php --install-dir=bin --filename=composer


# (alternatively) You could try the one-line command bellow for default installation
$ curl -s https://getcomposer.org/installer | php

```

Then try the composer command to see if you have it.

```bash

$ composer

```

### 2.Installing Laravel Valet

**Valet** is a lightweight solution for hosting Laravel in development, and only avaiable on OSX. It uses brew to install php7.1 and other dependencies, but first you need Composer to install Laravel Valet. So install the composer using the script above first.

After composer is installed, use it to download the Valet package.

```bash
$ composer global require laravel/valet

```

After composer install the package, you should note about where it is installed. Because you need to set the $PATH environment variables to enable the command from the packages. On OSX, the executable programs are in `~/.composer/vendor/bin`, and on Ubuntu, the path might be `~/.config/composer/vendor/bin`.

Then you can use valet commands to manage your development environment.

### 3.Install Laravel

Installing Laravel is similar to Valet. Use `composer` to download and install the package globally.

```bash
$ composer global require "laravel/installer"

```

Then you can use `laravel` command to create a new project:

```bash
$ laravel new myproject
```





