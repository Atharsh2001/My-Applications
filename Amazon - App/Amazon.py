#Amazon Mini Application

import os
import random
newretail_names = []
newretail_pass = []
products = [{'pid':1,"sellerid":1,"price":3000,"decs":"iphone","disc":10,'stock':100},
{'pid':2,"sellerid":2,"price":3500,"decs":"tv","disc":30,'stock':100},
{'pid':2,"sellerid":3,"price":4000,"decs":"tv","disc":15,'stock':100}]
sales_id = {1:'atharsh',2:'vasanth',3:'yadav'}
retailer_users = {'atharsh':'1234','vasanth':'1234','yadav':'1234'}
users = {'atharsh':1234}
add_cart = list()
history = list()
def new_user():
    nuser_name = input("Enter New Name : ")
    nuser_pass = int(input("Enter New Password(5 Digit Numeric) : "))
    if(nuser_name in users):
        input("\nName Already Exsists...")
    else:
        users.update({nuser_name:nuser_pass})
        input("\n\tAccount Created Successfully...")
def new_retail_login():
    new_name = input(" Enter new Name -> ")
    new_pass = input(" Enter new password (5 digit numeric ) -> ")
    if new_name in retailer_users:
        input("\tName already exist..")
    else:
        input("\tThank You Registering...Plz Wait for Approval from admin...")
        return new_name,new_pass
def admin_approval():
    m=0
    for i in newretail_names:
        print("The new registered Retailer ->",newretail_names[m])
        retail_approve = input("Press yes or no for Account Approval\nStatus :")
        if retail_approve == 'yes':
            retailer_users.update({newretail_names[m]:newretail_pass[m]})
            input("\tReatailer added Successfully...")
            sales_id.update({(max(sales_id)+1):newretail_names[m]})
        elif retail_approve=='no':
            input("Account Revoked...\nPress Enter to continue ")
        m+=1    
    input("\nNo More Approvals...\n\n\tPress Enter To Continue...")    
def remove_retailer():
    remove_name = input("Enter Name to remove :")
    del retailer_users[remove_name]
    input("\tRetailer removed Successfully...")
def add_product(re_name):
    print("\t...Adding Product...")
    pro_id = random.randint(101,400)
    for o in sales_id:
        if(re_name==sales_id[o]):
            seller_id = o
    pro_price = int(input("Enter Product Price : "))
    des = input("Enter Product Description : ")
    disc = int(input("Enter Product Offer : "))
    stock = int(input("Enter Product Stock : "))
    products.append({'pid':pro_id,"sellerid":seller_id,"price":pro_price,"decs":des,"disc":disc,'stock':stock})
    input("\n\tProduct Added Successfully...\n\tPress Enter To Continue...")
def remove_poduct():
    pass
def search_product():
    pr = input("Enter Product Name to Search : ")
    p=0
    a = 1
    ca = dict()
    global an
    an = list()
    count = 0
    for j in products:
        if(pr==products[p]['decs']):
          print(str(a)+"->  The Price of "+str(pr)+" is "+str(products[p]["price"]))
          print("     The Seller Of This product is",sales_id[products[p]['sellerid']])
          print("\n     -----------     \n")
          count+=1
          ca.update({a:products[p]})
        p+=1  
        a+=1
    cart = input("\nEnter Choice to add to Cart (Type exit To Continue) -> ")
    if cart!='exit':
        #add_cart = ca[cart]
        an.append(ca[int(cart)])
    if count==0:
        print("\tProduct Not Found...")
        input("     Press Enter To Continue...")   
def view_cart():
    c=1
    d=0
    for j in an:
        print(c,")")
        print("The Name of the product is",an[d]['decs'])
        print("The Price Of {} is {}".format(an[d]['decs'],an[d]['price']))
        print("The Offer available is",an[d]['disc'])
        print("     ---------    \n")
        c+=1
        d+=1
    input("\n\tPress Enter To Continue...")
def remove_cart():
    re= int(input("\nEnter Number to Remove an item from Cart : "))
    an.pop(re-1)
    print("\tItem removed successfully...")
    input("\n\tPress Enter to continue...")       
def checkout(us_name):
    print("\t...Bill...")
    print("\n   Purchased products :")
    d=1
    e=0
    price = 0
    discount = 0
    for e in range(len(an)):
        print("{}) {}".format(d,an[e]['decs']))
        print("Product Id is",an[e]['pid'])
        price += an[e]['price']
        discount += (an[e]['disc']/100)*an[e]['price']
        history.append({'product':an[e]['decs'],'price':an[e]['price'],'name':us_name})
        d+=1
    print("Total Prize ->",price)
    print("Offered Price ->",price-discount)
    print("\n\tOrder is placed successfully...\nproduct is reached within 3 to 4 working days!!!\n\t\tHappy Shopping...")
    print("\n\t...Thank you for Purchasing from Amazon...")
    input("\t     Press Enter to Continue...")
