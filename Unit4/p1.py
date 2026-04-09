#Wap A Program To Create A List in such that it should add squarre roots of number between 1 to n in the list 
#example:[1,44,9,16,25,.....]
n = int(input("Enter a number: "))
sqr = []
for i in range(1, n + 1):
    sqr.append(i * i)
print(sqr)

def sqr(n):
    sqr = []
    for i in range(1, n + 1):
        sqr.append(i * i)
    print(sqr) 

sqr(n) 
