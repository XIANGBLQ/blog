# Put Linux into Old PC - (1) Installation and Hardware

- date: 2016-05-15 21:04
- tags: linux, study
- category: guides
-----------------------------

### 0. How this series begin?

I bought from Taobao a used Japanese IBM G40 PC, which has Pentium 4 (2.5GHz) processor, 512MB RAM and a 140GB hard disk (I believe the hardware spec has been changed by the used PC seller). Since the power consumption and the speed are not suitable for very modern applications, I decided to use it as an experiment machine for creating a minimal linux workspace. This series of blog posts will be the progress showing how I work on this machine to make it very friendly and efficient for daily used.

### Part 1. System Setup

I started to boot with the Ubuntu 16.04 LTS server image(flashed on a USB stick), the booting is a bit strange than previous versions, it shows a "boot:" prompt which need you to tells what to boot, but it's not difficult to find out how to boot into the installation mode.

The reason using Ubuntu latest version is because I want to keep up with the development of the software packages, Debian is in a very stable status, while the Ubuntu packages are active enough to try out new things. I format the whole disk and install Ubuntu on it. This is the starting point.

#### 1.1 Problem 1: hibernation on lid close

I'm so exciting at the moment when I finish all the installation and reboot, because I finally get this project started! But the first problem come very quickly - **when I try to lower the lid, the screen just go dark, and when I reopen it, the going hibernate process sticks in every few seconds**. I think there is some problem with the led sensor, because it automatically goes into hibernate a few seconds later when I activate again. So I think it is related to the power options in system settings.

This problem leads me to know about the **"systemd"** program. Searching solutions on the internet, I find out the settings in systemd will handle the power related key event. It sets how system react when user press Power key, Hibernate Key, Lid close/open, etc.

```bash
$ sudo vi /etc/systemd/logind.conf
# --in the file, change below line
#HandleLidSwitch=suspend
# --to
HandleLidSwitch=ignore

$ sudo service systemd-logind restart

```

This helps me to get over the hibernation problem at once. **Systemd** is a Linux system and service manager. There is similar programs like ubuntu's "upstart", or Mac OS's "launchd". You can search for more info about it. **The man page of systemd(init) is definitely worth reading to understand the first process of the system.**

There are two other power related packages ```acpi``` and ```acpid```. The Ubuntu document recommends that you can remove the packages if you do not have a laptop. Might read that later.

#### 1.2 Problem 2: Japanese keyboard layout
 
Although I set some Japanese keyboard layout in the installation, but it doesn't match all the keys with my Japanese IBM G40 keyboard. Apparently I need to switch the keyboard layout and do a few tests. The configuration program I used here is ```dpkg-reconfigure```, which allows you to configure a package again after they're installed. The package will be "keyboard-configuration".

```bash
# choose a different keyboard mapping
$ sudo dpkg-reconfigure keyboard-configuration
```

The above one already solved the problem. I changed the keyboard model to IBM ThinkPad T60/R60/T61/R61, then it says the layout of this keyboard varies in different country, so I'm able to choose the "Japanese" as the country of the origin layout. 

Some threads mentioned about the ```console-setup``` as I found out it is mainly for the encoding and the font set in the console, it might be related to the problem but not at this point. I may referred back if I try to work with Chinese character in the console.

```bash
# This change some console character set options
$ sudo dpkg-reconfigure console-setup
```
A little more on dpkg-reconfigure, if you use ```man dpkg-recongure``` to check its manual, you will find another related command called ```debconf-show```. It shows you all the current configurations of the package. So before you go with "dpkg-reconfigure", you can check the configuration first.

```bash
$ sudo debconf-show keyboard-configuration
```
It shows how many configuration items of the package and their values. Check out the man page for "keyboard-configuration", "console-setup", "dpkg-reconfigure" and "debconf-show" to explore more.

#### 1.3 Remapping the unused keys

The Japanese keyboard on my laptop doesn't have a Win(or Super) key, but have some abandoned key for old Japanese input. So I kind of like to remap the key to be more useful, such as using one as Super key.

Reference for **key remapping**: <http://askubuntu.com/questions/24916/how-do-i-remap-certain-keys-or-devices>

#### 1.4 Problem 3: WiFi Connection

The original G40 doesn't have wireless network connection. Fortunately I have a spare USB wifi adapter, but I need to configure the WiFi manually via command line. The adapter I used is Ralink RT5370, which is already supported in the kernel, so I don't need to explicitly install a driver for it.

First I could use ```lsusb``` to check that device is recognized. Then I move on to updating the configuration in ```/etc/network/interfaces```. Check out the man page of **interfaces**, and you will find the information of the keywords and syntax for configuring the network interface. For example:

*	*auto*, telling ```ifup``` to get this interface up automatically
*	*iface*, define an interface (template) using different methods(inet, inet6, etc.)
*	*allow-\*, allow the interface to be brought up by various sub-system(e.g. allow-hotplug, allow-auto, etc.)
*	*pre-up*, *post-down*, commands to be execute before the interface is up or after it is down

	
The configuration syntax is not difficult, so I added the below lines to enable the wifi adapter at system startup:

```
auto wlan0
iface wlan0 inet dhcp
iface wlan0 inet6 auto
```

