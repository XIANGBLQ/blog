# Intel Edison Get Started

- date: 2015-06-03 16:15
- tags: programming
- category: guides
------------------------------

This guide is about the initial steps for me starting development on Intel Edison platform.

### 1. The Board and Setting Up Serial Communication

The board I use to develop with Edison is the [Intel Edison for Arduino](http://www.seeedstudio.com/depot/Intel-Edison-for-Arduino-p-2149.html) board. So first plug the Edison module on the board; secondary, I have the 6.5V 2A DC connected to supply the power to the board (or you could power up the board with the micro-USB in the middle); third, a micro-USB wire connect to the board for serial communication.

I'm using minicom on Mac OSX for the serial connection, but you can also use ```screen``` on Mac OSX and Linux(see the reference at the end of this section).

If you forgot the root password, here's the way to recover it: 

    * on booting, press any key to stop the process
    * on the "boot>" command line prompt, type ```run do_ota``` to redo the flashing process. 

Then you end up with a login using "root" as user name and no password.

 * [Reference for assembling](https://software.intel.com/zh-cn/assembling-intel-edison-board-with-arduino-expansion-board)
 * [Reference for setting up serial on Linux](https://software.intel.com/zh-cn/setting-up-serial-terminal-on-system-with-linux)
 * [Reference for setting up serial on Mac](https://software.intel.com/zh-cn/setting-up-serial-terminal-on-system-with-mac-os-x)


### 2. Setting up WiFi

The next thing to do is to setup the WiFi on Edison, because a large part of the development process happens on WiFi.

```bash
$ configure_edison --wifi

# check the wifi status
$ wpa_cli status

```
Follow the instructions of this program to complete the scanning, choosing hotspot, and reboot with WiFi.

By default, ```ssh``` is restricted to usb, so you need to disable the restriction by using ```configure_edison --setup``` to setup the device name and password. It will automatically update the file '/lib/systemd/system/sshd.socket' and comment out this line "BindToDevice=usb0". (need reboot to take effect)



 * [Reference for setting up WiFi](https://software.intel.com/zh-cn/connecting-your-intel-edison-board-using-wifi)

### 3. Blink the LED

(to be continued when I get the board...)





