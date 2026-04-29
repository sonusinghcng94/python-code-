# Task 1: CHECK TICKET PRICE
def CalcTicketPrice(age):
    price = 1000
    if age < 3:
        price = 0
    elif age >= 60:
        price = 500
    return price

# NEW MODULE: CONVERT AED TO USD
def ConvertToUSD(aed):
    exchange_rate = 0.27   # 1 AED = 0.27 USD
    usd = aed * exchange_rate
    return usd

# Task 2: CHECK BAGGAGE WEIGHT
def CheckBagWeight(weight):
    weightOk = 1
    if weight > 25:
        weightOk = 0
    return weightOk


# MAIN PROGRAM
print("_________Welcome to Travel Buddy_________")

while True:
    print("\n1.Check ticket price \n2.Check baggage weight \n3.Exit")
    
    menuOpt = int(input("Enter your choice: "))
    
    if menuOpt == 1:
        age = int(input("Enter age of traveller: "))
        
        # Get price in AED
        tPriceAED = CalcTicketPrice(age)
        
        # Convert to USD
        tPriceUSD = ConvertToUSD(tPriceAED)
        
        print(f"Ticket Price: {tPriceAED} AED")
        print(f"Ticket Price in Dollars: {tPriceUSD:.2f} USD")
    
    elif menuOpt == 2:
        weight = float(input("Enter the weight of your bag: "))
        weightAllowed = CheckBagWeight(weight)
        
        if weightAllowed == 1:
            print("Your weight is OK..Have a safe flight!")
        else:
            print("Your baggage is overweight..Please contact supervisor!")
    
    elif menuOpt == 3:
        print("Thank you for using our service...Please come back again!")
        break
    
    else:
        print("Invalid Option...Please try again!")