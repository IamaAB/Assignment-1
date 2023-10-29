print(" ------------------------------------------------------------------------------")
print(" |                                                                             | ")
print(" |                         Bank Account Management System                      |")
print(" |                                                                             | ")
print(" ------------------------------------------------------------------------------")
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs {amount}. \nNew balance: Rs {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs {amount}. \nNew balance: Rs {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def calculate_interest(self):
        pass  # To be implemented in subclasses

    def deduct_transaction_fee(self):
        pass  # To be implemented in subclasses

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest calculated and added. New balance: Rs {self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, transaction_fee=1):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        if self.balance >= self.transaction_fee:
            self.balance -= self.transaction_fee
            print(f"Transaction fee deducted. New balance: Rs {self.balance}")
        else:
            print("Insufficient funds to deduct the transaction fee.")

class BankCustomer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.savings_account = None
        self.checking_account = None

    def create_savings_account(self, account_number, initial_balance=0, interest_rate=0.03):
        self.savings_account = SavingsAccount(account_number, initial_balance, interest_rate)
        print(f"Savings account created for {self.customer_name}")

    def create_checking_account(self, account_number, initial_balance=0, transaction_fee=1):
        self.checking_account = CheckingAccount(account_number, initial_balance, transaction_fee)
        print(f"Checking account created for {self.customer_name}")

    def display_customer_details(self):
        print("\n--------------------------------------------------------")
        print("Customer Details:")
        print(f"Customer Name: {self.customer_name}")
        print("--------------------------------------------------------")
        if self.savings_account:
            print("Savings Account Details:")
            print(f"Account Number: {self.savings_account.account_number}")
            print(f"Balance: Rs {self.savings_account.balance}")
            print(f"Interest Rate: {self.savings_account.interest_rate}")
            print("--------------------------------------------------------")
        if self.checking_account:
            print("Checking Account Details:")
            print(f"Account Number: {self.checking_account.account_number}")
            print(f"Balance: Rs {self.checking_account.balance}")
            print(f"Transaction Fee: Rs {self.checking_account.transaction_fee}")

if __name__ == '__main__':
    customer_name = input("Enter your name: ")
    customer = BankCustomer(customer_name)

    while True:
        print("\nOptions:")
        print("1. Create Savings Account")
        print("2. Create Checking Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Calculate Interest (Savings Account)")
        print("6. Deduct Transaction Fee (Checking Account)")
        print("7. Display Customer Details")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter Savings Account Number: ")
            initial_balance = float(input("Enter initial balance: "))
            customer.create_savings_account(account_number, initial_balance)
        elif choice == "2":
            account_number = input("Enter Checking Account Number: ")
            initial_balance = float(input("Enter initial balance: "))
            customer.create_checking_account(account_number, initial_balance)
        elif choice == "3":
            amount = float(input("Enter deposit amount: "))
            if customer.savings_account:
                customer.savings_account.deposit(amount)
            else:
                customer.checking_account.deposit(amount)
        elif choice == "4":
            amount = float(input("Enter withdrawal amount: "))
            if customer.savings_account:
                customer.savings_account.withdraw(amount)
            else:
                customer.checking_account.withdraw(amount)
        elif choice == "5":
            if customer.savings_account:
                customer.savings_account.calculate_interest()
            else:
                print("No savings account found.")
        elif choice == "6":
            if customer.checking_account:
                customer.checking_account.deduct_transaction_fee()
            else:
                print("No checking account found")
        elif choice == "7":
            customer.display_customer_details()
        elif choice == "8":
            print("Bye Bye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
