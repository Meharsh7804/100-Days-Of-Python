# Develop a Python program that prints all the prime numbers between 1 and 100 using nested for loops.
for num in range(2, 101):
    is_prime = True

    # Check if the current number is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # If the number is prime, print it
    if is_prime:
        print(num, end=" ")

print()