# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# Update an exhisting key:value or add a new to it
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})

# Remove key:value pair
# capitals.pop("China")

# Remove latest key:value pair
# capitals.popitem()

# Clear the dictionary
# capitals.clear()

# To get all the keys but not the values
# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# To get all the values but not the keys
# values = capitals.values()
# for value in capitals.values():
#     print(value)

# Resembles a 2d list of tuples
# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")
