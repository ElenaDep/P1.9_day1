from __future__ import print_function
import sys
from math import *

if len(sys.argv) == 1 :
	print("Usage: insert a number as argument to select which function you want to use\n")
	print("- 1 for f(x)=x\n")

else:

	def function1(x):
		return x

	def irrat_e(xlist):
		return [ exp(x) for x in xlist ]


	def irrat_s(xlist):
		return [ sqrt(abs(x)) for x in xlist ]


	xval = [n*1.0 for n in range(-5,6,1)]

	func_num = int(sys.argv[1])
	if func_num == 1:
		yval=function1(xval)

	if func_num == 2:
		yval=irrat_e(xval)

	if func_num == 3:
		yval=irrat_s(xval)

	import matplotlib.pyplot as plt
	plt.plot(yval)
	plt.show()

