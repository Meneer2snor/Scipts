unit = input("Is this temperature in Celsius or Fahrenheit (C / F): ")
temp = float(input("Enter the temperature: "))

# voor ° moet je numlock aan + alt + 0176
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"That temperature in Fahremheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"That temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
