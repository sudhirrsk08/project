def sample(*argv):
	for ar in argv:
		print(ar)
def test(**argv):
	for ar,arr1 in argv.items():
		print("%s===%s"%(ar,arr1))




sample('hello','world','python')

test(sdr='hi', psh='exit')
