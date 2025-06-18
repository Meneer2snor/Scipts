# Python calculator

operator = input("Enter an operator (+ - * /): ")


if operator == "+":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 + num2
    print(round(result, 2))

elif operator == "-":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 - num2
    print(round(result, 2))

elif operator == "*":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 * num2
    print(round(result, 2))

elif operator == "/":
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator")
