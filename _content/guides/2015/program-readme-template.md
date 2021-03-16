# A Template for Program Readme on Github

- date: 2015-06-03 16:15
- tags: programming
- category: guides
------------------------------

When writing a Program, the developer should be clear about the purpose, to eliminate time wasted. Refering to the [How to Program](http://textfiles.com/programming/writprog.pro), I propose a documatation template companied with a Software Development Life Cycle to ensure this.

    1. SPECIFICATION
    2. PROGRAM DESIGN
    3. CODE DESIGN
    4. CONSTRUCTION AND DESIGN

So, starting a project on github, I think we should follow a basic documentation structure to answer each questions, to ensure that your purpose is clear enough.

### 1. Speficication

In this stage, four things matter.

 * User Interface

    in what approach does user interact with the program?
    what input/output?
    command line? menus? how much freedom allowed?
    
 * Algorithm

    what specific computation behind the program?
    what method do we use?

 * Data Structures

    how should the data of the problem be organized?
    
 * [Generality]

    is it used only in a small number of situations? or is it general purpose of wide variety of circumstances?
    you need fewer choices if made for a small number of situations, and more choices and more commands for large number of situations

 * [Robustness]
    how gracefully does the program respond to bad data or bad commands?


### 2. Program Design

A design of the program may be often represented by a structure chart, but it's not the most important thing. Instead, you should divied the large program into **subroutines**.

 * Design Structure
    top level routines
        sub routines

There're a few ideas for evaluating the desgin:

    1. Keep subroutines short
    2. Keep subroutines single-purpose
    3. Keep calling sequence short
    4. Communicate data through calling sequences
    5. Limit use of flag variables
    6. Make design hierarchical

### [3. Setup and Testing]
### [4. About and License]

_(Since the original post discontinued, I have to complete the rest of the template myself.)_

Following is a template in markdown:

```

### 1. Specification

##### User Interface

##### Algorithms

##### Data Structures

##### [Generality]

##### [Robustness]

### 2. Program Design

##### Design Structure

##### Public Interface

### 3. Setup and Testing

### 4. About

### 5. License

```

