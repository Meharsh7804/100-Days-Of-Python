# Create a set with the common elements between the tuple (1, 2, 3) and the set {3, 4, 5}.

my_tuple = (1, 2, 3)
my_set = {3, 4, 5}

common_elements = set(my_tuple).intersection(my_set)

# common_elements = set(my_tuple) & my_set

print(common_elements)