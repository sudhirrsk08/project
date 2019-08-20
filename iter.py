mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
#raise StopIteration
print(next(myit))
print(next(myit))

print(mytuple)
myit=iter(mytuple)
print(next(myit))
