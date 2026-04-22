'''
Program Global Store Manager Program
Author: SOnu
Date: 22 April, 2026

Features:
1. standard checkout 
2. International/ Tourist checkout 
3. System Function demo

# classroom activity/ homework feature of existing the same program
- Add the customer a VIP (Enrolled in the customer loyality  program). If VIP reduce price by 2%.
- Add need gift wrap option. Charge 5 for wrapping.
'''
import math  # Import math library for math functions

# Function with default values for tax and discount
def CalcStoreBill(price, tax=0, discount=0):  # Default values assigned
    totalBill = price + (price * tax / 100) - discount  # Fixed formula
    return totalBill

# Main Program - Menu Loop
while True:
    print("1. Standard checkout\n2. Tourist checkout\n3. System Function Demo (Price Round-up)\n4. Exit")
    menuOpt = int(input("Enter an option: "))

    if menuOpt == 1:
        price = float(input("Enter the price of the item: "))
        finalBill = CalcStoreBill(price)  # Uses default tax=0, discount=0
        print("The final bill is:", finalBill)

    elif menuOpt == 2:
        price = float(input("Enter the price of the item: "))  # Fixed: was 'print =' instead of 'price ='
        customTax = float(input("Enter the custom tax in %: "))
        discount = float(input("Enter the discount for the item: "))
        finalBill = CalcStoreBill(price, customTax, discount)  # Overloaded call
        print("The final bill is:", finalBill)

    elif menuOpt == 3:
        price = float(input("Enter a decimal price to round up: "))
        roundedPrice = math.ceil(price)   # Fixed: was math.cell (typo)
        print(f"Round to ceil is - {roundedPrice}")   # Fixed: used f-string
        roundedPrice = math.floor(price)
        print(f"Round to floor is - {roundedPrice}")  # Fixed: used f-string

    elif menuOpt == 4:
        break

    else:
        print("Invalid Choice!")

print("Thank you for using the store!")