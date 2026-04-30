# Quizs Question 4


# Set the secret PIN
secret_pin = "1234"

# Give the user 3 attempts
for attempt in range(3):
    user_entry = input("Please enter your 4-digit PIN: ")
    
    # Check if the PIN is correct
    if user_entry == secret_pin:
        print("Access Granted")
        break  # Exit the loop if correct
    else:
        print("Wrong PIN. Try again.")
else:
    # This part runs only if the loop finishes 3 times without breaking
    print("Account Locked")