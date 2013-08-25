
def calc(n):
	if n <4:
		return 0
	else:
		return calc(n-1)+calc(n-2)+(n-3)