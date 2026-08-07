choice = input("1 THB -> USD, 2 USD -> THB: ")
amount = float(input("Amount: "))

if choice == "1":
    usd = amount / 35.5
    print(f"{amount:.2f} THB = {usd:.2f} USD")
    print("Formula: USD = THB / 35.5")
elif choice == "2":
    thb = amount * 35.5
    print(f"{amount:.2f} USD = {thb:.2f} THB")
    print("Formula: THB = USD * 35.5")
else:
    print("Invalid choice")