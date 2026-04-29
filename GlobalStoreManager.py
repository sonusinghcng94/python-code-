'''
Program: Global Store Manager Program
Author: PSUC
Date: 22nd April 2026

Features: 
1. Standard checkout - 5% default tax
2. International/Tourist checkout - custom tax + discount
3. System Function Demo

Classroom Activity/Homework features of extending the same program
- Add the customer a VIP (Enrolled in the customer loyalty program). If VIP reduce price by 2%.
- Add gift wrap option. Charge 5 for wrapping.

'''

#import a third party library
import math  #Math library with predefined or system defined functions

#Functions/Modules (User-defined function)
#Standard & Tourist checkout - One function for two tasks -> Function Overloading
def CalcStoreBill(price, tax=5, discount=0): #Use assigned default values when inputs are not supplied.
    totalBill = price + ((price*tax)/100) - discount
    return totalBill

#Main Program
#Menu Loop
while True:
    #Display the menu
    print("1.Standard checkout\n 2.Tourist checkout\n 3.System Function Demo (Price Round-up)\n 4.Exit")

    menuOpt = int(input("Enter an option: ")) #Get menu option from user

    #Evaluate the Menu Option
    if(menuOpt == 1):
        price = float(input("Enter the price of the item:"))
        finalBill = CalcStoreBill(price) #different version of call
        print("The final bill is: ", finalBill)
    elif(menuOpt == 2):
        price = float(input("Enter the price of the item:"))
        customTax = float(input("Enter the custom tax in %:"))
        discount = float(input("Enter the discount for the item:"))
        #Function overriding
        finalBill = CalcStoreBill(price, customTax, discount) #another version of call
        print("The final bill is: ", finalBill)
    elif(menuOpt == 3):
        price = float(input("Enter a decimal price to round-up:"))
        roundedPrice = math.ceil(price) #round to nearest higher
        print(f"Round to ceil is - {roundedPrice}")
        roundedPrice = math.floor(price) #round to nearest lower
        print(f"Round to floor is - {roundedPrice}")
    elif(menuOpt == 4):
        break;
    else: 
        print("Invalid choice!")

print("Thank you for using the store!");