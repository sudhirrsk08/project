def isPalindrome(s): 
	rev=s[::-1]
	if (s == rev): 
        	return True
	return False
  
s = input("enter a string\n")
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No")
