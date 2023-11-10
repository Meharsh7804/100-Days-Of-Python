# Create a list called fruits with three of your favorite fruits and print the list.

fruits = ["Dragon Fruit", "Raspberryfruit","Avocado"]

print("Press '1' to add a new fruit in list." )
print("Press '2' to access 2nd element of list.")
print("Press '3' to remove first element of list.")
choice = int(input("Enter a choice"))

if (choice == 1):
    fruits.append("Strawberry")
    print(fruits)

elif (choice == 2):
    random = fruits[1]
    print(random)

elif (choice == 3):
    fruits.remove(fruits[0])
    print(fruits)

else:
    print("Invalid Choice")