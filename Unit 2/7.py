#Wap input age of persion and give msg

age= int(input("Enter Your Age : "))

if age >= 1 and age <= 12 :
    print("You Are Kid ")
    
elif age >=12 and age <= 17:
    print("Your Are Teenager")
    
elif age >= 18 and age <= 60:
    print("You Are Adult")

elif age >= 60:
    print("You Are Senior citizen")

elif age > 120:
    print("No Citizen Exist")
    print("Enter valid Number")
else:
    print("Enter valid Number")

