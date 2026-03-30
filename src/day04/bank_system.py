# Day 4 - Mini Project 2: Bank Account System
# Practice: Classes, Inheritance, and Magic Methods
#
# GOAL: Build a simple bank that lets customers open accounts,
#       deposit/withdraw money, and check balances.
#
# CLASSES TO BUILD:
#   Account          -> base class for all account types
#   SavingsAccount   -> inherits Account, adds interest
#   CheckingAccount  -> inherits Account, allows overdraft
#   Bank             -> manages all accounts and customers


# ============================================================
# Class 1: Account (Base Class)
# ============================================================
class Account:
    # Class variable: track how many accounts have been created
    # HINT: use this to auto-generate account numbers like "ACC001"
    total_accounts = 0

    def __init__(self, owner_name, initial_deposit=0):
        Account.total_accounts += 1
        self.account_number = f"ACC{Account.total_accounts:03d}"
        self.owner_name = owner_name
        self.balance = initial_deposit
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount should be greater than 0")
            return False
        self.balance += amount;
        self.transactions.append({"type": "deposit", "amount": amount})
        return True

    def withdraw(self, amount):
        # TODO: validate amount > 0
        # TODO: check there are sufficient funds (balance >= amount)
        # TODO: deduct amount from self.balance
        # TODO: record the transaction
        # TODO: return True on success, False on failure
        pass

    def get_balance(self):
        # TODO: return self.balance
        pass

    def print_statement(self):
        # TODO: print a mini statement showing all transactions
        # HINT: loop over self.transactions and print each one
        print(f"\n--- Statement for {self.account_number} ({self.owner_name}) ---")
        # ... your code here ...

    def __str__(self):
        # TODO: return a readable string, e.g.:
        # "ACC001 | Alice Johnson | Balance: $500.00"
        pass

    def __repr__(self):
        # TODO: return a developer-friendly string, e.g.:
        # "Account(account_number='ACC001', owner='Alice Johnson', balance=500.0)"
        pass


# ============================================================
# Class 2: SavingsAccount (inherits Account)
# ============================================================
class SavingsAccount(Account):
    def __init__(self, owner_name, initial_deposit=0, interest_rate=0.03):
        super().__init__(owner_name, initial_deposit)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest: ${interest:.2f}")

    def __str__(self):
        # "ACC002 | Bob Smith | Balance: $1000.00 | Interest: 3.0%"
        return f"{self.account_number} | {self.owner_name} | Balance: ${self.balance:.2f} | Interest: {self.interest_rate*100:.1f}%"


# ============================================================
# Class 3: CheckingAccount (inherits Account)
# ============================================================
class CheckingAccount(Account):
    def __init__(self, owner_name, initial_deposit=0, overdraft_limit=200):
        super().__init__(owner_name, initial_deposit)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # TODO: override withdraw to allow going negative,
        #       but only down to -self.overdraft_limit
        if amount <= 0:
            print("Withdrawal amount should be greater than 0")
            return False
        if self.balance - amount < -self.overdraft_limit:
            print("Insufficient funds (overdraft limit reached)")
            return False
        self.balance -= amount
        self.transactions.append({"type": "withdraw", "amount": amount})
        return True

    def __str__(self):
        # "ACC003 | Carol White | Balance: $-50.00 | Overdraft limit: $200"
        return f"{self.account_number} | {self.owner_name} | Balance: ${self.balance:.2f} | Overdraft limit: ${self.overdraft_limit}"


# ============================================================
# Class 4: Bank
# ============================================================
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []   # list of Account objects

    def open_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} opened for {account.owner_name}")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def list_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
            return
        for account in self.accounts:
            print(f"")

    def total_deposits(self):
        # HINT: use a loop or the built-in sum() with a generator
        return sum(account.balance for account in self.accounts)

    def __str__(self):
        return f"{self.name} | {len(self.accounts)} accounts | Total deposits: ${self.total_deposits():.2f}"


# ============================================================
# Main Program
# ============================================================
bank = Bank("City Bank")

# --- Seed some accounts ---
# HINT: create 2-3 accounts of different types and open them
# e.g.
# alice_savings = SavingsAccount("Alice Johnson", initial_deposit=500)
# bank.open_account(alice_savings)
# ... add more ...


print()

# --- Menu loop ---
while True:
    print("\n--- Bank Menu ---")
    print("1. List accounts")
    print("2. Open new account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check balance")
    print("6. Print statement")
    print("7. Apply interest (savings accounts)")
    print("8. Exit")

    choice = input("\nEnter choice (1-8): ")

    if choice == "1":
        bank.list_accounts()

    elif choice == "2":
        owner_name = input("Owner Name: ")
        account_type = input("Account Type (savings/checking): ")
        initial_deposit = float(input("Deposit Amount: "))  # ← float, not string

        if account_type == "savings":
            account = SavingsAccount(owner_name, initial_deposit)
        elif account_type == "checking":
            account = CheckingAccount(owner_name, initial_deposit)
        else:
            print("Invalid account type")
            continue   # ← go back to the menu

        bank.open_account(account)

    elif choice == "3":
        account_number = input("Account number: ")
        amount = float(input("Deposit amount: "))
        account = bank.find_account(account_number)
        if account:
            if account.deposit(amount):
                print("Deposit successful!")
            else:
                print("Deposit failed.")
        else:
            print("Account not found.")

    elif choice == "4":
        # TODO: ask for account number, then amount
        # TODO: find account and call account.withdraw(amount)
        pass

    elif choice == "5":
        # TODO: ask for account number
        # TODO: find account and print its balance
        pass

    elif choice == "6":
        # TODO: ask for account number
        # TODO: find account and call account.print_statement()
        pass

    elif choice == "7":
        # TODO: loop through bank.accounts
        # TODO: if the account is an instance of SavingsAccount, call apply_interest()
        # HINT: use isinstance(account, SavingsAccount)
        pass

    elif choice == "8":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")


# BONUS: Add a transfer(from_account, to_account, amount) method to Bank
# BONUS: Save/load accounts to a JSON file
# BONUS: Add a fixed deposit account type with a lock-in period
