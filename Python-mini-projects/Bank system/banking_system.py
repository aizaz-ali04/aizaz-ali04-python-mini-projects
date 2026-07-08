class BankAccount:
    acc_counter = 1000   # class variable for auto account number

    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__balance = balance
        self.__pin = pin
        BankAccount.acc_counter += 1
        self.account_no = BankAccount.acc_counter

    def check_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount > 0: 
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, receiver):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.__balance -= amount
            receiver.__balance += amount
            print("Transfer successful")

accounts = []


def find_account(acc_no):
    for acc in accounts:
        if acc.account_no == acc_no:
            return acc
    return None


while True:
    print("\n--- BANK SYSTEM ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        pin = input("Set 4-digit PIN: ")
        acc = BankAccount(name, pin)
        accounts.append(acc)
        print("Account created successfully!")
        print("Your Account Number:", acc.account_no)

    elif choice == "2":
        acc_no = int(input("Enter account number: "))
        pin = input("Enter PIN: ")

        user = find_account(acc_no)

        if user and user.check_pin(pin):
            print("Login successful!")

            while True:
                print("\n--- ACCOUNT MENU ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transfer Money")
                print("5. Logout")

                ch = input("Enter choice: ")

                if ch == "1":
                    amt = float(input("Enter amount: "))
                    user.deposit(amt)

                elif ch == "2":
                    amt = float(input("Enter amount: "))
                    user.withdraw(amt)

                elif ch == "3":
                    print("Balance:", user.get_balance())

                elif ch == "4":
                    recv_no = int(input("Enter receiver account number: "))
                    receiver = find_account(recv_no)

                    if receiver:
                        amt = float(input("Enter amount: "))
                        user.transfer(amt, receiver)
                    else:
                        print("Receiver not found")

                elif ch == "5":
                    print("Logged out")
                    break

                else:
                    print("Invalid choice")

        else:
            print("Invalid account number or PIN")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice")


