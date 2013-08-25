def iterativeFibo(number):
	list = [0,1]
	for i in range(2,number+1):
		list.append(list[i-1]+list[i-2])
	return list[number]