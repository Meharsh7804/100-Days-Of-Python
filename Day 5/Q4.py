#   Write a Python program that takes multiple text files as input, concatenates them, and saves the result to an output file. The program should ask the user to enter the names of the input files and the name of the output file.

# Prompt the user for input and output file names
input_files = input("Enter the names of input files (separated by space): ").split()
output_file = input("Enter the name of the output file: ")

# Concatenate input files and write to the output file
with open(output_file, "w") as output:
    for input_file in input_files:
        with open(input_file, "r") as file:
            output.write(file.read())