def view_history(us_name):
    w = 0
    for w in range(len(history)):
        if history[w]['name']==us_name:
            print("{}) product name : {}\n   product prize : {}".format((w+1),history[w]['product'],history[w]['price']))
            print("\t    --------     ")
    input("\nPress enter to continue...")    


while(True):
    os.system("cls")
    print("\t...Welcome to Amazon...")
    print("1) Admin login\n2) Retailler Login\n3) User login\n4) Exit\n")
    choice = int(input("Enter your Choice -> "))
    if choice == 4:
        break
    elif choice == 3:
        while(True):
            os.system("cls")
            print("\t...Welcome to User Login...")
            print("1) New User\n2) Exsisting User\n3) Exit\n")
            u1_choice = int(input("Enter Your Choice -> "))
            if u1_choice==3:
                break
            elif u1_choice==2:
                os.system("cls")
                print("\tExsisting User Login Portal...")
                us_name = input("Enter Name : ")
                us_pass = int(input("Enter Password : "))
                if (us_name in users) and us_pass==users[us_name]:
                    while(True):
                        os.system("cls")
                        print("\t...Welcome {}...".format(us_name))
                        print("1) Search Product\n2) My Cart\n3) Checkout\n4) View History\n5) Exit\n")
                        u_choise = int(input("Enter your Choice -> "))
                        if u_choise==5:
                            break
                        elif u_choise==4:
                            os.system("cls")  
                            view_history(us_name)  
                        elif u_choise==3:
                            os.system("cls")
                            checkout(us_name)
                        elif u_choise==2:
                            os.system("cls")
                            print("\t...My Cart...\n")
                            print("1) View My Cart 2) Remove Item 3) Exit\n")
                            C_choice = int(input("Enter Your Choice -> "))
                            if C_choice==3:
                                break
                            elif C_choice==2:
                                os.system("cls")
                                remove_cart()
                            elif C_choice==1:
                                os.system("cls")
                                print("\t...My Cart...\n")
                                view_cart()
                        elif u_choise==1:
                            os.system("cls")
                            search_product()
                        else:
                            input("\tInvalid choice...")             
                else:
                    input("\n\tInvalid Password Or Username...")   
            elif u1_choice==1:
                os.system("cls")
                print("\t...Welcome To New User Portal...")
                new_user()                   
    elif choice == 2:
        while(True):
            os.system("cls")
            print("\t...Welcome Retailler...\n\t      Login!")
            print("1) Exsiting Retailer\n2) New Retailer\n3) Exit\n")
            re_choice = int(input("Enter Your Choice -> "))
            if re_choice == 3 :
                break
            elif re_choice == 2:
                os.system("cls")
                print("\tRetailer Registration...")
                a,b = new_retail_login()
                newretail_names.append(a)
                newretail_pass.append(b)
            elif re_choice == 1:
                os.system("cls")
                print("\t...Welcome Retailler...")
                re_name = input("Enter Username :")
                re_pass = input("Enter Password :")
                if ((re_name in retailer_users) and re_pass == retailer_users[re_name]):
                    while(True):
                        os.system("cls")
                        print("\tWelcome ",re_name)
                        print("1) Add Product\n2) Remove Product\n3) Update Price\n4) Exit")
                        ex_choice = int(input("Enter your Choice ->"))
                        if ex_choice==4:
                            break
                        elif ex_choice==3:
                            pass
                        elif ex_choice==2:
                            pass
                        elif ex_choice==1:
                            os.system("cls")
                            add_product(re_name)
                        else:
                            input("\tInvalid Choice...")
                else:
                    input("\tInvalid Username or Password")
    elif choice == 1:
            os.system("cls")
            print("\t...Welcome Admin...")
            ad_name = input("Enter name :")
            ad_pass = input("Enter password :")
            if ad_name=='admin' and ad_pass == '1234':
                while(True):
                    os.system("cls")
                    print("1) Retailer Approval List\n2) Remove Retailer\n3) Exit\n")
                    ad_choice = int(input("Enter your Choice -> "))
                    if ad_choice == 3:
                        break
                    elif ad_choice == 2:
                        os.system("cls")
                        remove_retailer()
                    elif ad_choice == 1:
                        os.system("cls")
                        admin_approval()
                    else:
                        input("\tInvalid Choice...")
            else:
                input("\tInvalid name or password")
    else:
        input("\tInvalid Choice...")                    

