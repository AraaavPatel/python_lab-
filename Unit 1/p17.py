#wap to remove specific eliment from the list


l1 = [10, 20, 30, 40, 50]

print(l1)

val=int(input('Enter How many values You want  to Remove'))

for n in range(val):

    a = int(input("Enter index number to remove: "))

    if 0 <= a < len(l1):
        l1.pop(a)
        print("Updated List:", l1)
    else:
        print("Enter valid index from 0 to", len(l1) - 1)

print("Delition complited")
