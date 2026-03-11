# Sum Of Odd and Even From 1 to 20

a=int(input("Enter Number For A "))
b=int(input("Enter Number For B "))
even=0
odd=0

for n in range (a,b+1):

    if n % 2 == 0 :
        even+=n

    else:
        odd+=n

print("Total Of Even IS : ",even)
print("Total Of Odd IS  : ",odd)

print ("Finish")
        
