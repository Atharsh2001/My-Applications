
import os
def show_money():
    for j in amount:
        print(j,"-->",amount[j])
    input("\nEnter to Continue...")   
def deposit_money():
    for i in amount:
        n = int(input("Enter "+str(i)+" Notes : "))
        amount[i]+=n
    input("\tAmount Added Succesfully...")
def pin_change():
    pin_name = input("Enter name :")
    new_pin = int(input("Enter New pin :"))
    useracc[pin_name] = new_pin
    input("\tPin changed Succesfully...")
def balance_info(user_name):
    print("\tyour current balance is",userbalan[user_name]) 
    input("\t  Press Enter to continue...")  

def withdraw(user_name):
    p=int(input("The available notes are 100,200,500,2000\nEnter amount for withdrawal :"))
    h = p
    twothou_count = 0
    fivehun_count = 0
    hund_count = 0
    two_count = 0
    while(p>=2000 and amount[2000]!=0):
        p -= 2000
        twothou_count +=1
        amount[2000] -= 1
    while(p>=500 and amount[500]!=0):
        p -= 500
        fivehun_count +=1
        amount[500] -= 1
    while(p>=200 and amount[200]!=0):
        p -= 200
        two_count +=1
        amount[200] -= 1
    while(p>=100 and amount[100]!=0):
        p -= 100
        hund_count +=1
        amount[100] -= 1
    if p==0:    
        print("2000 Notes ->",twothou_count)
        print("500 Notes ->",fivehun_count)
        print("200 Notes ->",two_count)
        print("100 Notes ->",hund_count)
        userbalan[user_name]-=p
        ("\n\tAmount Withdrawed Successfully...")
        input("\t\nPress Enter to continue...")
        u_history.append(str(f"Amount Withdrawed - {h}"))

    else:
        amount[2000]=twothou_count
        amount[500]=fivehun_count
        amount[100]=hund_count
        amount[200]=two_count
        print("\t Amount Not Available...")
        input("\n\tpress enter to continue...")       

def money_transfer(name):
    tr_name =input("Enter Account Name to transfer -> ")
    tr_amount = int(input("Enter Amount To Transfer ->"))
    tr_count = 0
    if tr_count<=3 and tr_amount<=10000:
        if tr_name in useracc:
            userbalan[tr_name] += tr_amount
            userbalan[name] -= tr_amount
            print("\n\t  Amount Transfered Successfully...\n")
            input("Press Enter to Continue")
            tr_count+=1
            u_history.append(str(f"Amount transfered to {tr_name} - {tr_amount}"))
        else:
            input("\n\t  Invalid user name...")    
    else:
        print("\n\t Reached Limit...")
        input("\n\t   Press Enter to continue")
def mini():
    for l in history:
        if user_name==l:
            lis=history[l]
            for j in lis:
                print(j)
    input("\n\t Press Enter to continue")            

useracc = {'atharsh':1234,'ashwin':1234,'sathish':1234}
userbalan = {'atharsh':30000,'ashwin':25000,'sathish':40000}       
amount = {100:0,200:0,500:2,2000:0}
history = dict()
u_history = list()
while(True):
    os.system("cls")
    print("\tWelcome to SBI ATM!!!\n")
    print("1) Admin Login \n2) Customer Login \n3) Exit\n")
    choice = int(input("Enter your choice -> "))
    if choice==3:
        exit()
    elif choice==2:
        os.system("cls")
        print("\tWelcome user...\n")
        user_name = input("Enter User Name :")
        user_pass = int(input("Enter your Password :"))
        if(user_name in useracc and user_pass==useracc[user_name]):
            while(True):
                os.system("cls")
                print(f"\t   Welcome {user_name}\n")   
                print("1) Cash Withdraw\n2) Balance Check\n3) Pin Change\n4) Money Transfer\n5) Mini Statement\n6) Exit")
                user_choice = int(input("Enter Your choice :"))
                os.system('cls')
                if choice==6:
                    break
                elif user_choice==5:
                    os.system("cls")
                    history.update({user_name:u_history})
                    mini()
                if user_choice==4:
                    os.system("cls")
                    money_transfer(user_name)
                elif user_choice==3:
                    os.system("cls")
                    pin_change()
                elif user_choice==2:
                    os.system("cls")
                    balance_info(user_name)
                elif user_choice==1:
                    os.system("cls")
                    withdraw(user_name)
                else:
                    input("\tInvalid choice...")          
    elif choice==1:
        os.system("cls")
        print("\tWelcome Admin..\n")
        username = input("Enter Username:")
        password = input("Enter Password:")
        if username=="admin" and password=="1234":
            while(True):
                os.system("cls")
                print("1) Deposit \n2) Show Money \n3) Exit\n")
                admin_choice = int(input("Enter Your Choice -> "))
                if admin_choice==3:
                    break  
                elif admin_choice==2:
                    os.system("cls")
                    show_money() 
                elif admin_choice==1:
                    os.system("cls")
                    deposit_money()    
                else:
                    input("\tInvalid Choice...")    
        else:
            input("\tInvalid Username or Password")
    else:
        input("\tInvalid choice...")        
            
        
        

