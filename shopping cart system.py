cart = {}

while True:
    print("\n1.Add Product")
    print("2.View Cart")
    print("3.Total Bill")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        price = int(input("Enter price: "))
        cart[product] = price
        print("Product added")

    elif choice == 2:
        print(cart)

    elif choice == 3:
        total = sum(cart.values())
        print("Total Bill:", total)

    elif choice == 4:
        break