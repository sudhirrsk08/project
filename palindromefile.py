def Reverse(s):
    answer=""
    for c in s:
        answer=c+answer
    return answer
def IsPalindrome(s):
    if s==Reverse(s):
        return True
    else:
        return False

def checkPalin(word): 
	if word.lower() == word.lower()[::-1]: 
		return True

F=open("Wordlist.txt","r")
for line in F:
	count=0
	word=line.strip("\n")
	for elements in word: 
     		if (checkPalin(elements)): 
            		count += 1
	print (count) 
if IsPalindrome(word):
     print ("%s"%word)

