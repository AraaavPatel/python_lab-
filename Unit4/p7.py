f = open("numbers.txt", "r")

total = 0
count = 0

for line in f:
    num = int(line.strip())
    print(num)
    total += num
    count += 1

avg = total / count

print("Total:", total)
print("Average:", avg)

f.close()