from __future__ import print_function
import sys
from math import *

func_num = int(sys.argv[1])

def function1(x):
	return x

def polynomial(xlist, n):
	return [ x**n for x in xlist ]


xval = [n*1.0 for n in range(-5,6,1)]

if func_num == 1:
	yval=function1(xval)

if func_num == 2 or func_num == 3:
	yval=polynomial( xval, func_num)


import matplotlib.pyplot as plt
plt.plot(yval)
plt.show()

