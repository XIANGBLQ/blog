# Ubuntu Desktop Sharing to Mac OSX

- date: 2016-02-26 10:52
- tags: linux, osx
- category: tricks

----------------------------

I have a spare laptop rest in my house which I seldom use(I major use my macbook pro for work), but it's still good for developing projects and runs Linuxi Mint. So I want it to be available any time when I'm at home so I could use it to continue my side project works. With ssh and VNC, I can setup both the command line and desktop environment online so I don't need to open the laptop, but use my macbook to access the environment. Then I have the convenience that the laptop can put anywhere in the house and clear my desktop.

I found [this post](http://www.fiz-ix.com/2012/12/ubuntu-to-mac-os-x-screen-sharing-with-vinagre/) very useful to do the trick. It uses "vino" with easily setup steps, and you can get "Vinagre" VNC client on Linux ox,  but you need some notices about the access on OSX. So I write my process here.

### 1. Setup Vino(VNC for gnome)

Just reference the post. 

```bash

$ sudo apt-get vino
# the preferences is the same as "Desktop Sharing" preference panel in Linux Mint
$ vino-preferences

```

You can set up the items just as the post said in vino-preferences, but on Linux Mint it lacks out the "Advanced settings" mentioned in the post. So you need "dconf-editor" to manually set it.

```bash
$ sudo apt-get install dconf-editor
$ dconf-editor
```

Find the config item in dconf-editor with path **"desktop.gnome.remote-access"**. You need to uncheck the "require encryption" to support OSX, otherwise the authentication is unsupported on OSX.

### 2. Using Screen Sharing on Mac OSX

Turn on the "Spotlight" with keyboard shortcut ```cmd+K```, enter "screen sharing" and you can find the default desktop sharing client app on Mac OSX.

Type "vnc://your_server_ip:5900" and then you get the prompt to enter password for the access. That's it!

### 3. More

The post also talked about using the ```avahi``` service to broadcast the desktop sharing service to OSX. It is an advanced option to try, I will update it if I have tried.

