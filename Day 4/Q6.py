# Create a Python module named utils that contains a function to check if a number is prime or not. Import this module and use the function to determine if a given number is prime.
import utils as check

print("Wanna check that a number is prime or not?")
a = int(input("Enter a number: "))

b= check.isPrime(a)
print("Number is Prime!") if b else print("Number is Composite!")