from collections import Counter
retrive_data=open("testing.txt",'r')
data=retrive_data.read()
file_list=data.split()
print("Palindrome List: ")
for a in file_list:
    if a==a[::-1]:
        print(a)
count_word=Counter(file_list)
print("Repeated Words Data: ")
for b in count_word:
    print(b,":",count_word[b])
