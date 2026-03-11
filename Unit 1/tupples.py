# Creat tuple 

tp=("Arav","Arman","Rajat",'Devgang','Sarthak')
print('\ntp = ',tp)


#MULTIPLE data type tuple

tp1=('Arav',20,5.11)
print('\ntp1 = ',tp1)

tp2=(65,68,321,465,23,645,98,23)
print('\ntp2 = ',tp2)

#print specific element

print(tp1[2])

#conveert to string

str = " ".join(tp)

print('\n',str)


#4 element from the last element

print('\n', tp[-4])


#check wether an element exist or not

a =int(input('Enter An Number : '))

if a in tp2:
    print('\nThe Character is Available In Tuple : ',a)
elif a not in tp2:
    print('\nThe character is Not Available in Tuple : ',a)

#to conuvert a list to a tuples
li=[5,6,8,9,7,3,4]
li= tuple(li)
print('\n',li)

