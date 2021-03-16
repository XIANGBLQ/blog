# VirtualBox Command Line Tricks

- date: 2016-02-17 11:01
- tags: shell, virtualbox
- category: tricks

----------------------------

Sometimes we need to work with VirtualBox's command line tools to make things done. Here are a collections of tasks I encountered.

### 1. Converting an Linux .img format to a .vdi (VirtualBox disk)

```bash
$ VBoxManage convertfromraw mydisk.img mydisk.vdi --format vdi
```

### 2. Mount virtual disk on your ubuntu system

In linux, we can use a the ```qemu-nbd``` and ```kpartx``` to mount a .vdi file on a path. The *qemu-nbd* tool can create a block device to enable it to be share via NBD(Network Block Device) protocol. Then, we will use ```kpartx``` to create device maps from the partition tables of the device, which makes the partition of the image mountable.

```bash
# (prerequisites] install the dependencies
$ sudo apt-get install qemu-utils kpartx

# to mount the device
$ sudo modprobe -nbd
$ sudo qemu-nbd -c /dev/nbd0 <vdi_file>
$ sudo kpartx -a /dev/nbd0
$ sudo mount /dev/mapper/nbd0p1 /mnt/<mount_point>

# delete the device when no longer needed
$ sudo umount /mnt/<mount_point>
$ sudo qemu-nbd -d /dev/nbd0


```


(...to be continued)
