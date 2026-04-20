'''
LEARNING A MODULAR PROGRAM:
The program has below tasks:
1. Check ticket price
2. Check baggage weight 

What is modularity?
Making one module each for every task or subtask in a program

Activity Task: Our Travel Buddy needs to show prices in Dollars for international tourists.
'''

#Task 1: CHECK TICKET PRICE
#Creating a new module/block of code (Module = Function = Method = Definition)
#A task/Mofule is abstracted within boundries or a block of code
def CalcTicketPrice(age): #Logic is abstracted in this function
    price = 1000 #creating price variable and setting a default price
    if (age < 3):
        price = 0 #Changing price in case of infant
    elif (age >= 60):
        price = 500 #Changing price in case of senior citizen
    return price #Sending a response to the call to function

#Task 2: CHECK BAGGAGE WEIGHT
def CheckBagWeight(weight):
    weightOk = 1 #This means weight is okay
    if(weight > 25):
        weightOk = 0 #This means weight is not okay
    return weightOk

#MAIN: BLOCK OF CODE TO CONNECT TASKS

#Display menu 
print("_________Welcome to Tarvel Buddy_________")
while True:
    print("1.Check ticket price \n2.Check baggage weight \n3.Exit")
    
    menuOpt = int(input("Enter your choice:")) #Get menu choice input
    #Check menu choice
    if(menuOpt == 1):
        age = int(input("Enter age of traveller:"))
        tPrice = CalcTicketPrice(age) #Calling function to get the price in return 
        print(f"The price of your ticket is: {tPrice} AED")  #Printing formatted statements using variables
    elif(menuOpt == 2):
        weight = float(input("Enter the weight of your bag:"))
        weightAllowed = CheckBagWeight(weight)
        if(weightAllowed == 1):
            print("Your weight is OK..Have a safe flight!")
        else:
            print("Your baggage is overweight..Please contact supervisor!")
    elif(menuOpt == 3):
        print("Thank you for using our service...Please come back again!")
        break #End the program
    else:
        print("Invalid Option...Please check the menu options and try again!")


