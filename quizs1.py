# quizs question 1


# Asking the user for the bill amount
bill = float(input("Enter the total bill amount in AED: "))

# Checking for the discount
if bill > 1000:
    # 20% discount
    discount = bill * 0.20
elif bill >= 500:
    # 10% discount
    discount = bill * 0.10
else:
    # No discount

    discount = 0

# Calculating the final price

final_price = bill - discount

# Showing the result

print("The final price to pay is:", final_price, "AED")