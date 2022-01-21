# Vehicle Rental System - Mini Application

import os
import random as rd
vehicles = [{'type':'bike','name':'bullet','id':'V1','rate':50,'stock':3},{'type':'car','name':'audi','id':'V2','rate':120,'stock':1}]
history = list()
users = {'atharsh':'1234','ashwin':'1234'}
user_vech = {'atharsh':'none'}
cart = list()
def view_vechile():
    q=1
    for i in vehicles:
        print(f"{q}) Name -> {i['name']}\n   ID -> {i['id']}\n   Rate/Km -> {i['rate']}")
        q+=1
        print("\t   ----------\n")
    input("\n\n  Press Enter to continue...")
def add_vechicle():
    ty = input("Enter Type of vehicle -> ")
    na = input("Enter Name of Vehicle -> ")
    vid = "V"+str(rd.randint(3,10))
    ra = int(input("Enter Rate per kilometer -> "))
    st = int(input("Enter no of stocks -> "))
    vehicles.append({'type':ty,'name':na,'id':vid,'rate':ra,'stock':st})
    input("\n\n\t   Vehicle Added Successfully... ")
def remove_vehicle():
    q=1
    for i in vehicles:
        print(f"{q}) {i['name']}")
        q+=1
    nam = input("\nEnter Name to remove -> ")
    co=0
    si = len(vehicles)
    for j in range(len(vehicles)):
        if vehicles[j]['name']==nam:
            vehicles.pop(j)
            print("\n\n   Vehicle removed Successfully...")
            break
        else:
            co+=1
    if co==si:
        input("\n   Vechicle not found...")
    else:
        input("\n\n   Press Enter to continue")       
def view_history():
    q=1
    for i in history:
        print(f" {q}) {i}")
    input("\n Press enter to continue...")    
def new_user():
    nam = input("Enter New Name -> ")
    pas = input("Enter New Password -> ")
    if nam in users:
        input("\n\n Name already already exists...")
    else:
        users.update({nam:pas})
        user_vech.update({nam:'none'})
        input("\n\n   User Created Successfully...")    
def search_vehicle(name):
    print(" 1) Search by Type\n 2) Search by name\n")
    choice = input("Enter Your Choice -> ")
    if choice=='2':
        nam = input("\nEnter name of vehicle to search -> ")
        co = 0
        for i in vehicles:
            if i['name']==nam:
                print(f"Name -> {i['name']}\nVehicle ID -> {i['id']}\nRate/km -> {i['rate']}")
            else:
                co+=1
        if co==len(vehicles):
            input("\n\n\t   Vechicle not found...")
        else:
            print("\n 1) Add to cart\n 2) Exit")
            choice = input("\nEnter Your Choice -> ")
            if choice=='1':
                cn = 0
                for i in user_vech:
                    if i==name and user_vech[i]=='none':
                        cart.append(nam)
                        input("\n\n   Added to cart...")
                        break  
                    else:
                        cn +=1      
                if cn==len(user_vech):
                    input("You Already owed one vechicle\nplz Return in time...")        
            else:     
               print()
    elif choice=='1':
        nam = input("\nEnter Type of Vehicle to search -> ")
        co = 0
        for i in vehicles:
            if i['type']==nam:
                print(f"Name -> {i['name']}\nVehicle ID -> {i['id']}\nRate/km -> {i['rate']}")
                print("\n")
            else:
                co+=1
        if co==len(vehicles):
            input("\n\n\t   Vechicle not found...")
        else:
            print("\n 1) Add to cart\n 2) Exit")
            choice = input("\nEnter Your Choice -> ")
            if choice=='1':
                nam = input("Enter name of bike to add cart -> ")
                for i in user_vech:
                    if i==name and user_vech[i]=='none':
                        cart.append(nam)
                        history.append(str(f"{name} Buyed a {nam}"))
                        input("\n\n   Added to cart...")  
                    else:
                        input("\nYou Already owed one vechicle\nplz Return in time...")
            else:     
               print()
