
# fruits = ["apple", "orange", "banana", "coconut"]
# vegatables = ["celery", "carrots", "patatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegatables, meats]

# print(groceries[0][3])

groceries = (("apple", "orange", "banana", "coconut"),
             ("celery", "carrots", "patatoes"),
             ("chicken", "fish", "turkey"))

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
