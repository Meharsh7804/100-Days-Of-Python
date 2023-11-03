# Write a Python program that checks if a given string is a palindrome (reads the same backward as forward) using an if statement.

user_input = input("Enter a string: ")

# Remove spaces and convert the string to lowercase for case-insensitive comparison
cleaned_input = user_input.replace(" ", "").lower()

# Check if the cleaned input is the same when reversed
if cleaned_input == cleaned_input[::-1]: # [::-1] is used to reverse the string.
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")