def my_cart(cart,name):
    print("\t   My Cart\n")
    q=1
    for i in cart:
        print(f" {q}) {i}")
    print("\n 1) checkout\n 2) Removes items from cart\n 3) Exit")
    choice = input("Enter your choice -> ")
    if choice=='3':
        print()
    elif choice=='2':
        cart = list()
    elif choice=='1':
        nam = input("\n Enter Name to checkout -> ")
        if nam in cart:
            if user_vech[name]=='none':
               user_vech[name]=nam
               cart = list()
               input("\t Vehicle buyed succesfully\n\nPress Enter to continue...")
            else:
                input("\n\nYou Already owed one vechicle\nplz Return in time...")
        else:
            input("\n Name not found...")
    else:
        input("\n\t Invalid choice...")
def return_vechicle():
    if user_vech[name]=='none':
        input("You Owed nothing...")
    else:    
        print(f"Your Owed Vehicle -> {user_vech[name]}")
        print("\n 1) Return\n 2) Exit")
        choice = input("\nEnter your Choice -> ")
        if choice=='2':
            pass
        elif choice=='1':
            bill = 0
            km = int(input("Enter no of kilometers runed -> "))
            da = input("Enter Damage status\n (low,medium,high,no) -> ")
            if da=='low':
                bill += 300
            elif da=='medium':
                bill+=1200
            elif da=='high':
                bill += 3000
            else:
                input("Invalid choice...")
            for i in vehicles:
                if i['name']==user_vech[name]:
                    f = i['rate']
            bill += (f*km)
            print(f"\n\n   Your Bill Amount is -> {bill}")
            history.append(str(f"{name} Returned {user_vech[name]} and Bill Amount is {bill}"))
            input("\n\t Press enter to return...")
            user_vech.update({name:'none'})
        else:
            input("\nInvalid choice...")                                             
while(True):
    os.system("cls")
    print("\t   ---Vehicle Rental---")
    print("\n 1) Admin\n 2) User\n 3) Exit\n")
    choice = input(" Enter Your choice -> ")
    if choice=='3':
        break
    elif choice=='2':
        os.system("cls")
        print('\t   ---Welcome to user login---\n')
        print(" 1) new user\n 2) Existing user\n 3) Exit\n")
        choice = input("Enter your choice -> ")
        if choice=='3':
            break
        elif choice=='2':
            os.system("cls")
            name = input("\nEnter your name -> ")
            passwrd = input("Enter password -> ")
            if name in users and passwrd==users[name]:
                while(True):
                    os.system("cls")
                    print(f"\t   ---Welcome {name}---\n")
                    print(" 1) Search Vehicle\n 2) My Cart\n 3) Return Vehicle\n 4) Logout\n")
                    choice=input("Enter Your Choice -> ")
                    if choice=='4':
                        cart = list()
                        break
                    elif choice=='3':
                        os.system("cls")
                        return_vechicle()
                        cart = list()
                    elif choice=='2':
                        os.system("cls")
                        my_cart(cart,name)
                        cart = list()
                    elif choice=='1':
                        os.system("cls")
                        search_vehicle(name)
                    else:
                        input("\n\n  Invalid Choice...")
        elif choice=='1':
            os.system("cls")
            new_user()
        else:
            input("\n\n\t   Invalid Choice...")
    elif choice=='1':
        os.system("cls")
        ad = input("Enter Name -> ")
        pas = input("Enter Password -> ")
        if ad=='admin' and pas=='1234':
            while(True):
                os.system("cls")
                print("\t   ---Welcome Admin---\n")
                print(" 1) Add vechile\n 2) Remove Vehicle\n 3) View Vehicle\n 4) View Reports\n 5) Logout\n")
                choice = input("Enter Your Choice -> ")
                if choice=='5':
                    break
                elif choice=='4':
                    os.system("cls")
                    view_history()
                elif choice=='3':
                    os.system("cls")
                    view_vechile()
                elif choice=='2':
                    os.system("cls")
                    remove_vehicle()
                elif choice=='1':
                    os.system("cls")
                    add_vechicle()
                else:
                    input("\n\n\t   Invalid choice...")
        else:
            input("\n\n\t   Invalid Username or password...")        
    else:
        input("\n\n\t   Invalid Choice...")