#pass By Values

def per(a,b):
    a.append(50)
    print("--------------------------------")
    print(f"inside the Function:{a}")

    b.append("Have A Good Day")
    print(f"inside The Function:{b} ")

    print("--------------------------------")


a=[10,20,30,40]
b=["Hello World."]

print("--------------------------------")
print(f"before the function int:{a}")
print(f"before the Function the String:{b}")

per(a,b)

print(f"Outside The Function int : {a}")
print(f"Outside the function String : {b}")
print("--------------------------------")


#SUM all the number
#find thmax of three num
#multiply all the numbers in list
#check weather a number falls within a given range
#to print the even number form a given list
#wap to add,sub,mul,divof all the numbers in list