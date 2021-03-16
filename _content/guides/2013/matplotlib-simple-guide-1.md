# Matplotlib Example in Short (1) - The Plotting Graph

- date: 2013-12-31 01:00
- tags: python, graph, matplotlib
- category: guides

--------------------------------

The book [_"Beginning Python Visualization"_](http://www.amazon.com/Beginning-Python-Visualization-Transformation-Professionals/dp/1430218436) (by Shai Vaingast) is a great book for learning data visualization with Python. Here I would like to write a short reference guide for the Matplotlib usage after studying with it.

## Why Matplotlib?

In my opinion, there are different purpose while working on visualization: 1. scientific presentation; 2. web(real time / periodic update) presentation; 3. artistic presentation. The **Matplotlib** library in python is mainly served for the first and the  purpose, where you can easily plot data on the graph for analyzing and crafting your visualization script, at the same time you could use with IPython Notebook or in other web development to render statistics and display on the web. 

If you have complicated graph or artistic requirements on the final result, you might move on to [Bokeh](http://bokeh.pydata.org/) or [NodeBox OpenGL] (), but matplotlib is still a handy tool for dealing with raw data in preceding scenarios.

## The Basic Plotting

Here is a basic example to show how to use the basic plotting function in Matplotlib.

The graph image:

![alt](http://terryoy-github.u.qiniudn.com/blog/images/2013/matplotlib_sum_graph.png "Matplotlib Plotting Graph Summary example")

The source code:

```python

# remember in matplotlib-1.1 we import everything from **pylab** 
from pylab import *

I = arange(0, 2*pi+0.1, 0.01)
hold(True)
plot(cos(I), sin(I), label='x = cos($\alpha$), y = sin($\alpha$)')
plot([0, cos(pi / 4)], [0, sin(pi/4)], "k-", [0, 1], [0, 0], "k-") 
I1 = arange(0, pi/4, 0.01)
plot(0.3 * cos(I1), 0.3 * sin(I1), 'b--')
title('Drawing a Cicle by Radius')
xlabel('x = cos(I), I = [0, $2\pi$]')
ylabel('y = sin(I), I = [0, $2\pi$]')
text(0, 1, 'Top', ha='left', va='bottom')
text(0, -1, 'Bottom', ha='left', va='top')
text(0.4 * cos(pi / 8), 0.4 * sin(pi / 8), '$45^\circ$', ha='left', va='bottom')
xticks(arange(-1, 1, 0.25))
xlim([-1.2, 1.2])
ylim([-1.2, 1.2])
grid()

show()

```

Now let's check out each commands we could use.

### 1. plot(), markers, line styles, and colors

```python
    
# plot accept vectors to draw lines
plot([1,2,3])   # given one vector, it will take it as both X, and Y
plot(arange(5))     # arange() is a function from NumPy which could generate vectors
I = arange(-5, 5.1, 1)    # arange(begin value, end value, step)
plot(I, 2*I)    # plot a "y = 2x" line with the vector I as X's range

plot(I, 2*I, 'ko-', I, I*I, 'bD--') # multi-plot with options in one line

# now check out the short options, which you could use in the third parameter in each plot
# -- Markers (check out doc for more)
#   'o': Circle, 
#   '^': Upward-pointing triangle,
#   's': Sqaure,
#   '+': Plus,
#   'x': Cross,
#   'D': Diamond
#
# -- Line Styles
#   '-': Solid line,
#   '--': Dashed line,
#   '-.': Dash-dot line,
#   ':': Dotted line
#
# -- Color
#   'b': Blue,
#   'c': Cyan,
#   'g': Green,
#   'k': Black,
#   'm': Magenta,
#   'r': Red,
#   'w': White,
#   'y': Yellow

plot(I, I*I, 'o-', lw=2, ms=6) # lw/linewidth - Line Width, ms/markersize - Marker Size

```

### 2. Axes and Grids, text, legends and titles

```python

# range of axes
axis([-6, 6, -6, 6])    # accept an array with [xmin, xmax, ymin, ymax]
xlim(-10, 10)   # or if you want to set Axis X or Axis Y separately
ylim(-10, 10) 
axis()  # check the current axes range
xlim()
ylim()

# grids and ticks
grid(True)  # set grid display to True or False
xticks(arange(-5, 5, 1))    # customize the tick locations on Axis X
yticks(arange(-5, 25, 5))   # customize the tick locations on Axis Y
xticks(arange(5), ('Tom', 'Jerry', 'Sally', 'Harry', 'Me'))   # also customize the tick labels

# draw axes lines
axvline(linewidth=4, color='r') # draw a vertical axis line at x=0, with linewidth and color
axvline(1, 0.2, 0.8)    # draw a vertical line on x=1, with vertical ratio (0.2, 0.8) of the graph's height
axhline(y=0, xmin=0, xmax=1)    # draw a horizontal axis similar to axvline()

# enable legends
plot(I, I*I, label="y = x^2")
legend()    # enable legends of existing lines
legend(['sin(x)', 'cos(x)'])    # set legend text explicitly


# text at any position
text(1, 1, 'text positioned at (1, 1)', va='baseline', ha='left')   # draw text with vertical and horizontal alignment
text(1, 1, 'some text', bbox=dict(facecolor='red', alpha=0.5))  # draw text with a rectangle background

# title of the graph
title('some title', va='baseline', ha='center') # draw the title text of the graph

# labels of axes
xlabel('Time")
ylabel('Money we gain')

# use (TeX-like) symbols, **you must use raw string (r'text')**
title(r'$ \alpha_i > \beta_i $')    # TeX-like symbols should be surrounded by '$$'


```
For more TeX symbols, please check the [reference on matplolib](http://matplotlib.org/users/mathtext.html#symbols).

### 3. Figure control

```python

# create / specify a figure to plot
figure()    # create a new figure by default
figure(2)   # switch to the figure with id 2
# save figure to a file (select format by extension)
savefig('filename.png') 

# creating subplots
# subplot(numRows, numCols, plotNum)
subplot(1, 1, 1)    # the default 
subplot(2, 1, 1)    # split in 2 x 1 table, and draw on upper half
subplot(2, 2, 3)    # split in 2 x 2 table, and draw on the bottom left(it can work together with the above one, as long as the plots don't overlap)

# erasing the graph 
cla()   # clear axes
clf()   # clear figure
close(1)    # close figure with id (if specified)


