import csv  
class Customer:
    def __init__(self, account_id, first_name, last_name, password, balance_checking=0.0, balance_savings=0.0):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings
        self.overdraft_count = 0
        self.overdraft_fee = 53
        self.active = True
    
    def display_customer(self):
        print(f"Account ID: {self.account_id}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Password: {self.password}")
        print(f"Balance checking: {self.balance_checking}")
        print(f"Balance savings: {self.balance_savings}")

def overdraft_fee(self):
        # track the number of withdrals
        self.overdraft_count += 1
        if self.overdraft_count >= 2:
            self.active = False  
            # discount fee from balance_checking
        self.balance_checking -= self.overdraft_fee  

# ---- Start Add New Customer ----
def create_new_customer(account_id, first_name, last_name, password):
    account_id = input("Enter your accound ID: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your password: ")
    
    balance_checking = 0.0
    balance_savings = 0.0

    return Customer(account_id, first_name, last_name, password, balance_checking, balance_savings)

def write_to_csv(customer):
    with open('bank.csv', 'a', newline='') as csvfile:  
        writer = csv.writer(csvfile)    
        writer.writerow([customer.account_id, customer.first_name, customer.last_name, customer.password, customer.balance_checking, customer.balance_savings])  

def check_customer_exists(account_id, password):
                with open('bank.csv', 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row and row[0] == str(account_id) and row[3] == str(password):
                            return True
                return False
# ---- End Add New Customer ----
# ---- Start Deposit Money function for checking and savings -----
def deposit_to_accounts(account_id, deposit_amount, account_type):
    rows = []
    with open('bank.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # read all rows and store in row
        for row in reader:
            # check from the row is not empty 
            if row: 
                if row[0] == account_id:
                    if account_type == 'checking':
                        # balance_checking => [4]
                        row[4] = float(row[4]) + deposit_amount
                    elif account_type == 'savings':
                        row[5] = float(row[5]) + deposit_amount
            rows.append(row)
                                        
    with open('bank.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows) 
    return row
# ---- End Deposit Money function for checking and savings -----

# ---- Start Withdraw Money function for checking and savings -----
def withdraw_from_accounts(account_id, withdraw_amount, account_type):
    rows = []
    with open('bank.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row: 
                if row[0] == account_id:
                    if account_type == 'checking':
                        if float(row[4]) >= withdraw_amount:
                            row[4] = float(row[4]) - withdraw_amount
                        else:
                            print("Insufficient balance in checking account")
                    elif account_type == 'savings':
                        if float(row[5]) >= withdraw_amount:
                            row[5] = float(row[5]) - withdraw_amount
                        else:
                            print("Insufficient balance in savings account")
                    updated_row = row
                rows.append(row)
            else:
                rows.append(row)
                                        
    with open('bank.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows) 
    return updated_row 
# ---- End Withdraw Money function for checking and savings -----

# ---- Start transfer Money function  -----
def transfer_between_accounts(account_id, transfer_amount, from_account, to_account):
    rows = []
    with open('bank.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row: 
                if row[0] == account_id:
                    if from_account == 'checking' and float(row[4]) >= transfer_amount:
                        row[4] = float(row[4]) - transfer_amount
                    elif from_account == 'savings' and float(row[5]) >= transfer_amount:
                        row[5] = float(row[5]) - transfer_amount
                    else:
                        print("Insufficient balance in the from account")
                    # إضافة المبلغ إلى الحساب المستلم
                    if to_account == 'checking':
                        row[4] = float(row[4]) + transfer_amount
                    elif to_account == 'savings':
                        row[5] = float(row[5]) + transfer_amount
                rows.append(row)

    with open('bank.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
# ---- End transfer Money function  -----

print("\nWelcome to ACME Bank 💰")
while True:
        print("\n Choose an action:")
        print("1. Add new Customer")
        print("2. Login")

        choice = input("\nEnter your choice:").strip()
        
        if choice == '1':
            new_customer = create_new_customer('ccount_id', 'first_name', 'last_name','password')
            write_to_csv(new_customer)
            print("\nCustomer added successfully!\n")

        elif choice == '2':
            account_id = input("Enter your accound ID: ").strip()
            password = input("Enter your password: ").strip()

            if check_customer_exists(account_id, password):
                print('\nThe Customer aleread exists, you may proceed with the transactions\n')
            else:
                print("\nThe customer not exists, please click option '1' to register")
                continue
            choice = input("choose: Deposit, Withdraw, Transfer: ").lower()

            if choice == "deposit":
                    print("\n Choose the type of account:")
                    print("1. checking account")
                    print("2. savings account")
                    #print("3. both a checking and a savings account")

                    account_choice = input("\nEnter your choice: ")
                    
                    if account_choice == '1':
                                print("You selected a checking account.")
                                deposit_amount = float(input("\nEnter the deposit amount: "))
                                updated_checking = deposit_to_accounts(account_id, deposit_amount,'checking')
                                print(f"Deposited {deposit_amount} into checking account. New balance: {updated_checking[4]}")
                    elif account_choice == '2':
                        print("You selected a savings account.")
                        deposit_amount = float(input("\nEnter the deposit amount: "))
                        updated_savings = deposit_to_accounts(account_id, deposit_amount,'savings')
                        print(f"Deposited {deposit_amount} into checking account. New balance: {updated_savings[5]}")

            elif choice == "withdraw":
                    print("\n Choose the type of account:")
                    print("1. checking account")
                    print("2. savings account")

                    account_choice = input("\nEnter your choice: ")
                    
                    if account_choice == '1':
                                print("You selected a checking account.")
                                withdraw_amount = float(input("\nEnter the withdraw amount: "))
                                updated_checking = withdraw_from_accounts(account_id, withdraw_amount,'checking')
                                print(f"Withdraw {withdraw_amount} into checking account. New balance: {updated_checking[4]}")
                    elif account_choice == '2':
                        print("You selected a savings account.")
                        withdraw_amount = float(input("\nEnter the deposit amount: "))
                        updated_savings = withdraw_from_accounts(account_id, withdraw_amount,'savings')
                        print(f"Withdraw {withdraw_amount} into savings account. New balance: {updated_savings[5]}")    
            elif choice == "transfer":
                print("\n Choose the type of account to transfer from:")
                print("1. checking account")
                print("2. savings account")
                from_account_choice = input("\nEnter your choice: ")

                if from_account_choice == '1':
                    from_account = 'checking'
                elif from_account_choice == '2':
                    from_account = 'savings'

                transfer_amount = float(input("\nEnter the amount to transfer: "))

                print("\n Choose the type of account to transfer to:")
                print("1. checking account")
                print("2. savings account")
                to_account_choice = input("\nEnter your choice: ")

                if to_account_choice == '1':
                    to_account = 'checking'
                elif to_account_choice == '2':
                    to_account = 'savings'

                transfer_between_accounts(account_id, transfer_amount, from_account, to_account)
                print(f"Transferred {transfer_amount} from {from_account} to {to_account}.")

