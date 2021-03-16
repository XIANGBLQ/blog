# Python Main Args, Config, and Exception Snippets

- date: 2013-12-21 15:35
- tags: python
- category: tricks

-------------------

Part 1. Below is an example showing how to use **arguments** in a python script. It's taken from this [example](http://www.tutorialspoint.com/python/python_command_line_arguments.htm).

```python
#!/usr/bin/python

import sys, getopt

def print_usage():
    print 'main.py -i <input_file> -o <output_file>'

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        # opts is a list of returning key-value pairs, args is the options left after striped
        # the short options 'hi:o:', if an option requires an input, it should be followed by a ":"
        # the long options 'ifile=' is an option that requires an input, followed by a "="
        opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    # print(args) # debug line
    if not opts:
        print_usage()
        sys.exit(2)

    # print arguments
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print "Input file:", inputfile
    print "Output file:", outputfile


if __name__ == "__main__":
    main(sys.argv[1:])
```

Below is the example running result:

```
$ ./main.py -h
main.py -i <input_file> -o <output_file>
$ ./main.py
main.py -i <input_file> -o <output_file>
$ ./main.py -i inputfile
Input file: inputfile
Output file: 
$ ./main.py -i inputfile --ofile=outputfile
Input file: inputfile
Output file: outputfile
```

Part 2. Below is an example showing how to use **configuration** and **exceptions**.

```python
#!/usr/bin/python

from ConfigParser import ConfigParser, NoOptionError
import traceback

## The configuration is a file named "config.ini" with below content
# [helloworld]
# name = Terry
##

# read configuration
config = ConfigParser()
config.read('config.ini')

# use configuration
print 'an existing item value:', '[ name =', config.get('helloworld', 'name'), ']'
try:
    print 'an non-existing item value:', '[ non-exist =', config.get('helloworld', 'non-exist'), ']'
except NoOptionError:
    # pass
    traceback.print_exc() # display exception information
```

Here is the output result:

```
an existing item value: [ name = Terry ]
Traceback (most recent call last):
  File "./config_parser.py", line 12, in <module>
    print 'an non-existing item value:', '[ non-exist =', config.get('helloworld', 'non-exist'), ']'
  File "/usr/lib/python2.7/ConfigParser.py", line 618, in get
    raise NoOptionError(option, section)
NoOptionError: No option 'non-exist' in section: 'helloworld'
an non-existing item value: [ non-exist =
```

As you can see the line _"an non-existing item value: [ non-exist = "_ is output belowthe exception trace information. It is because the traceback.print_exc() output to **stderr** while the others output to **stdout**, they're two separate buffers and no particular order when output to console.









