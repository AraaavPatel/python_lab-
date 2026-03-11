# program for swap walue without using temp

a = 20
b = 30

print("Before Swap")
print (a,b)
print()

a,b=b,a
print("After Swap")
print (a,b)
print()

c = a
a = b
b = c
print("After Swap")
print (a,b)