Next I discover that my WiFi adapter is not called "wlan0"(you can check that by command ```iwconfig```). Instead, it is called "wlx5c63bf2a8b28", no wonder why I cannot bring it up when execute ifup. So now I need to change the name for it to make it more readable using **udev**. udev is responsible for which device gets which name. By the Systemd v197 standard of "Predictable Network Interface Names", interfaces are prefixed with "en" for ethernet, "wl" for WLAN, and "WW" for WWAN. 

```bash
# you check the interface entires list first, and fine the MAC address we'll need in udev
$ ip link
# (or alternatively for wireless interfaces)
$ iw dev

# update udev configuration
$ sudo vi /etc/udev/rules.d/10-network.rules
# add below line and save
SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="5c:63:bf:2a:8b:28", NAME="wlan0"

```

The **udev** program is a dynamic device management software, it supplies the system softwares with device events, manage permissions of device nodes and may create additional symlinks in the "/dev" directory, or provide names to unpredictable device names from the kernel. The man page for ```udev``` is worth reading.

Reboot to test out if the device is named correctly. The device can be found in ```/sys/class/net/```, with a symbolic link to the device's DEVPATH.

Next step is to setup the WPA2 authentication of the WiFi with my SSID and password. We'll need ```wpasupplicant``` package for that.

```bash
$ sudo apt-get install wpasupplicant
$ sudo vi /etc/wpa_supplicant/example.conf
# add the following contents:
#	ctrl_interface=/run/wpa_supplicant
#	update_config=1
$ sudo wpa_passphrase <SSID> <password> >> /etc/wpa_supplicant/example.conf

# to test the configuration: 1. start wpa_supplicant in the background, 2. use wpa_cli to interactive with the interface
$ wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/example.conf
# (or alternatively, add "-B" parameter to the wpa_supplicant command to make it run as a daemon in the background, then use "wpa_cli" to work interactively)
$ wpa_cli
>scan
>scan_results
# now you see the hotspot scan result, which means the configuration work

# Go back to our network interface setup, we will add wpa_supplicant to it(the "-D" is to specify the driver to use)
$ sudo vi /etc/network/interfaces
auto wlan0
iface wlan0 inet dhcp
  pre-up wpa_supplicant -B -Dwext -i wlan0 -c /etc/wpa_supplicant/example.conf
# save and test the interface
# (PS, sometimes I forgot the "-B" parameter in the wpa_supplicant command, it will make the ifup job hang because it will run as a daemon in the foreground.)
$ sudo ifdown wlan0
$ sudo ifup wlan0
# make sure the DHCP client can get an IP, otherwise the network auto start process in boot up might hang for 5 minutes to get the network...

```

Hard-coding the WiFi SSID and password in the configuration is not convenience in real environment, but so far in my experiement environment, it is OK to use it first. We will get back to the network manager later to make it more convenience to connect different WiFi network.

#### Problem 1.5 WiFi Connection Revisited

Last night I has successfully connect the wifi adapter to my home's network, howvever some new issues come up:

*	The bandwidth is only 1Mb/s
*	Not convenient to configure SSID and passphrase

After checking the [Debian's document](https://www.debian.org/doc/manuals/debian-reference/ch05.en.html), the network setup using *ifupdown* approach is a bit outdate, and the modern way is to use NetworkManager(NM) or Wicd(wicd and associated packages). 

(BTW, it is good to have the *debian-handbook* and *debian-reference* package installed in your local machine for any reference needed.)

At first, I try to look up a proper driver for the adapter. There is a package [rt2800usb](https://wiki.debian.org/rt2800usb) to support Ralink 802.11n usb devices on Linux. However, I found out that Ubuntu has already installed the ```linux-firmware``` which includes the rt28xx driver, so I decided to check it later.

Now I try to install the **network-manager** first. It is a program in two parts: a root daemon handling activation and configuration of network interfaces, and a user interface that controls it. It is provided by gnome project so the GUI is by default for gnome environment. However, it also provides a command line tool call ```nmcli``` in the package, so I will try it first.

```bash

$ sudo apt-get install network-manager
$ sudo service network-manager start
$ nmcli help

```

It will ignores the interfaces(except *lo*) in /etc/network/interfaces and use its own configuration, so comment out all leaving only *lo* in /etc/network/interfaces. Next. try a few commands for nmcli to check the network status.

```bash
# list network devices
$ nmcli device

# list connections
$ nmcli connection
```

now we can try to connect the wifi with the WiFi adapter

```bash
# list the wifi hot spots
$ nmcli device wifi list
# or refresh the list if you don't get it
$ nmcli device wifi rescan

# connect your hot spot
$ nmcli device wifi connect <SSID|BSSID> password <password>

```

It's as simple as just one command line, and yet so powerful than what I expected. The network manager auto saves the WiFi connection in its database, and it can also be activated automatically when system starts up. Save my day!

Reference for **nmcli**: [https://fedoraproject.org/wiki/Networking/CLI](https://fedoraproject.org/wiki/Networking/CLI)


After checking the connection, the bandwidth, everything goes well. So I can stop my researching for the network solution now. Next let's work on the desktop environment.

