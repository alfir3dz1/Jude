from Customer import Customer
from Account import Account
from Bank import Bank

#Note that the info is already added, determine the name Bank where it placed
def main():
    Start()

def Start():
    print("1. Bank ")
    print("2. Quit")
    option = int(input("Choose 1 or 2"))
    if  option==1:
        InBank()
    else:
        exit()

def InBank():
    sdf = input("Bank: ")
    print(sdf)
#That's the end of the command because in the previous file, i add the command manually








main()
