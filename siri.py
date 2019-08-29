x=int(input())
sqrs=dict()
while x>0:
	key = input("Enter the key: ")
	value = int(input("Enter the value: "))
	sqrs[key] = value
	x-=1
print(sqrs)
x=input()
for k,v in sqrs.items():
	if(k==x):
		print(sqrs[k])

