person = {
    "name": "Bhupender Jogi",
    "age": 20,
    "city": "America"
}

print(person)

person["age"] = 25
print(person)

person["occupation"] = "Traveler"
person.pop("city")
print(person)   

if("name" in person):
    print("Positive")
else:
    print("Negative")

print(person.keys())
print(person.values())

for key in person:
    print(person[key])