l=[]
def A(str):
	for i in list(str):
		print(i)
		if i != "a":
			l.append(i)
	print(l)
	l.reverse()
	print("l_reverse: \n%s"%(l))
	str_new = "".join(l)
	print('return_str:\t"%s"'%(str_new))
A(input("input string\n"))