# find the reverse of a number

num = int(input("\nEnter a number:\t"))

rev = 0

while num > 0:
    n = num % 10
    num = num // 10 
    rev = rev * 10 + n

print("\nReverse of the number : \t",rev)

