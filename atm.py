balance = 5000

print("🏦 Welcome to Divya ATM")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your Balance is:", balance)

    elif choice == 2:
        deposit = int(input("Enter deposit amount: "))
        balance += deposit
        print("Deposit Successful ✅")
        print("New Balance:", balance)

    elif choice == 3:
        withdraw = int(input("Enter withdraw amount: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Withdraw Successful ✅")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance ❌")

    elif choice == 4:
        print("Thank you for using Divya ATM 🙌")
        break

    else:
        print("Invalid choice ❌ Try again!")
