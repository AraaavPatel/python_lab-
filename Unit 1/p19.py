
l1=[65,98,23,45,178,621,98,19,987,5]

max=l1[0]
min=l1[0]
for i in range(10):
    if min > l1[i]:
        min = l1[i]
    if max < l1[i]:
        max = l1[i]

print(l1)
print("Maximum is",max)
print("Minimum Is",min)
