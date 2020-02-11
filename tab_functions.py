from __future__ import print_function
import sys
from math import *

if len(sys.argv) == 1 :
	print("Usage: insert a number as argument to select which function you want to use\n")
	print("- 1 for f(x)=x\n")
	print("- 2 for f(x)=x**2\n")
	print("- 3 for f(x)=x**3\n")

else:

	def function1(x):
		return x

	def polynomial(xlist, n):
		return [ x**n for x in xlist ]
	
	xval = [n*1.0 for n in range(-3,4,1)]

	func_num = int(sys.argv[1])
	if func_num == 1:
		yval=function1(xval)

	if func_num == 2 or func_num == 3:
		yval=polynomial( xval, func_num)

	import matplotlib.pyplot as plt
	plt.plot(yval)
	plt.show()

