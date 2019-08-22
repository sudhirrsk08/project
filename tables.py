a = int(input("Enter table no\n"))
table = [[a, b, a * b] for b in range(1, 11)] 
  
print("\nMultiplication Table") 
for i in table: 
    print (i) 
