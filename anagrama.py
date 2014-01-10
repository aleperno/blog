#!/usr/bin/python
import sys
from itertools import permutations as perm

def stringTolist(string):
	l = []
	for i in string:
		l.append(i)
	return l

def listToString(_list):
	s = "".join(_list)
	return s

def permutations(_list):
	gen = perm(_list)
	while True:
		try:
			aux = gen.next()
			print "%s" % listToString(aux)
		except StopIteration:
			break

def main():
	pal = sys.argv[1]
	print "Las permutaciones posibles son:"
	lpal = stringTolist(pal)
	permutations(lpal)

if __name__ == '__main__':
	main()