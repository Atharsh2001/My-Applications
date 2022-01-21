# Railway Ticket Booking

import os
import numpy as np
import random
users_id = {'atharsh':'1234','ashwin':'1234'}
se = list()
history = list()
station_id = {1:'Tiruppur',2:'Erode',3:'Salem',4:'Tirchy',5:'Kanchepuram'}
st = [0,0,0,0,0]
train = [
[1,1,1,0,0],
[1,1,0,0,0],
[1,1,0,0,0],
[0,1,1,1,1],
[0,0,1,1,1],
[0,1,1,1,0],
[1,1,0,0,0],
[1,1,1,0,0],
[0,1,1,1,1],
[0,0,1,1,1]]
wait_list = [0,0,0]
def new_user():
    print("\t  ...New Login User portal\n")
    new_name = input("Enter New Name -> ")
    new_pass = input("Enter New Password -> ")
    if new_name in users_id:
        print("\n\tName already exists...")
        input("Press Enter To continue")
    else:
        users_id.update({new_name:new_pass})
        print("\n\tUser Created Successully...\n")
        input("Press Enter to Continue")
    
def booking_seats(a,b):
    print("\n\t      Booking Seats...")
    print("\t{} to {} station".format(station_id[a],station_id[b]))
    sta = input("\nEnter confirm to Book Seats\n(Enter exit To cancel) -> ")
    return sta
            
def station(): 
    print("\tSelect Station...")
    print("\n1) Tiruppur\n2) Erode\n3) Salem\n4) Tiruchy\n5) Kanchepuram\n")
    ini = int(input("Enter boarding Station : "))
    fnl = int(input("Enter depature station : "))
    global avail_seat
    avail_seat = list()
    sn = []
    count = 0
    for m in range(5):
        if(m>=(ini-1) and m<fnl):
            st[m]=1
            sn.append(0)
        else:
            st[m]=0
    for i in range(0,10,1):
        ss = []
        se = []
        ss = train[i]
        for j in range(0,5,1):
            if(j<(ini-1) or j>(fnl-1)):
                continue
            else:    
                se.append(ss[j])
        a = se
        b = sn
        arr1 = np.array(a)
        arr2 = np.array(b)
        comp = arr1 == arr2
        res = comp.all()
        if res==True:
            count+=1
            avail_seat.append(i)       
    if count!=0:
        print("\nAvailable seats ->",count)
    else:
        print("\n\n  No Available seats...")
        w_count = 0
        for ty in wait_list:
            if ty==0:
                w_count+=1
        if w_count>0:        
            print("\n   Availble waiting seats are",w_count)
        else:
            print("\n   No Alavilable Waiting Seats")    
        input("\n\t Press Enter to continue ...")    
    return ini,fnl  
def user_history():
    print("\t...User History...\n")
    if len(history)!=0:
        q=1
        for _ in range(len(history)):
            if history[_]['name']==name:
                print("{}) Name : {}\n   Boarding Station : {}\n   Depature Station : {}\n   Seat No : {}\n   PNR No : {}\n   Train Name : CBE - MAD Express\n".format(q,history[_]['name'],station_id[history[_]['board']],station_id[history[_]['depart']],(history[_]['seat'])+1,history[_]['pnr']))
                print("\n\t--------\n")
            q+=1        
        input("Press Enter to Continue...")      
    else:
        input("\n\tNo History")  

def remove_Seat(name,ini,fnl):
    print("\n\t   Cancel Ticket\n")
    seat_no = int(input("Enter Your Seat No -> "))
    pnr1 = input("Enter Your PNR No -> ")
    for e in range(len(history)):
        if((seat_no-1)==history[e]['seat']and name==history[e]['name'] and pnr1==history[e]['pnr']):
            del history[e]
            for it in range(5):
                if(it<(ini-1) or it>(fnl-1)):
                    continue
                else:
                    train[seat_no-1][it]=0    
            print("\n\t Ticket Cancelled Successfully...")
            input("\nPress Enter to continue...")
            break
    else:
        input("\n\t   No Data Found...")        

while(True):
    os.system("cls")
    print("\t   ...Welcome To IRCTC...\n")
    print("1) New User\n2) Exixsting User\n3) Exit\n")
    choice = int(input("Enter Your Choice -> "))
    if choice==1:
        os.system("cls")
        new_user()
    elif choice==2:
        os.system("cls")
        print("\t   ...Existing User Login Portal...")
        name = input("Enter Name -> ")
        passwd = input("Enter Password -> ")
        if (name in users_id) and passwd==users_id[name]:
            while(True):
                os.system("cls")
                print("\t   ...Welcome {}...".format(name))
                print("\n1) Ticket Booking\n2) Ticket Cancel\n3) Logout\n")
                choice = int(input("Enter Your choice -> "))
                if choice==1:
                    while(True):
                        os.system("cls")
                        print("\t  CBE - MAD Express\n")
                        print("1) Seat Availability\n2) Booking History\n3) Exit\n")
                        choice = int(input("Enter Your Choice -> "))
                        if choice==1:
                            os.system("cls")
                            a,b = station()
                            print("\n1) Book Seats\n2) Book in waiting\n3) Exit\n")
                            sec = int(input("Enter Your Choice -> "))
                            if sec==3:
                                break
                            elif sec==2:
                                pass
                            elif sec==1:
                                os.system('cls')
                                sta = booking_seats(a,b)
                                if sta=='confirm':
                                    os.system("cls")
                                    print("\n\t  Seat Booked Successfully...")
                                    r = avail_seat[0]
                                    for iy in range(5):
                                        if(iy<(a-1) or iy>(b-1)):
                                            continue
                                        else:
                                            train[r-1][iy]=1
                                    pnr ='PN' +str(random.randint(500,1000))
                                    history.append({'seat':r,'board':a,'depart':b,'name':name,'pnr':pnr})
                                    print("\n\tYour seat Numer is -> ",r+1)
                                    print("\tYour PNR No is -> ",pnr)
                                    print("\n\tThank You for Choosing IRCTC\n\tHave a safe ride...")
                                    input("\n\t  Press Enter To Continue")
                                elif sta=='exit':
                                    break
                                else:
                                    input("\n\tInvalid Choice...")
                            else:
                                input("\tInvalid Choice...")       
                        elif choice==2:
                            os.system("cls")
                            user_history()
                        else:
                            break
                elif choice==2:
                    os.system("cls")
                    remove_Seat(name,a,b)
                elif choice==3:
                    break
                else:
                    input("\n\tInvalid Choice...")
        else:
            input("\n\tInvalid Username or Password...")
    elif choice==3:
        break
    else:
        input("\n\tInvalid Choice...")