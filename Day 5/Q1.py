# Write a Python program that reads a text file named "input.txt," counts the number of lines in the file, and then writes the count to an output file named "output.txt".
with open("Day 5\input.txt", "r") as input_file, open("day 5\output.txt", "w") as output_file:
    lines = input_file.readlines()
    lines_count = len(lines)
    output_file.write(str(lines_count))
    print("Number of lines = ", lines_count)