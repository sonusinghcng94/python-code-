# Quiz Question 3


# Using float() to allow decimal numbers like 1.5 hours
price_per_hour = 10.0

hours = float(input("How many hours do you want to park? "))

# Checking the limit
if hours > 4:
    print("Error: Maximum stay is 4 hours")
elif hours <= 0:
    print("Error: Please enter a valid time.")
else:
    # Calculating total cost 
    total_cost = hours * price_per_hour
    print(f"For {hours} hours, your total price is: {total_cost:.2f} AED")