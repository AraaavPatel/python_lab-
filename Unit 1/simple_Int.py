#Wap For Find Simple Intrest

p =int(input("Enter Amount :"))
r =float(input("Enter Roi :"))
t =int(input("Enter Time :"))

si= p*r*t/100
print(si)
print("\n Total Payable amount is",p+si)
