class Account:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amt):
        self.__balance = self.__balance + amt
    def withdraw(self,amt):
        self.__balance = self.__balance - amt
    def getbalance(self):
        return self.__balance

a = Account(1200)
a.deposit(300)
a.withdraw(700)
print(a.getbalance())
b = Account(700)
b.deposit(200)
b.withdraw(500)
print(b.getbalance())
c = Account(600)
c.deposit(400)
c.withdraw(60)
print(c.getbalance())

