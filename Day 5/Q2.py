# Create a program that asks the user to enter their age. Check if the input is a valid integer. If it's not, handle the exception and ask the user to enter the age again until a valid input is received.

while True:
    try:
        age = int(input("Enter your age"))
        break
    except ValueError:
        print("Enter validage. Try again")
print("Age : " + age)