from Customer import Customer
from Account import Account
class Bank():
    customer = []
numberOfCustomer = 0
bankName = ""
def __init__(self,bankName):
    self.__bankName = bankName
def addCustomer(self, firstName, lastName):
    self.__customer.append(Customer(firstName, lastName, Account(0)))
    self.__numberOfCustomer =+1
def getNumofCustomer(self):
    return self.__numOfCustomer
def getCustomer(self):
    return self.__customer
customer = ["There were total of 3 customers in the bank"]
print(customer)#This is how I count and add the number of customers manually

