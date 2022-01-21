import os
import random as ra
users = [{'name':'atharsh','pass':'1234','id':'I1'}]
expense = dict()
paid_history = list()
def new_user():
    new_na = input("\nEnter New Name -> ")
    new_pass = input("Enter New Password -> ")
    new_id = 'I'+str(ra.randint(2,9))
    for i in users:
        if new_na in i['name']:
            print("\n\t Name Already exists...")
            input("\nPress Enter To Continue...")
        else:
            users.append({'name':new_na,'pass':new_pass,'id':new_id})
            print("\n\t   Account created successfully...\n\nYour Id is",new_id)
            input("\nPress Enter To Continue...")
            break
def adding_expense(name):
    ex_name = input("\nEnter Expense Name -> ")
    ex_amount = int(input("Enter Expense Amount -> "))
    no_of_mem = int(input("\nEnter No of members -> "))
    lis = {}
    for k in range(no_of_mem):
        a = input("\nEnter Member Name ->")
        b = input("Enter Member Id -> ")
        for l in users:
            if a==l['name'] and b==l['id']:
                if a==name:
                    c = 0
                    paid_history.append({name:(str(f"{name} Paid {ex_amount} on {ex_name}"))})
                else:     
                    c = round(ex_amount/no_of_mem,1)
                lis.update({a:c})
    if (len(lis))==0:
        input("\n  Invalid Account Details...")
    else:                  
        expense.update({ex_name:lis})
def current_expense():
    for m in expense:
        print(m,"\n")
    st = input("Enter Your Choice -> ")
    for n in expense:
        if st==n:
            for m in expense[n]:
                if expense[n][m]==0:
                    print(f"\n{m} paid {n}")
            for l in expense[n]:
                if expense[n][l]!=0 and expense[n][l]!='p':
                    print(f"\n\t{l} owes {expense[n][l]}")
                if expense[n][l]=='p':
                    print(f"\t{l} Fully settled up on {n}") 
    input("\n\tPress Enter to Continue...")
def settle_up(name):
    for m in expense:
        print(m,"\n")
    st = input("Enter Your Choice -> ")                 
    for n in expense:
        if st==n:
            for l in expense[n]:
                if expense[n][l]!=0 and l==name:
                    print(f"\t{l} owes {expense[n][l]}")
                    at = int(input("Enter Amount to settle up -> "))
                    expense[n][l] -= at
                    paid_history.append({name:str(f"{l} paid {st} of {at}")})
                    if expense[n][l]==0:
                        expense[n][l] = 'p'
                        paid_history.append({name:str(f"{l} fully settled on {st}")})
    input("\n\nPress Enter to Continue...") 

def activity(name):
    q=0
    ac=1
    for i in paid_history:
        for j in i:
            if j==name:
                print(f"\n{ac}) {i[j]}")
                ac+=1
        q+=1    
    input("\n Press Enter To Continue...")                 
                 
while(True):
    os.system("cls")
    print("\t    ---Welcome to Splitwise---\n")
    print("1) New User","2) Exsiting User","3) Exit\n",sep="\n")
    choice = int(input("Enter Your Choice -> "))
    if choice==1:
        os.system("cls")
        new_user()
    elif choice==2:
        os.system("cls")
        name = input("Enter Name -> ")
        passwrd = input("Enter Password -> ")
        for j in users:
            if name==j['name']:
                na = j['name']
                pa = j['pass']
                break
        if name==na and passwrd==pa:
            while(True):
                os.system("cls")
                print(f"\t   ---Welcome {name}---")
                print("\n1) New Expense\n2) My Expense\n3) settle Up\n4) Activity\n5) Exit\n")
                choice = int(input("Enter Your Choice -> "))
                if choice==1:
                    os.system("cls")
                    adding_expense(name)
                elif choice==2:
                    os.system("cls")
                    current_expense()
                elif choice==3:
                    os.system("cls")
                    settle_up(name)
                elif choice==4:
                    os.system("cls")
                    activity(name)
                elif choice==5:
                    break    
                else:
                    input("\n   Invalid Choice...")     

        else:
            input("\n\n\t Invalid Username Or Password")