# Learn to Use CMake to Compile Code
- date: 2018-01-12 14:41
- tags: linux, programming
- category: guides
------

I'm trying to use the Linux environment to develop C/C++ programs, but never really get on the path.

It's not the language that I don't understand, but the environment, the toolchain and how to configure a project in real life is my question. Linux have many programs developed in C/C++, but compiling them myself always out of my scope, which is blocking me from deeper understanding of Linux.

So here I'm reading a walkthrough to help myself making a C/C++ project work.

**CMake** is said to be an OS and compiler independent build system. So you first write CMake configurations in any source directories, and then it can generate a native build environment that will compile source code, create libraries, generate wrappers and build executables in arbitrary combinations.


### 0. Build Essential

First of all, if you want to compile anything in Linux, you should install the `build-essential` package first.

```bash
$ sudo apt install build-essential
```

It contains all the common packages to build Debian packages, such as: g++, gcc, hurd, libc, dpkg, make, etc.

Next step let's install the CMake package:

```bash
$ sudo apt install cmake
```

### 1. A Hello World and a CMakeLists.txt

The minimal demo has two files. 

A `hello.cpp` source file:

```cpp
#include <iostream>

using namespace std;

int main(void) {
     cout << "Hello World" << endl;
     return(0);
}

```

A `CMakeLists.txt` config file:

```
# Specify the minimum version for CMake

cmake_minimum_required(VERSION 2.8)

# Project's name
project(hello)

# Set the output folder where your program will be created
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})

# The following folder will be included
include_directories("${PROJECT_SOURCE_DIR}")

# Compile the program to hello
add_executable(hello ${PROJECT_SOURCE_DIR}/hello.cpp)

```

The three lines `cmake_minimum_required`, `project(hello)`, and `add_executable` are essential.

Run below two commands to compile the exectuatble:

```bash
# Generate CMake configurations
$ cmake -H. -Bbuild

# Build the executable
$ cmake --build build -- -j3

```


### References

[Learning CMake: A Beginner's Guide](https://tuannguyen68.gitbooks.io/learning-cmake-a-beginner-s-guide/content/chap1/chap1.html)
[CMake Official Tutorial](https://cmake.org/cmake-tutorial/)

