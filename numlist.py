# Create a list of first 100 numbers
# From that list , Create :
# (1) a list of all even numbers 
# (2) a list of all odd numbers 
# (3) a list of numbers that are divisible by both 3 and 5

num = []
even = []
odd = []
div3n5 = []

for i in range(1,101):
    num.append(i)
print("\nFirst 100 numbers = ",num)

for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("\nEven numbers : ",even)
print("\nOdd numbers : ",odd)

for i in num:
    if i % 3 == 0 and i % 5 == 0:
        div3n5.append(i)
print("\n Numbers that are divisible by both 3 and 5 : ",div3n5)