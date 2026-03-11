#Wap To Fing Compound interest 
P = int(input( "Enter Total Amount : "))   
R = float(input("\nEnter ROI: "))
T = int(input("\nEnter Year : "))      

A = P * (1 + R/100) ** T
CI = A - P

print("Compound interest:",CI)
