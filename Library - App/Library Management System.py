#Library Management System - Mini Application

import os
import random as rd
users = {'atharsh':'1234','ashwin':'1234'}
us = ['atharsh']
admin_his = list()
books = [{'name':'dictinory','count':2,'id':'B4'},{'name':'tamil','count':5,'id':'B2'},{'name':'english','count':4,'id':'B7'}]
def adding_books():
    b_nam = input("\n Enter Name of the book -> ")
    b_cnt = int(input(" Enter No of count -> "))
    b_id = 'B'+str(rd.randint(10,100))
    books.append({'name':b_nam,'count':b_cnt,'id':b_id})
    input("\n\n   Book Added Successfully...")
def adding_counts():
    q=1
    for i in books:
        print(f"{q})  {i['name']} -> {i['count']}")
        q+=1
    na = input("\nEnter Name Of book -> ")
    co = int(input("Enter counts to add -> "))
    for i in books:
        if i['name']==na:
            i['count']+=co       
    input("\n\n   Books Count added Successfully...")
def removing_books():
    q=1
    for i in books:
        print(f" {q})  {i['name']}")
        q+=1
    na = input("\nEnter Name of the book to remove -> ")
    q=0
    no_count =0
    for i in books:
        if i['name']==na:
            books.pop(q)
            print("   Book Removed Successfully...")
        if i['name']!=na:
            no_count+=1
        q+=1
    if no_count==len(books):
        print("\n\t   No Books Available...\n")        
    input("\nPress Enter to Continue...")
def viewing_books():
    q=1
    for i in books:
        print(f"\n{q})  Name -> {i['name']}\n    count -> {i['count']}\n    Book ID -> {i['id']}")
        print("\t   -----------")
        q+=1
    input("\n\n   Press Enter to Continue...")    
def reports():
    q=1
    for i in admin_his:
        print(f"{q}) {i}")
        q+=1
    input("\n\n Press Enter to continue...")   
def new_user():
    new_name = input("\nEnter Name -> ")
    new_pass = input("Enter New Password -> ")
    if new_name in users:
        print("\n   Name Already Exists...")
        input("\n\n   Press Enter to Continue...")
    else:
        users.update({new_name:new_pass})
        us.append(new_name)
        print("\n   User Created Successfully")
        input("\n\n   Press Enter to Continue...")
class user:
    def __init__(self):
        self.book = list()
        self.cart = list()

    def adding_cart(self,name):
        self.cart.append(name)
        input("\n\n   Book added to cart...")

    def my_cart(self):
        q=1
        for i in self.cart:
            print(f"{q})  {i}")
            q+=1
        print("\n1) Checkout\n2) Remove Book\n3) Exit")    
        choice = input("\nEnter Your Choice -> ")
        return choice

    def remove_cart(self):
        q=0
        na = input("\nEnter Name of book to remove from cart -> ")
        for i in self.cart:
            if na==i:
                self.cart.pop(q)
                input('\n\nBooked removed Successfully...')
            q+=1    
    
    def checkout(self):
        na_count = 0
        b_count = 0
        for i in self.cart:
            if len(self.book)<2:
                self.book.append(i)
                admin_his.append(str(f"{name} Borrowed {i} Book from Library"))
                b_count+=1
            else:
                na_count +=1      
        if na_count!=0:
            print("\n\t You have already exceed the limit of borrowing\n\t\tPlease Return Books In time...")             
        print(f"\n{b_count} Borowed Buyed Successfully...")
        input("\n\tpress Enter to continue...")

    def return_books(self):
        nas = input("Enter the Name of book -> ")
        nai = input("Enter Book ID -> ")
        for i in books:
            if i['name']==nas and i['id']==nai:
                q=0
                for j in self.book:
                    if j==nas:
                        self.book.pop(q)
                        admin_his.append(str(f"{name} Returned {j} Book To library..."))
                        print("\n\tBook returned Successfully...\nThanky You For using library")
                        input()
                    q+=1
        input("\n\n   Press enter to continue...")                   


def search_book():
    na = input("\n Enter Name of book to search -> ")
    no_count =0
    for i in books:
        if i['name']==na:
            print(f"\n\n\t  Book Name : {i['name']}\n\t  Book ID : {i['id']}\n\t   No of Books available in Library : {i['count']}")
        else:
            no_count+=1
    if no_count==len(books):
        print("\n\n\t  Book Not Available...")
    print("\n\n1) Add Book to cart\n2) Exit")
    choice = input("\nEnter Your Choice -> ")
    return na,choice         

while(True):
    os.system("cls")
    print("\t   ---Wlecome to Library---\n")
    print("1) Admin\n2) User\n3) Exit\n")
    choice = input("Enter Your Choice -> ")
    if choice=='3':
        break
    elif choice=='2':
        while(True):
            os.system('cls')
            print("\t   ---Welcome to User Login---\n")
            print("1) New User\n2) Existing User\n3) Exit\n")
            choice = input("Enter Your Choice -> ")
            if choice=='3':
                break
            elif choice=='2':
                os.system("cls")
                name = input("\nEnter Name -> ")
                passwrd = input("Enter Password -> ")
                q=0
                for i in us:
                    if i==name:
                        a = q
                    q+=1
                us[a] = user()    
                if(name in users and passwrd==users[name]):
                    while(True):
                        os.system("cls")
                        print("\t   ---Welcome user---")
                        print("1) Search Books\n2) My Cart\n3) Return Books\n4) Logout")
                        choice = input("Enter Your Choice -> ")
                        if choice=='4':
                            break
                        elif choice=='3':
                            os.system("cls")
                            us[a].return_books()
                        elif choice=='2':
                            os.system("cls")
                            choice = us[a].my_cart()
                            if choice=='1':
                                os.system("cls")
                                us[a].checkout()
                            elif choice=='2':
                                us[a].remove_cart()
                            elif choice=='3':
                                continue
                            else:
                                input("\n\t  Invalid choice...")
                        elif choice=='1':
                            os.system("cls")
                            na,choice = search_book()
                            if choice=='2':
                                continue
                            elif choice=='1':
                                us[a].adding_cart(na)
                            else:
                                input("\n\t  Invalid choice...")
                        else:
                            input("\n\t  Invalid choice...")
                else:
                    input("\n\n\t   Invalid Username or password...")    
            elif choice=='1':
                os.system("cls")
                new_user()
            else:
                input("\n\n\t   Invalid Choice...")
    elif choice=='1':
        os.system("cls")
        ad = input("Enter Email -> ")
        pas = input("Enter Password -> ")
        if ad=='admin' and pas=='1234':
            while(True):
                os.system("cls")
                print("\t   ---Welcome Admin---\n")
                print("1) Add books\n2) Modify Book Counts\n3) Remove Books\n4) View Books\n5) Reports\n6) Exit\n")
                choice = input("Enter Your Choice -> ")
                if choice=='6':
                    break
                elif choice=='5':
                    os.system("cls")
                    reports()
                elif choice=='4':
                    os.system("cls")
                    viewing_books()
                elif choice=='3':
                    os.system("cls")
                    removing_books()
                elif choice=='2':
                    os.system("cls")
                    adding_counts()
                elif choice=='1':
                    os.system("cls")
                    adding_books()
                else:
                    input("\n\tInvalid Choice...")
        else:
            input("\n\n\t   Invalid Username or password...")            
    else:
        input("\n\tInvalid Choice...")    
