# Python Function Decorators and The Use in Django

- date: 2017-3-26 16:26
- tags: python
- category: tricks

---------

### 1. Basic of functions

 * Functions can be assign
 * Functions can be defined inside a function
 * Functions can be passed as a parameter and return as a returning value
 * Inner functions have access to the enclosing scope

```python
def foo(name='World'):
   print('Hello, {0}!'.format(name)))

# assign
bar = foo
bar()
# => Hello, world!


# Use in parameter and return as result
def greetings(call):
    welcome = 'Welcome back!' # the enclosing scope to "greeting_to"

    def greeting_to(name):
        call(name)
        print(welcome)

    return greeting_to

greet = greetings(bar) # set bar as a greeting function
greet('Terry') # use the return function to generate greetings
# => Hello, Terry!
# => Welcome, back!

```

### 2. Decorators

A **Function Decorator** is a wrapper to an existing function, in which you can do some pre-process to the parameter or post-process to the returning value of the existing funciton.

The function decorator in Python must follows the below rules:

 * It is a function that accept a function parameter(like saying _"a decorator to which function"_)
 * The decorator function must define and return a function as a result, so that the client gets something act similar to the existing function(act just like a function wrapper). 
 * Do the customizing things inside the wrapper function, and call the existing function eventually


```python

def greeting_decorator(call):
    def wrapper(name):
        call(name)
        print("Isn't it powerful?")
        
    return wrapper


# The decorator syntax
@greeting_decorator
def greet(name):
    print("Hello, {0}".format(name))

greet('Terry') # decorated function though the function name is the same as defined
# => Hello, Terry 
# => Isn't it powerful?

```

Decorators can be chained, and can also accept extra parameters when defining the customization to the function. However, decorators that accept parameters need to add another wrapper to the simple decorator.


```python

def room(room_name):
    def decorator_wrapper(func):
        def wrapper(name):
            print("Enter room: {0}".format(room_name))
            func(name)

        return wrapper
    return decorator_wrapper

def leave_on_greet(greet_func):
    def greeting_wrapper(name):
        greet_func(name)
        print("Thanks, I'm leaving")

    return greeting_wrapper


@room('Matrix')
@leave_on_greet
def greet(name):
    print("Hello, {0}".format(name))


greet('Terry')
# => Enter room: Matrix
# => Hello, Terry
# => Thanks, I'm leaving


```



### 3. Example: using decorator in Django views

It is very common that you want to write decorators for the request in views.py. For example, Django itself provides [a list of decorators](https://docs.djangoproject.com/en/1.10/topics/http/decorators/) that you can use in certain scenarios, such as restricting HTTP methods, or cache controls. There are also other examples that could be consider: logging requests or checking auth tokens.

Here I write a very simple example that logs requests which a specified module name. We will have to use a new feature here that passes arguments between functions, because Django view methods can accept arguments defined in URL patterns.


```python

# a request log decorator which you can define the module
def log_request(module=""):
    def decorator_wrapper(view_func):
        def func_wrapper(request, *args, **kwargs):
            print('[{0}] {1} {2} {3}'.format(module, request.get_host(), request.method, request.get_full_path()))
            return view_func(request, *args, **kwargs)
        return func_wrapper
    return decorator_wrapper


# use in views.py
@log_request(module="Book")
def book_detail(request, book_id):
    return HttpResponse('Book info: {0}'.format(book_id))


# URL patterns
urlpatterns = [
    url(r'^book/(?P<book_id>\d+/info$', views.book_detail),
    # ...
]

```

Test in command line:

```bash

# test in shell, and see the book id correctly returned
$ curl http://localhost/book/1/info
Book info: 1

# check the log in server console, everything is shown
[Book] localhost:8000 GET /v1/book/1/info

```

### Reference

Reference: <http://thecodeship.com/patterns/guide-to-python-function-decorators/>
