#Define function Without parameter

def hello():
    print("Hello,World...!")

hello()

#define a Function To Greet a Person

name=input("Enter Your Name : ")

def greet(name):
    print(f"hello,{name}!")

greet(f"{name}")


#define A function To Add Two Number

a=int(input("Enter number a : "))
b=int(input("Enter number b : "))
def add(x,y):
    return x+y

result = add(a,b)
print(f"The Sum is : {result}")

#define a function to calculate the area  of rectangle
l=int(input("Enter Length Of Rectangle : "))
b=int(input("Enter Bredth Of Rectangle : "))
def aor(l,b):
    area=l*b
    return area

n=aor(l,b)
print(f"The Area Of Rectangle Is : {n}")
