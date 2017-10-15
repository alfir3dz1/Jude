from Account import Account
class Customer():
    def __init__(self,firstName,lastName,Account):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__Account = Account
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def getAccount(self):
        return self.__Account
    def setAccount(self,account):
        self.__Account = account

a = ("Alfi", "Redzwan", 800)#Act as dictionary because it has no tuple, puts the first and last name and put account according to the new balance
print(a)
b = ("Taufiq", "Rohaimi", 400)#Act as dictionary because it has no tuple, puts the first and last name and put account according to the new balance
print(b)
c = ("Ali", "Redza", 940)#Act as dictionary because it has no tuple, puts the first and last name and put account according to the new balance
print(c)
