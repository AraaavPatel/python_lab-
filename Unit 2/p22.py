

s1=int(input("Enter Marks For S1" ))
s2=int(input("Enter Marks For S2" ))
s3=int(input("Enter Marks For S3" ))
s4=int(input("Enter Marks For S4" ))

to=s1+s2+s3+s4

per=to/4

print("Total Percentage",per)

if s1<40 or s2<40 or s3 <40 or s4 <40:
    print("The Student Is Failed")
elif per<=40 :
    print("The Student got D Grade")
elif per<=60 :
    print("The Student got C Grade")
elif per<=80 :
    print("The Student got B Grade")
elif per<=90 :
    print("The Student got A Grade")
elif per<=95 :
    print("The Student got S Grade")
elif per > 95 :
    print("The Student got O Grade")



'''if per < 40:
    print("Student IS Failed")
else:
    print('Student IS pass')'''
