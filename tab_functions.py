from __future__ import print_function
import sys

if len(sys.argv) == 1 :
	print("Usage: insert a number as argument to select which function you want to use\n")
	print("- 1 for f(x)=x\n")

else:

	def function1(x):
		return x


	xval = [n*1.0 for n in range(-5,6,1)]

	func_num = int(sys.argv[1])
	if func_num == 1:
		yval=function1(xval)

	import matplotlib.pyplot as plt
	plt.plot(yval)
	plt.show()

