# Given a JSON file called "data.json" containing an array of objects, write a program that reads the file, extracts specific data (e.g., names or ages),and prints it to the console.

import json

with open("Day 5/data.json", "r") as file :
    data = json.load(file)

for entry in data :
    print(entry["name"])