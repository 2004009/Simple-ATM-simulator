class ATM:
    def __init__(self, pin):
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return amount

    def balance_check(self):
        return self.balance

def main():
    pin = 1311
    enter_pin = int(input("Enter the pin: "))
    if pin == enter_pin:
        atm = ATM(pin)
        while True:
            print("\nATM Menu")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = int(input("Enter the amount to deposit: "))
                new_balance = atm.deposit(amount)
                print(f"Total amount deposited: {amount}")
                print(f"New balance: {new_balance}")

            elif choice == 2:
                amount = int(input("Enter the amount to withdraw: "))
                result = atm.withdraw(amount)
                if result == "Insufficient funds":
                    print(result)
                else:
                    print(f"Total amount withdrawn: {result}")
                    print(f"Remaining balance: {atm.balance_check()}")

            elif choice == 3:
                print(f"Total Balance: {atm.balance_check()}")

            elif choice == 4:
                print("Exiting... Thank you!")
                break

            else:
                print("Invalid choice! Please try again.")

    else:
        print("ERROR: Invalid PIN")

if __name__ == "__main__":
    main()

