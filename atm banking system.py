balance = 5000

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Money deposited")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        
        if amount <= balance:
            balance -= amount
            print("Please collect cash")
        else:
            print("Insufficient balance")

    elif choice == 4:
        break