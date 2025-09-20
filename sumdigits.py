# To find the sum of digits in a number

num = int(input("\nEnter a number:\t"))

sum = 0
n = 0

while num % 10 != 0:
    n = num % 10
    num = num // 10
    sum = sum + n

print("\n Sum of digits is : ",sum)

