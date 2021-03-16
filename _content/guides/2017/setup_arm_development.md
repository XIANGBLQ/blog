# Setup Arm Development Environment
- date: 2017-12-31 00:00:00
- tags: linux, misc
- category: guides

-----

### 1. Clone the kernel repository

```bash
$ git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

# or just download the package from the mirror
$ wget https://mirror.tuna.tsinghua.edu.cn/kernel/v4.x/linux-4.4.1.tar.xz
```


### 2. Install the Cross Compiling Toolchain 


```bash
$ sudo apt-get install gcc-arm-linux-gnueabi

# another option is "arm-linux-gnueabihf" but we use "gcc-arm-gnueabi" here
```

### 3. Make the first compile

We're emulating the vexpress Cortex A9 for demo.

```bash
$ export ARCH=arm  
$ export CROSS_COMPILE=arm-linux-gnueabi-  
$ make vexpress_defconfig  
$ make zImage -j8  
$ make modules -j8  
$ make dtbs 

```

### 4. Install QEMU

```bash
$ sudo apt-get install qemu
```

### 5. Make Root File System

### 5.1 busybox

```bash

$ wget http://www.busybox.net/downloads/busybox-1.25.1.tar.bz2  
$ tar xvf busybox-1.25.1.tar.bz2
$ make defconfig  
$ make CROSS_COMPILE=arm-linux-gnueabi-  
$ make install CROSS_COMPILE=arm-linux-gnueabi- 
```

Then you find the executables in `_install` folder. Next we start to create the rootfs.

### 5.2 rootfs


```bash
$ sudo mkdir rootfs
$ sudo mkdir rootfs/lib 
 
# copy busybox to rootfs
$ sudo cp _install/* -r rootfs/

# copy arm libs to lib
# sudo cp -P /usr/arm-linux-gnueabi/lib/* rootfs/lib/

```

### 5.3 Create 4 tty devices

```bash
$ sudo mkdir -p rootfs/dev
$ sudo mknod rootfs/dev/tty1 c 4 1  
$ sudo mknod rootfs/dev/tty2 c 4 2  
$ sudo mknod rootfs/dev/tty3 c 4 3  
$ sudo mknod rootfs/dev/tty4 c 4 4
```

You can also create other folders in the image. (Reference: <https://learningfromyoublog.wordpress.com/2016/04/05/131/>)


### 5.4 Make the Image

```bash
# creat an empty image
$ dd if=/dev/zero of=a9rootfs.ext3 bs=1M count=32  

# format to ext3
$ mkfs.ext3 a9rootfs.ext3  

# copy files into the image
$ sudo mkdir tmpfs  
$ sudo mount -t ext3 a9rootfs.ext3 tmpfs/ -o loop  
$ sudo cp -r rootfs/*  tmpfs/  
$ sudo umount tmpfs  

```

### 6. Start QEMU with the Image

```bash
# open in current console
$ qemu-system-arm -M vexpress-a9 -m 512M -dtb extra_folder/vexpress-v2p-ca9.dtb -kernel extra_folder/zImage -nographic -append "root=/dev/mmcblk0 rw console=ttyAMA0" -sd a9rootfs.ext3 

# open in new window(maybe GUI)
$ qemu-system-arm -M vexpress-a9 -m 512M -dtb extra_folder/vexpress-v2p-ca9.dtb -kernel extra_folder/zImage -append "root=/dev/mmcblk0 rw" -sd a9rootfs.ext3  

```

Now you enter the console of the emulator system. Press `Ctrl+A C` to exit to `(qemu)` console, or `Ctrl+A X` to exit..




