#!/usr/bin/python

import time

def recursiveFibo(number):
	"""Recursive implementation of the fibonacci function"""
	if (number < 2):
		return number
	else:
		return recursiveFibo(number-1)+recursiveFibo(number-2)

def iterativeFibo(number):
	list = [0,1]
	for i in range(2,number+1):
		list.append(list[i-1]+list[i-2])
	return list[number]

def main():
	print "Calculating the fibonacci of 4 by recursion"
	exetime = time.time()
	print "The fibonacci of 4 is: ",recursiveFibo(4)
	print "The execution lasted: ",time.time()-exetime," seconds"
	print "-----------------------------------------------------"
	print "Calculating the fibonacci of 4 by iteration"
	exetime = time.time()
	print "The fibonacci of 4 is: ",iterativeFibo(4)
	print "The execution lasted: ",time.time()-exetime," seconds"
	print "#####################################################"
	print "Calculating the fibonacci of 40 by recursion"
	exetime = time.time()
	print "The fibonacci of 40  is: ",recursiveFibo(40)
	print "The execution lasted: ",time.time()-exetime," seconds"
	print "-----------------------------------------------------"
	print "Calculating the fibonacci of 40 by iteration"
	exetime = time.time()
	print "The fibonacci of 40 is: ",iterativeFibo(40)
	print "The execution lasted: ",time.time()-exetime," seconds"
main()