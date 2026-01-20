print("______commence du convertisseur final______")
from Convertisseur import degre_to_farenheit , euro_to_dollars, km_to_miles
choice = input("Choose conversion type (1: Euro to Dollars, 2: Degree to Fahrenheit, 3: Km to Miles): ")
if choice == '1':
    euro = float(input("Enter amount of euro that you want to convert : "))
    dollars = euro_to_dollars(euro)
    print(f"{euro} euros is equal to {dollars} dollars : ")
elif choice == '2':
    degre = float(input("Enter the degree that you want to conver in farenheit : "))
    farenheit = degre_to_farenheit(degre)
    print(f"{degre} degree is equal to {farenheit} farenheit : ")
elif choice == '3':
    km = float(input("Enter the km that you want to convert to miles: "))
    miles = km_to_miles(km)
    print(f"{km} km is equal to {miles} miles : ")
else : 
    print("Invalid choice. Please select 1, 2, or 3.")
