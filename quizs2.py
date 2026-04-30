# Quizss Question 2

# Create an empty list to keep track of food
cart = []

print("Welcome to Hungry Bot!")

# Keep the loop running until we say 'done'
while True:
    # Ask the user for an item
    food = input("Enter an item to add to your cart (or type 'done' to finish): ")
    
    # Check if the user is finished
    if food == "done":
        print("Order complete! Your food is on the way.")
        break
    else:
        # Add the item to our list
        cart.append(food)
        print("Item added!")

# Show the full list of items at the end
print("You ordered:", cart)