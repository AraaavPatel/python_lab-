values = input("Enter comma-separated numbers: ")

lst = values.split(",")   # convert to list
tpl = tuple(lst)         # convert to tuple

print("List:", lst)
print("Tuple:", tpl)