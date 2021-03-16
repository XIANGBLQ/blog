# Put Linux into Old PC - (3) Localize the Language Environment

- date: 2016-06-28 21:03
- tags: linux, study
- category: guides
-----------------------------

### Part 3. Localize the language environment

It is very easy to support the multi-language environment if you're installing the normal Linux desktop. However, it takes a few steps if you want to try the manual way. To make it more challenging, I would like to add Japanese support(the second foreign language I'm going to learn) together with Chinese support which is my mother language.

The job to enable this multi-language environment includes three parts:

 * Able to view the Asian characters,
 * Able to input the Asian characters,
 * The user interface are translated into the familiar language. (However, I might prefer an English environment just for working~)

#### 3.1 Enabling the Input Method

Now I want to enable the input method at first, because it enable me to try enter other characters. There are several approaches to support multi-language input method, such as ```SCIM```, ```ibus```, and ```uim```. The currently recommendation is **ibus**. There are several popular alternatives for both Japanese and Chinese input methods. `Anthy` and `mozc` are for Japanese, and `pinyin`, `sunpinyin` and `google-pinyin` are for Chinese(let's hope that Sogou Pinyin is joining this competition~). You can choose as you prefer, but I will first install only two basic choices.

```bash
# Install Anthy and Pinyin
$ sudo apt-get install ibus-anthy ibus-pinyin

# Setup the configurations for the first time (you may need to manually add the input method in the enabled list)
# (for input method config)
$ im-config
# (for ibus config)
$ ibus-setup


```

Be sure to change the method switching keyboard shortcuts to "Ctrl+Space", otherwise you may not correctly enable it(by default, it uses "Super+Space" to switch between but I have no "Super" key on my keyboard).

After all the steps above, the ibus input method is still not enabled at start up, which means you need to manually start the daemon by executing "ibus-setup". However, no doubt that I will fix this soon.

To enable things at X start up, you need to put commands in ```~/.xprofile``` or ```~/.xinitrc```, depends on the windows manager requirements. ```~/.xprofile``` is often used before windows manager start up, while ```~/.xinitrc``` is used by "initx" and its frontend "startx" to initialize the X window manager(remember we put "exec openbox-session" in this file previously?). The ```ibus-daemon``` program starts the ibus daemon server, so if I want to start ibus when X starts, I will put it in the ~/.xinitrc file. [[2]](#ref)

```bash
$ vi ~/.xinitrc
# (add at the end of the file)
ibus-daemon -drx
```

You can check out what the part of "-drx" means by ```man ibus-daemon```. It's easy.

#### 3.2 Testing the Input method

There are a lot of applications that supports input method. Two I have tried, the browser and the terminal. Not every termimal emulator supports ibus input. Luckily, I have chosen ```lxterminal``` and it does the job.

The first and easy test is on the browser. I changed the keyboard shortcut for "switching to next input method" to Ctrl+Space, because the default one is Super+Space but my `Super` key isn't available at the time and `Ctrl` is more like my preference. 

The Japanese font seems to be already available with the installation above, but the Chinese font isn't. So, by installing some extra Chinese fonts, you should be able to see most of the east asian characters.


```bash

# Chinese Font
$ sudo apt-get install fonts-wqy-microhei fonts-wqy-zenhei

```

The "Typing Method" in the Japanese input method is more like a switch from Pinyin to Wubi in Chinese. My Japanese keyboard has Hiragana characters written on the keys, so I can choose "Kana" as typing method(a little bit like Wubi, typing words in characters). If you choose "Romanji" as the typing method, then you should input the characters in a phonetic way.


#### 3.3 Localizing the UI

The English UI is good enough for me in the most circumstances. But still, I want to look into the details for changing the language of applicatoin interfaces.

##### Basic Locale Settings

The system variable "LANG=xx_YY.ZZZZ" has defined the language settings in three ways: `language code`, `country code`, and `encoding`. (Notice the upper cases and the lower cases.) This variable affects the language interface of most of the applications. To do an experiement, try to set the variable as below, before entering the X window environment. You will see the menu of applications are changed to a different font, but the language is possibly still in English. This is because the application has no Chinese locale interface installed.

```bash
$ export LANG=zh_CN.UTF-8
```



### Reference
<a name="ref"></a>
[1] Debian i18n: <https://www.debian.org/doc/manuals/debian-reference/ch08.en.html> <br/>
[2] IBus: <https://wiki.archlinux.org/index.php/IBus>

