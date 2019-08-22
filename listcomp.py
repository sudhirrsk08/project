a=[1,2,3,4,5,56,6,7]
b=[3,4,5,6,7,88,9,0]
for i,j in zip(a,b):
	print(i,j) 

keys = ['a','b','c','d','e'] 
values = [1,2,3,4,5]   
  
# but this line shows dict comprehension here   
myDict = { k:v for (k,v) in zip(keys, values)}   
  
# We can use below too 
# myDict = dict(zip(keys, values))   
  
print (myDict) 
