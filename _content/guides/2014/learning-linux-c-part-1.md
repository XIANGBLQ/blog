# Linux C Learning (Part 1)

- date: 2014-08-20 23:34
- tags: linux, programming
- category: guides

------------------------------

Below is some study notes for Linux C Programming from a web course. It can serve as a coding reference in the future, or a walkthrough summary of the study. As I already have the knowledge of C Programming Language, so I will not cover the language detail here, but only the development environment under Linux.

### 1. **gcc** and **gdb**

There are several steps for the **gcc** compiler to compile a source file into a executable program. It can be set to the step output with some parameter to gcc, so you can checkout their result in file.

```bash

# Preprocessor: This is to remove comments, replace marcos(#define), and headers(#include)
$ gcc -E test.c -o test.i

# (+)Compile: This compile the source code into assembly code. Different architecture has different assembly language spec
$ gcc -S test.c -o test.s

# (+)Assemble: this translate assembly code into binary object. You can check the file with "file test.o" to see the format as a "object file" or a "ELF LSB relocatable", and the architecture of the platform(x64, etc.)
$ gcc -c test.c -o test.o

# (+)Link: This generate the final executable
$ gcc test.c -o test

```

There are other useful parameters of gcc for specific purpose, for example, optimization, or debugging.

* "-O[level]", optimzation level, (0,1,2,3)
* "-g", generate debug info, gdb needed
* "-Wall", enable all warnings and errors
* "-Werror", enable errors
* "-D", define macro in command line
* "-I", set the location of headers
* "-std=C99", use C99 standard

The **gdb** debugging tool can be used to trace the program with some useful commands:

- "l", list source code with line numbers
- "n", proceed next line
- "b [line number]", set a breakpoint at the code with the line number
- "c", continue running until finish or meets the next break point
- "p [variable]", print the instant value of a variable






