# ---- Start Read Data from "data.csv" file ----
import csv  
    
# # opening the CSV file  
# with open('data.csv', mode ='r')as file:  
# # reading the CSV file  
#     csvFile = csv.reader(file)  
    
#     # displaying the contents of the CSV file  
#     for lines in csvFile:  
#         print(lines)  
# # ---- End Read Data from "data.csv" file ----

# # ---- Start Wite Data from "data.csv" file to bank.csv ----
# # Python program to demonstrate 
# # writing to CSV 
# fields = ['account_id', 'frst_name', 'last_name', 'password', 'balance_checking', 'balance_savings']    
# # data rows of csv file  
# rows = [ ['10001', 'suresh', 'sigera', 'juagw362', '1000', '10000'],  
#         ['10002', 'james', 'taylor', 'idh36%@#FGd', '10000', '10000'],  
#         ['10003', 'melvin', 'gordon', 'uYWE732g4ga1', '2000', '20000' ],  
#         ['10004', 'stacey', 'abrams', 'DEU8_qw3y72$', '2000', '20000'],  
#         ['10005', 'jake', 'paul', 'd^dg23g)@', '100000', '100000']]    

# filename = "bank.csv" 
# # writing to csv file  
# with open(filename, 'w') as csvfile:  
#     # creating a csv writer object  
#     csvwriter = csv.writer(csvfile)    
#     csvwriter.writerow(fields)
#     # writing the data rows  
#     csvwriter.writerows(rows) 
#  End Wite Data from "data.csv" file to bank.csv

# ---- Start Add New Customer ----
class Customer:
    def __init__(self, account_id, first_name, last_name, password, balance_checking=0.0, balance_savings=0.0):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings
    
    def display_customer(self):
        print(f"Account ID: {self.account_id}")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Password: {self.password}")
        print(f"Balance checking: {self.balance_checking}")
        print(f"Balance savings: {self.balance_savings}")

# ---- Start Add New Customer ----
def create_new_customer(account_id, first_name, last_name, password):
    account_id = input("Enter your accound ID: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your password: ")
    # balance_checking = float(input("Enter your balance checking: "))
    # balance_savings = float(input("Enter your balance savings: "))
    
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
# ---- Start Deposit Money for checking and savings -----
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

# ---- Start Withdraw Money for checking and savings -----
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
                            #return None
                    
                    updated_row = row
                rows.append(row)
            else:
                rows.append(row)
                                        
    with open('bank.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows) 
    return updated_row 
# ---- End Withdraw Money for checking and savings -----

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
            choice = input("choose: Deposit, Withdraw: ").lower()

            if choice == "deposit":
                    print("\n Choose the type of account:")
                    print("1. checking account")
                    print("2. savings account")
                    #print("3. both a checking and a savings account")

                    account_choice = input("\nEnter your choice: ")
                    
                    if account_choice == '1':
                                print("You selected a checking account.")
                                deposit_amount = float(input("\nEnter the deposit amount: "))
                                updated_row = deposit_to_accounts(account_id, deposit_amount,'checking')
                                print(f"Deposited {deposit_amount} into checking account.")
                    elif account_choice == '2':
                        print("You selected a savings account.")
                        deposit_amount = float(input("\nEnter the deposit amount: "))
                        updated_row = deposit_to_accounts(account_id, deposit_amount,'savings')
                        print(f"Deposited {deposit_amount} into checking account.")

            elif choice == "withdraw":
                    print("\n Choose the type of account:")
                    print("1. checking account")
                    print("2. savings account")

                    account_choice = input("\nEnter your choice: ")
                    
                    if account_choice == '1':
                                print("You selected a checking account.")
                                withdraw_amount = float(input("\nEnter the withdraw amount: "))
                                updated_row = withdraw_from_accounts(account_id, withdraw_amount,'checking')
                                print(f"Withdraw {withdraw_amount} into checking account.")
                    elif account_choice == '2':
                        print("You selected a savings account.")
                        withdraw_amount = float(input("\nEnter the deposit amount: "))
                        updated_row = withdraw_from_accounts(account_id, withdraw_amount,'savings')
                        print(f"Withdraw {withdraw_amount} into checking account.")

# ---- Start Deposit Money for checking and savings -----
    

