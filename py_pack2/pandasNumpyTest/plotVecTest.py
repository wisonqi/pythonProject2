import time
import sys
import numpy as np

import matplotlib.pyplot as plt


# %matplotlib inline

def Plotvec1(u, z, v):
    ax = plt.axes()  # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r',
             head_length=0.1)  # Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')  # Adds the text u to the Axes

    ax.arrow(0, 0, *v, head_width=0.05, color='b',
             head_length=0.1)  # Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')  # Adds the text v to the Axes

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')  # Adds the text z to the Axes
    plt.ylim(-2, 2)  # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)  # set the xlim to left(-2), right(2)


def Plotvec2(a, b):
    ax = plt.axes()  # to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color='r',
             head_length=0.1)  # Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color='b',
             head_length=0.1)  # Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)  # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)  # set the xlim to left(-2), right(2)


# Plotvec1(u, z, v)

npl = np.linspace(-2, 2, 5)
print(npl)

a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))
