f = open("names.txt", "w")

n = int(input("How many names? "))

for i in range(n):
    name = input("Enter name: ")
    f.write(name + "\n")

f.close()
print("Names saved to file.")