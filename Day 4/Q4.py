#  Write a Python function that takes a list as a parameter and returns the maximum value in the list.
def max_value(lst):
    highest = lst[0]  # Initialize highest to the first element in the list
    for item in lst:
        if item > highest:
            highest = item
    print("Maximum value from collection:", highest)

my_list = [48, 97, 86, 12, 39, 77, 53, 10, 8]
max_value(my_list)