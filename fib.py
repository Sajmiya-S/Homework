# Fibonacci Series

fib = 0
sum = 0
for i in range(15): 
    if i <= 1:
        fib = fib + i 
        sum = sum + fib 
        print(fib)  
    else: 
        sum = fib - sum 
        fib = fib + sum 
        print(fib)