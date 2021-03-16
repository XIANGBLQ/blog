# Multiple Arguments in Python

- date: 2016-02-03 16:05
- tags: python
- category: tricks

----------------------------

This article tells about how to use variable number of arguments in Python functions.

### 1. Passing Multiple Arguments 

The meaning of "args" and "kwargs" we often used as the multiple arguments are "normal(unnamed) arguments" and "keyword(named) arguments". Try the below in python and you can see it's actually the difference of a tuple and a dictionary.

```python

>>>def play(*args, **kwargs):
	print(args)
	print(kwargs)

>>>play()
()
{}

```

You should use the order of specific arguments, unnamed arguments, and named arguments when defining a function:

```python
def arg_order(arg, *args, **kwargs):
```


### 2. How to pass arguments from one function to another

Below are a list of examples to show you the result of different methods of multiple arguments:

```python

>>> def a(*args):
...   print("unnamed: {0}".format(args))
... 
>>> a(1,2,3)
unnamed: (1, 2, 3)

>>> def b(**kwargs):
...   print("named: {0}".format(kwargs))
... 
>>> b(a=1)
named: {'a': 1}

>>> def c(arg, *args, **kwargs):
...   print("full:")
...   print(arg)
...   a(*args)
...   b(**kwargs)
... 
>>> def test(*args, **kwargs):
...   c(123, 456, 789, we="we", love="love", it="it")
... 
>>> test(4,5,6, we="we", love="love", it="it")
full:
123
unnamed: (4, 5, 6)
named: {'we': 'we', 'love': 'love', 'it': 'it'}

```

