from __future__ import print_function
import sys
from math import *

if len(sys.argv) == 1 :
	print("Usage: insert a number as argument to select which function you want to use\n")
	print("- 1 for f(x)=x\n")
	print("- 2 for f(x)=sin(x)\n")
	print("- 3 for f(x)=cos(x)\n")
	print("- 4 for f(x)=tang(x)\n")

else:

	def function1(x):
		return x
	
	def trig_s(xlist):
		return [ sin(x) for x in xlist ]

	def trig_c(xlist):
		return [ cos(x) for x in xlist ]

	def trig_t(xlist):
		return [ tan(x) for x in xlist ]

	xval = [n*1.0 for n in range(-5,6,1)]

	func_num = int(sys.argv[1])
	if func_num == 1:
		yval=function1(xval)

	if func_num == 2:
		yval=trig_s(xval)

	if func_num == 3:
		yval=trig_c(xval)

	if func_num == 4:
		yval=trig_t(xval)

	import matplotlib.pyplot as plt
	plt.plot(yval)
	plt.show()

