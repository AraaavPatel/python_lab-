#create blank Dictionary

di={}
print(di)

#Wap To Add Key & value to dictoinary

di1={1:20,2:30}

print('\n',di1)

di1.update({0:10,
            3:40})


print('\nUpdated Dictionary : ', di1)


#Wap to Sort Ascending A Dictionary

di2=dict(sorted(di1.items()))

print('\nAscending order : ',di2)

di3=dict(reversed(di2.items()))

print('\nDescending Order : ',di3)

#Wap To Concatenate The Following To Create New ONE .(use update())

di4={1:10,2:20}
di5={3:30,4:40}
di6={5:50,6:60}

di4.update(di5.items())
di4.update(di6.items())
print('\nUpdated Dictionary : ',di4)


#Check key Exist or Not

k=int(input('Enter number to Find Key : '))

if  k in di4:
    print("Key Exist")
else:
    print("Key Dose'nt Exist")

#Wap To Itrate Over Dictinoary using Loop

for i,j in di4.items():
    print(i,j)


