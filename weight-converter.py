weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds ? (K/L): ").lower()

if unit == 'k':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f"Your weight is: {round(weight,1)} {unit}")   
elif unit == 'l':
    weight = weight / 2.205
    unit = 'Kgs.'
    print(f"Your weight is: {round(weight,1)} {unit}")   
else:
    print(f"{unit} is not valid.")
    
           