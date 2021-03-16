# How I fix my Ubuntu with iRST(Intel Rapid Start Technology) Raid

- date: 2016-12-29 00:05
- tags: linux
- category: tricks

-------------------

I have bought a Haier X3 laptop with a 500GB hard disk and a 32GB SSD with which you could use to boot and cache disk rapidly for Windows via Intel's technology. However, I'm a Linux fan, so I also need to install Ubuntu on my computer.

At first, the Windows 7 system was pre-installed. When I installed Ubuntu it failed at booting if the Windows 7 had enabled iRST. I cannot find any working solution to fix the Ubuntu problem at the time, so I just disabled Win 7's iRST, and then use the SSD as normal disk. Later I had a very good time with the Linux environment.

Recently, I'm going to refresh the whole system and make both clean again. So I give a second try to enable Windows 7's iRST and make Ubuntu boot correctly, and I succeeded after two days hard work!

The root cause is that the raid management tool on Linux will assemble the partitions as RAID and then the `initramds` cannot find the partition with UUID. It fails like this:

```sh

Gave up waiting for root device. Common problems:
 - Boot args (cat /proc/cmdline)
   - Check rootdelay= (did the system wait long enough?)
   - Check root= (did the system wait for the right device?)
 - Missing modules (cat /proc/modules; ls /dev)
ALERT! /dev/disk/by-uuid/52152d36-9dc4-42a6-8be1-3966bf397b09 does not exist. Dropping to a shell!

BusyBox v1.22.1 (Ubuntu 1:1.22.0-15ubuntu1) built-in shell (ash)
Enter 'help' for a lost of built-in commands.
(initramfs)

```

I have searched on the internet about it, finding that it's related to the block id that generated for the partitions are missing:

```sh
(initramfs) blkid
/dev/sda: TYPE="isw_raid_member"
/dev/sdb: TYPE="isw_raid_member"

(initramfs) ls /dev/md*
md/  md126  md127

```

While the partitions of `/dev/sda/` are supposed to be recognized by UUIDs, but it is created as a software RAID device(md126), so the partitions of it cannot be accessed at boot time. I have tried to install Ubuntu via my usb disk again and again, also try to use `chroot` to update the grub record and the initramfs on the partiion, and I still don't have luck. After a long frustrating period, I suddenly come up the idea: why not just disable the raid array at boot time? 

After I tried the below two commands in `initramfs`, it come back to normal boot after I exit the initramfs mode!

```sh

(initramfs) mdadm --stop --scan

(initramfs) blockdev --rereadpt /dev/sda

```

The first command scan all the RAID array entries and close them. The second command re-read the partitions with UUIDs so you get the UUID entries for initramfs to boot.

This time I have confident to make the solution permanent. First of all, I will need to use my Ubuntu usb boot disk to enter the shell('Go Back' in the first step of the installation, then you find a choice for executing a shell) and mount the partition. (My target Ubuntu parition is /dev/sda3)

```sh
$ mount /dev/sda3 /mnt
$ mount -t proc /proc /mnt/proc
$ mount -t sysfs /sys /mnt/sys
$ mount -o bind /dev /mnt/dev
$ chroot /mnt /bin/bash
```

This allow me to mount the partition just as I've booted into it. Then I will update it's boot process(e.g. grub & initramfs).

```sh
$ grub-install /dev/sda
$ update-grub

$ vi /etc/initramfs-tools/script/local-top/mdadm
mdadm --stop --scan
blockdev --rereadpt /dev/sda

$ chmod +x /etc/initramfs-tools/script/local-top/mdadm
$ update-initramfs -u

```

Voilà! My Ubuntu's back!...wait, my Windows 7 has gone! It seems that GRUB has erase my Windows 7 boot entry. This doesn't stop me now. It's easy to get Windows back.

I tried to run `update-grub` again, but it doesn't recognize the Windows boot entry even though os-prober is enabled. So I need to add it manually:

```sh
# check the Windows partition UUID
$ blkid

$ vi /boot/grub/grub.cfg
# (look for the section of "/etc/grub.d/40_custom" and add the content below)
menuentry "Windows 7" {
    insmod ntfs
    set root='(hd0,1)'
    search --no-floppy --fs-uuid --set 76B0EE43B0EE0987
    chainloader +1
}

```

Then reboot. It is finally OK.


