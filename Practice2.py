# Exercise 2 shopping cart program

item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like?:"))
total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"That will be ${total} in total")
