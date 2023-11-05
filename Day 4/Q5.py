# Define a function that generates a Fibonacci sequence of a given length using recursion.
def fibonacci(length):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1

    while count <= length:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()

n = int(input("Enter the value of n "))
fibonacci(n)