n=input()
m=input().split()
a=[int(b) for b in m]
a.sort()
c=max(a)
d=[e for e in a if e!=c]
print(d[-1])

