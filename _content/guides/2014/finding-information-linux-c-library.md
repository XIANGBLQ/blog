# Finding Information for C/C++ Library on Linux

- date: 2014-10-30 09:38
- tags: linux, programming
- category: guides

------------------------------

Developing on Linux often needs shared libraries most of the time. Below is a few references for finding the information about the libraries you are dealing with.

### 1. Naming Convention

All C standard libraries on linux has the name convention _"lib**xxx**"_. If you search packages of a library, you can use the (debian) command below to look for it:

```bash
$ apt-cache search libxxx
```

### 2. Library Packages

Usually, there are three packages of a library you could deal with. 

 * libxxx - this is the binary package of the shared library, usually has a "lib<name>.so.<version>" file on the path /usr/lib/ or /usr/local/lib. It is also needed at runtime.
 * libxxx-dev - this is the package which enables you to compile and link the library.
 * libxxx-dbg - this is the package which contains the debug symbols for debugging the program. where the files are usually installed at "/usr/lib/debug/".

If you want to know what files are installed on you system of a package, below are a few commands to do so:

```bash
$ dpkg-query -L <package_name>
$ dpkg-query -c <.deb_file>

# if you want to check files without installing the package
# use the apt-file program(it will cache the file lists of all packages)
$ apt-file update
$ apt-file list <package_name>

```

### 3. List Libraries on Your System

Below command can list all the share libraries and their locations, so you could whether a libray is installed and registered on which path.

```bash
$ ldconfig -p

# find a library(SDL) for example
$ ldconfig -p | grep -i sdl
```

For the ```ld``` program, it searches "/usr/lib/" for libraries by default, but it also include the paths defined in "/etc/ld.so.conf" and "/etc/ld.so.conf.d/".


### 4. Checking The Information of Library Files

A library usually contains two parts: static(.a) and shared(.so). You can check the both parts with the commands below:

```bash
# listing object files in static (archive) library
$ ar tf /usr/lib/i386-linux-gnu/libSDL2.a
SDL.o
SDL_assert.o
SDL_error.o
SDL_hints.o
SDL_log.o
...

# listing symbols in object files(.o), archive library(.a), and shared library(.so)
$ nm object.o
$ nm lib.a
$ nm -D lib.so 
$ nm --dynamic lib.so

```

### 5. Development Reference

Usually the "-dev" package contains some documentation or example files under path "/usr/share/doc/lib<name>-dev/". It is very useful to checkout these materials locally. For examples:

```bash
# open the documentation home page(xdg-open is a general command to open file, you can replace it with "iceaweasel" etc.)
$ xdg-open /usr/share/doc/libusb-dev/html/index.html

# extract the examples 
$ tar -zxvf /usr/share/doc/libsdl2-dev/examples/examples.tar.gz

```

### 6. More Information

Static, Shared Dynamic and Loadable Linux Libraries <br/>
[http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html](http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html)<br/>
Program Library HOWTO <br/>
[http://tldp.org/HOWTO/Program-Library-HOWTO/index.html](http://tldp.org/HOWTO/Program-Library-HOWTO/index.html)



