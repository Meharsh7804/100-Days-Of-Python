# Develop a Python program that asks the user to input a number and then prints the multiplication table for that number using a for loop.
num = int(input("Please enter a number "))

for i in range (1,11):
    print(num,"x",i,"=",num*i)