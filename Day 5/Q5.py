#  Write a program that reads data from a CSV file called "data.csv" and calculates the average of a particular column (e.g., the "scores" column). Print the calculated average to the screen.

import csv

with open("Day 5/data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) #SKIP HEADER
    total = 0
    count = 0

    for row in reader:
        score = float(row[1])
        total += score
        count += 1
    
    average = total / count
    print("Average score : ",average)
