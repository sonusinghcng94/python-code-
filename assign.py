import math 

# Updated Function with VIP and Gift Wrap logic
def CalcStoreBill(price, tax=5, discount=0, is_vip=False, gift_wrap=False):
    # Apply VIP discount first (2% off the base price)
    if is_vip:
        price = price * 0.98
    
    # Calculate tax and subtract manual discount
    totalBill = price + ((price * tax) / 100) - discount
    
    # Add flat gift wrap fee if selected
    if gift_wrap:
        totalBill += 5
        
    return totalBill

# Main Program
while True:
    print("\n--- Store Manager Pro ---")
    print("1. Standard Checkout")
    print("2. Tourist Checkout")
    print("3. VIP Checkout (New)")
    print("4. System Function Demo")
    print("5. Exit")

    try:
        menuOpt = int(input("Enter an option: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if menuOpt == 1:
        price = float(input("Enter the price: "))
        finalBill = CalcStoreBill(price) 
        print(f"The final bill is: {finalBill:.2f}")

    elif menuOpt == 2:
        price = float(input("Enter the price: "))
        customTax = float(input("Enter tax %: "))
        discount = float(input("Enter discount: "))
        finalBill = CalcStoreBill(price, customTax, discount)
        print(f"The final bill is: {finalBill:.2f}")

    elif menuOpt == 3:
        # VIP specific logic including Gift Wrap option
        price = float(input("Enter the price: "))
        is_vip = input("Is the customer a VIP? (y/n): ").lower() == 'y'
        wrap = input("Add gift wrap for 5? (y/n): ").lower() == 'y'
        
        finalBill = CalcStoreBill(price, is_vip=is_vip, gift_wrap=wrap)
        print(f"The final bill (VIP/Wrap applied) is: {finalBill:.2f}")

    elif menuOpt == 4:
        price = float(input("Enter a decimal price: "))
        print(f"Ceil: {math.ceil(price)} | Floor: {math.floor(price)}")

    elif menuOpt == 5:
        print("Closing system...")
        break
    else: 
        print("Invalid choice!")

print("Thank you for using the store!")