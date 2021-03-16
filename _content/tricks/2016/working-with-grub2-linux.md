# Working with Grub2 in Linux

- date: 2016-10-21 10:21
- tags: linux
- category: tricks

-------------------

**Grub2**(GRUB: the GRand Unified Bootloader) is the main bootloader in Debian/Ubuntu distribution. I have always wanted to know the details to change or fix the booting process. So I did a research and make a note here.

### 1. Overview

Normally we should use the util `update-grub` to update the grub2 boot entries. In grub(the older, not grub2), we need to update the boot menu file `/boot/grub/menu.lst` carefully to manage the entries. In this case, it could be easy to make mistakes, or inconvenient while editing the file and get required information at the same time. 

In grub2 with `update-grub`, this process can be managed in updating a general setting file and a list of scripts that generate entries. These files are:

 - `/etc/default/grub`, general grub settings,
 - `/etc/grub.d/*`, this directory contains a list of executable scripts and will be processed in order. You can add the files according to the convention:
   - "00_*": It is reserved for 00_header.
   - "10_*": Native boot entries.
   - "20_*": Third party apps (e.g. memtest86+).

The number namespace in-between is configuratble by system installer and/or administrator. The order of other number will be reflected in the menu if you set 01_otheros, 11_otheros, etc.

For example, I have below config files in `/etc/init.d/` for a ubuntu installation:

```
00_header
05_debian_theme
10_linux
20_linux_gen
30_os-prober
30_uefi_firmware
40_custom
41_custom
```


### 2. Clean up Grub2 Menu

After a release or a kernel upgrade, you may usually find unuseful entries in the boot menu, which are mainly for previous state recovery. So here let's see how to remove the unuseful entries.

First are the unnecessary kernel entries. They exist because you install more older kernel versions lying around on your machine. So you can check if there are more than one `linux-headers-<version>` entry and `linux-image-<version>` entry, then remove the unnecessary package via package manager.


Second, unwanted entries in `/etc/init.d/` such as memtest86+. Disabling them is very easy, just make them not executable then it's done.

```bash
$ cd /etc/init.d/
$ sudo chmod -x 20_memtest86+
```

And the last thing is to update grub:

```bash
$ sudo update-grub
```

Sometimes if you just want to edit some of the boot menu item, you could lookup the `menuentry` in the file and edit the content. For example, there is a `30_os-prober` file in `/etc/grub.d/`, which checks if there are other OS exists on local drives and create boot entries for them. You can see the similar content in each OS part and using `cat` and `menuentry` to add an entry to the grub config.


### 3. Grub2 Settings

In the general setting file `/etc/default/grub`, there are some basic settings that you could change.

```
# (template of /etc/default/grub)
# 1. Default boot entry, can be the index or the title of the boot item; SAVEDEFAULT option let you save every last choice as next default
GRUB_DEFAULT=0
GRUB_SAVEDEFAULT=true

# 2. Go directly to the default boot entry unless you press 'shift' or 'esc' at startup. The "QUIET" option will display the count down of the hidden timeout before going to boot, which you can use a chance for a boot splash
GRUB_HIDDEN_TIMEOUT=0
GRUB_HIDDEN_TIMEOUT_QUIET=true

# 3. Grub background, just simply set the image path(supports '.png', '.tga', '.jpg' or '.jpeg')
GRUB_BACKGROUND='/path/to/image.jpg'


```

Ref: (run as shell cmd) `info -f grub -s 'Simple configuration'`

### 4. Grub2 tools

#### 4.1 Grub Rescue

Many times when grub boot failed, it will run into `grub-rescue` shell environment. It is expected that you fix something(usually try to recover the damaged boot record.) and set a bootable entry for grub to continue the boot process

Below is an example of a common process.

```bash

# check available parition
grub rescue> ls
(hd0),(hd0,msdos3),(hd0,msdos2),(hd0,msdos1)

# check available grub boot record in a partition
grub rescue> ls (hd0,msdosX)/boot/grub

# set boot entry
grub rescue> set root=(hd0,msdos3)
grub rescue> set prefix=(hd0,msdos3)/boot/grub
grub rescue> insmod /boot/grub/normal.mod

# go to startup screen
grub rescue>normal

# (is this the alternative way?)
rescue>linux /boot/vmlinuz-xxx-xxx root=/dev/sdax
rescue>initrd /boot/initrd.img-xxx-xxx
rescue>boot


```


### Reference
========= 

The GRUB manual: (run in linux shell) `info grub`

Clean up Grub2 entries: <http://www.howtogeek.com/howto/17787/clean-up-the-new-ubuntu-grub2-boot-menu/>. (There is also a link to an article for the old `grub`)

How to Configure Grub2 boot loader settings: <http://www.howtogeek.com/196655/how-to-configure-the-grub2-boot-loaders-settings/>

