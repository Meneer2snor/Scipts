# input() = A function that promts the user to enter data
#          Returns the entered data as a string

name = input("What is your name?:")
age = int(input("How old are you?:"))

age = age + 1


print(f"Hello {name}!")
# f is niet nodig omdat je geen variables gebruikt
print("Happy Birthday!")
print(f"You are {age} years old")
