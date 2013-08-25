def recursiveFibo(number):
	"""Recursive implementation of the fibonacci function"""
	if (number < 2):
		return number
	else:
		return recursiveFibo(number-1)+recursiveFibo(number-2)