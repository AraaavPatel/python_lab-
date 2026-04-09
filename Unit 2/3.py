#pass by value
#integer
def mod(x):
    x=10
    print("Inside the function:",x)

num=5
mod(num)
print("Outside The Function:",num)

    
def merg(a,b):
    a=120
    print(f"inside the Fincton Int:{a}")
    b="Hello Mr."
    print(f"inside the function the string :{b}")

a= int(input("Enter Number a : "))
b= input("Enter Number b : ")

merg(a,b)
print(f"Outside the Function int:{a}")
print(f"Outside the Function string :{b}")
    
