# Check whether an integer is palindrome or not

def is_palindrome(num):
    n = num
    rev = 0
    count = 0
    while n != 0:
        mod = n % 10
        rev = mod + rev * 10
        n = n // 10
        count += 1 
    if num == rev:
        return True
    else:
        return False
print("\n*****Palindrome Checker*****")
p = int(input("\nEnter a number:"))

print(is_palindrome(p))