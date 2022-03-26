import os
Atm = {2000:1,500:0,200:0,100:0}
user = ['aaa','bbb']
UserCls = []
class UserClass:
    def __init__(self,name,password):
        self.name = name
        self.passwrd = password
        self.balance = 5000
        self.history = []
    def UserAthentication(self,name,passwrd):
        if name==self.name and passwrd==self.passwrd:
            return True
        else:
            return False
    def MoneyWithdrawal(self):
        amt = int(input("Available denominations are 2000,500,200,100\nEnter amount -> "))
        p = amt
        N_Count = {2000:0,500:0,200:0,100:0}
        while(p>=2000 and Atm[2000]!=0):
            p-=2000
            N_Count[2000]+=1
            Atm[2000]-=1
        while(p>=500 and Atm[500]!=0):
            p-=500
            N_Count[500]+=1
            Atm[500]-=1
        while(p>=200 and Atm[200]!=0):
            p-=200
            N_Count[200]+=1
            Atm[200]-=1
        while(p>=100 and Atm[100]!=0):
            p-=100
            N_Count[100]+=1
            Atm[100]-=1
        if p==0:
            if self.balance>=amt:
                print("\nAmount Withdrawed successfully\n")
                self.balance-=amt
                self.history.append(f"Amount withdrawed -> {amt}")
                for i in N_Count:
                    print(f"    {i} -> {N_Count[i]}")
                input("\n\n\tPress Enter to continue")
            else:
                input("\nLess Balance\n\n\tPress Enter to continue ")
        else:
            Atm[100]+=N_Count[100]
            Atm[200]+=N_Count[200]
            Atm[500]+=N_Count[500]
            Atm[2000]+=N_Count[2000]
            input("\nAmount not available  -  Enter Correct denomination\n\n\tPress Enter to continue ")
    def ShowBalance(self):
        print("\n\n Current Balance is",self.balance)
        input("\n\n\tPress Enter to continue")
    def DepositMoney(self):
        Msum = 0
        print("\nEnter Denominations : \n")
        for i in Atm:
            a = int(input(f" {i} -> "))
            Msum+=(a*i)
            Atm[i]+=a
        print("\nSum amount",Msum)
        self.balance+=Msum
        if Msum!=0:
            self.history.append(f"Amount deposited -> {Msum}")
        input("\nAmount Deposited successfully\n\n\tPress Enter to continue ")
    def MoneyTransfer(self):
        print("\tIMPS")
        name = input("\nEnter account name -> ")
        amt = int(input("Enter Amount -> "))
        if name in user:
            passwr = input("\nEnter Password for transaction -> ")
            if passwr==self.passwrd:
                ind = user.index(name)
                if self.balance>amt:
                    self.balance-=amt
                    UserCls[ind].balance+=amt
                    self.history.append(f"Amount Transfered to {UserCls[ind.name]} -> {amt}")
                    UserCls[ind].history.append(f"Amount Received from {self.name} -> {amt}")
                    input("\nAmount transfered Successfully\n\n\tPress Enter to continue")
                else:
                    input("\nInsufficient Balance\n\ntPress Enter to continue ")
            else:
                input("\nIncorrect password\n\n\tPress enter to continue ")
        else:
            input("\nName does not exist\n\n\tPress enter to continue")
    def UserHistory(self):
        print("\tUser History\n")
        print(*self.history,sep="\n")
        input("\n\n\tPress enter to continue ")
def AdminShowMoney():
    for i in Atm:
        print(f"  {i}  ->  {Atm[i]}")
    input("\n\n\tPress Enter to continue ")
def AdminDepositMoney():
    print("Enter no of Notes : ")
    for i in Atm:
        notes = int(input(f"Enter no of {i} Notes -> "))
        Atm[i]+=notes
    input("\nAmount deposited in ATM Sucessfully\n\n\tPress Enter to continue ")
def NewUser():
    name = input("Enter new name -> ")
    passwrd = input("Set new password -> ")
    if name in user:
        input("\nName already exists\n\n\tPress Enter to continue ")
    else:
        UserCls.append(UserClass(name,passwrd))
        input("\nUser Created Successfully...\n\n\tPress Enter to continue ")
UserCls.append(UserClass('aaa','111'))
UserCls.append(UserClass('bbb','222'))
while(True):
    os.system('cls')
    print('\tWelcome to Atm')
    choice = input('\n1) Admin login   2) User login   3) Exit\n\n Enter your choice -> ')
    if choice=='1':
        os.system('cls')
        name = input('Enter Admin name -> ')
        passwrd = input('Enter Admin pass -> ')
        if name=='admin' and passwrd=='111':
            while(True):
                os.system('cls')
                choice = input('\n1) Show money  2) Deposit money   3) Logout\n\nEnter your choice -> ')
                if choice=='1':
                    os.system('cls')
                    AdminShowMoney()
                elif choice=='2':
                    os.system('cls')
                    AdminDepositMoney()
                elif choice=='3':
                    break
                else:
                    input("\nInvalid choice...\n\n\tPress enter to continue ")
        else:
            input('\nInvalid user credentials...\n\n\tPress enter to continue ')
    elif choice=='2':
        os.system('cls')
        print('\tWelcome User ')
        choice = input("\n1) Exsisting User   2) New User   3) Exit\n\n Enter your choice -> ")
        if choice=='1':
            os.system('cls')
            name = input("Enter Name -> ")
            passwrd = input("Enter Password -> ")
            if name in user:
                ind = user.index(name)
                if UserCls[ind].UserAthentication(name,passwrd):
                    while(True):
                        os.system('cls')
                        print("\tWelcome back",name)
                        choice = input("\n1) Money Withdrawal   2) Balance Check\n3) Money Transfer   4) Deposit\n5) History   6) Logout\n\nEnter your choice -> ")
                        if choice=='1':
                            os.system('cls')
                            UserCls[ind].MoneyWithdrawal()
                        elif choice=='2':
                            os.system('cls')
                            UserCls[ind].ShowBalance()
                        elif choice=='3':
                            os.system('cls')
                            UserCls[ind].MoneyTransfer()
                        elif choice=='4':
                            os.system('cls')
                            UserCls[ind].DepositMoney()
                        elif choice=='5':
                            os.system('cls')
                            UserCls[ind].UserHistory()
                        elif choice=='6':
                            break
                        else:
                           input("\nInvalid choice...\n\n\tPress enter to continue ") 
                else:
                    input("\nName or password is incorrect\n\n\tPress Enter to continue ")
            else:
                input("\nName does not exists\n\n\tPress Enter to continue ")
        elif choice=='2':
            os.system('cls')
            NewUser()
        elif choice=='3':
            break
        else:
            input("\nInvalid choice...\n\n\tPress enter to continue ")          
    elif choice=='3':
        break
    else:
        input("\nInvalid choice...\n\n\tPress enter to continue ")