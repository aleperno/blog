#!/usr/bin/python

dict = {}


def counter():
	aux = 0
	aux2 = 0
	for i in dict:
		aux = aux + dict[i]-1
		aux2 = aux2 + dict[i]
	return (aux,aux2)

def collisioner(number):
	global dict
	if number < 2: return
	if number not in dict:
		dict[number]=1
	else:
		dict[number]=dict[number]+1

def recursiveFibo(number):
	"""Recursive implementation of the fibonacci function"""
	if (number < 2):
		return number
	else:
		collisioner(number-1)
		collisioner(number-2)
		return recursiveFibo(number-1)+recursiveFibo(number-2)

def main():
	global dict 
	print "Calculating the fibonacci of 4 by recursion"
	recursiveFibo(4)
	print "The collisions were: \n",dict
	print "There were: ",counter()," collisions" 
	print "############################################"
	dict = {}
	print "Calculating the fibonacci of 5 by recursion"
	recursiveFibo(5)
	print "The collisions were: \n",dict
	print "There were: ",counter()," collisions" 
	print "############################################"
	dict = {}
	print "Calculating the fibonacci of 6 by recursion"
	recursiveFibo(6)
	print "The collisions were: \n",dict
	print "There were: ",counter()," collisions" 
	print "############################################"
	dict = {}
	print "Calculating the fibonacci of 7 by recursion"
	recursiveFibo(7)
	print "The collisions were: \n",dict
	print "There were: ",counter()," collisions" 
	print "############################################"
	dict = {}
	print "Calculating the fibonacci of 8 by recursion"
	recursiveFibo(8)
	print "The collisions were: \n",dict
	print "There were: ",counter()," collisions" 
	print "############################################"
	dict = {}
	print "Calculating the fibonacci of 9 by recursion"
	recursiveFibo(9)
	print "The collisions were: \n",dict
	print "There were: ",counter()," collisions"
	print "############################################"
	dict = {}
	print "Calculating the fibonacci of 10 by recursion"
	recursiveFibo(10)
	print "The collisions were: \n",dict
	print "There were: ",counter()," collisions"  
main()
