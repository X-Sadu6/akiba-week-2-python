
# AKIBA BANK - Simple Bank Account System

balance = 1000
correct_pin = "1234"
attempts = 3
transactions = 0

# Step 1: PIN Authentication
while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")

        if attempts > 0:
            print("Attempts remaining:", attempts)

if attempts == 0:
    print("Too many incorrect attempts.")
    print("Your account is locked.")

else:
    # Step 2: Bank Menu
    while True:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        # Check Balance
        if choice == "1":
            print(f"Your current balance is: {balance} Birr")
            print("Transactions made:", transactions)

        # Deposit Money
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance += amount
                    transactions += 1
                    print("Deposit successful!")
                    print(f"Your new balance is: {balance:.2f} Birr")
                else:
                    print("Deposit amount must be greater than zero.")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        # Withdraw Money
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    transactions += 1
                    print("Withdrawal successful!")
                    print(f"Your new balance is: {balance:.2f} Birr")

            except ValueError:
                print("Invalid amount. Please enter a number.")

        # Exit
        elif choice == "4":
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            print("Total successful transactions:", transactions)
            break

        # Invalid Option
        else:
            print("Invalid option.")
            print("Please choose a valid option.")
