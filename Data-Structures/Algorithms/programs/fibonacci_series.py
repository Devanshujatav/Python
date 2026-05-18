def fibonacci(n):
    # Base case
    if n == 0 : 
        return 0
    elif n == 1 : 
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the number of terms in the Fibonacci series: "))
print("Fibonacci series: ")
for i in range(num):
    print(fibonacci(i), end=' ')