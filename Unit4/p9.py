class Demo:
    def add(self, a=None, b=None, c=None):
        if a and b and c:
            print("Sum of 3:", a + b + c)
        elif a and b:
            print("Sum of 2:", a + b)
        else:
            print("Invalid input")

obj = Demo()
obj.add(10, 20)
obj.add(10, 20, 30)