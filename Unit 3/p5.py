# Wap A Program TO input Number Wether Prime Or Not
def prime(p):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
        
num = int(input("Enter a number: "))
prime(num)