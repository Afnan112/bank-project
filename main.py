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
# #  End Wite Data from "data.csv" file to bank.csv

# ---- Start Add New Customer ----
class Customer:
    def __init__(self, account_id, first_name, last_name, password, balance_checking, balance_savings):
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


def create_new_customer():
    account_id = input("Enter your accound id: ")
    first_name = input("Enter your first name: ")
    last_name = input("Ener your last name: ")
    password = input("Enter your password: ")
    balance_checking = input("Enter your balance checking: ")
    balance_savings = input("Enter your balance savings: ")
    
    return Customer(account_id, first_name, last_name, password, balance_checking, balance_savings)
def write_to_csv(customer):
    with open('bank.csv', 'a', newline='') as csvfile:  
        writer = csv.writer(csvfile)    
        writer.writerow([customer.account_id, customer.first_name, customer.last_name, customer.password, customer.balance_checking, customer.balance_savings])  

customer1 = create_new_customer()
write_to_csv(customer1)
# ---- End Add New Customer ----