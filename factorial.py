# Find the factorial of a number
n = int(input("\nEnter the number for which factorial is to find:\t"))

fact = 1

for i in range(1,n+1):
    fact = fact * i

print(f"\n The factorial of {n} is : \t",fact)