# Write a function that takes a string as input and returns the string reversed.
def reverse(string):
    reverse_string = string[::-1]
    print(reverse_string)

str = input("Enter something !\n")
reverse(str)