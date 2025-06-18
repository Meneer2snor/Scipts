name = input("Enter your full name: ")
phone_number = input("Enter your phone number #: ")
# len geeft de lengte aan van een string
# result = len(name)

# .find zoekt het eerste ... op in dit geval spatie en die staat met de naam Bjorn de Vos op 5
# result = name.find(" ")

# .find zoekt het laatste ... op in dit geval spatie en die staat met de naam Bjorn de Vos op 8
# result = name.rfind(" ")

# .capitalize geeft de waarde van name aan met aan het begin een hoofdletter dus bjorn wordt dan Bjorn
# name = name.capitalize()

# .upper geeft alles aan in hoofdletters
# name = name.upper()

# .lower geeft alles aan in kleine letters
# name = name.lower()

# .isdigit geeft aan of de naam alleen bestaat uit cijfers
# result = name.isdigit()

# .isalpha geeft aan of het alleen maar bestaat uit letters (spatie is geen letter)
# result = name.isalpha()

# .count kijkt hoe vaak iets voor komt
# result = phone_number.count("-")

# .replace vervangt het ene voor het ander
phone_number = phone_number.replace("-", " ")

print(help(str))
print(phone_number)
