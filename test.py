def fun(a,b):
	if(a==0):
		return b
	else:
		return fun(a-1,a+b)

print(fun(4,7))
