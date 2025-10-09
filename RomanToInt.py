# Change the given roman number to integer
def romanToInt(s):
    num = 0
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] > roman[s[i + 1]] :
            num += roman[s[i]]
        elif i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            num -= roman[s[i]]
        else:
            num += roman[s[i]]
    return num

s = input("\nEnter a Roman Number: ").upper()
print(romanToInt(s))