a={'a':'1','b':'2','c':'1'}
print(a)
tmp={}
for k,v in a.items():
	print('k:%s,v:%s'%(k,v))
	tmp.setdefault(v,[]).append(k)
print(tmp)
