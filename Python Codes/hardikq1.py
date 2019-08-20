from collections import Counter
string={}
s=input('Enter the data: ')
lists=[]
fi_data=[]
final=[]

while len(s)!=0:
	head = str(s.rstrip('0123456789'))
	tail = s[len(head):]
	fi=head[:-1]
	tot=len(head)
	lists.append((head[tot-1],tail))
	s=fi

lists.sort()
#print(lists)
for a in lists:
	b=a[0]*int(a[1])
	fi_data.append(b)
last_data=''.join(fi_data)
oks=Counter(last_data)
for c in oks:
	string[c]=oks[c]
print(string)
for d in string:
	final.append(d)
	final.append(str(string[d]))
result=''.join(final)
print("The final output: ",result)
	

	
