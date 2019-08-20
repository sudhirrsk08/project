from collections import Counter
retrive_data=open("testing.txt",'r')
data=retrive_data.read()
file_list=data.split()
pali_list=[]
pali_index=[]
count=0
print("Palindrome List: ")
for a in file_list:
    if a==a[::-1]:
        pali_list.append(a)
for b in pali_list:
    c=len(b)
    pali_index.append(c)
long=max(pali_index)
index_value=pali_index.index(long)
long_word=pali_list[index_value]
print("longest palindrome:",long_word)
for c in pali_list:
    if long_word==c:
        count+=1
print(count)
print(long_word,"is Repeated",count,"times")
