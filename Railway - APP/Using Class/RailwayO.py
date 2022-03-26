import os
train = [[0 for i in range(5)] for j in range(10)]
user = ['aaa','bbb']
UserCls = []
pnr = []
class UserClass:
    def __init__(self,name,passwrd):
        self.name = name
        self.passwrd = passwrd
        self.id = 'IR'+str(len(user)+1)
        self.history = []
    def UserAthentication(self,name,passwrd):
        if name==self.name and passwrd==self.passwrd:
            return True
        else:
            return False
    def BookTicket(self):
        print("\tCoimabtore to Chennai")
        print("\n1) coimbatore 2) Tirupur 3) Salem 4) Tirchy 5) chennai")
        st1 = int(input("\nEnter Boarding station -> "))
        st2 = int(input("Enter Depature station -> "))
        SeatCount = 0
        for i in train:
            if i[st1-1:st2-1]==[0]*(st2-st1):
                SeatCount+=1
        print("\n\nAvailable seats :",SeatCount)
        pasen = int(input("Enter no of passengers -> "))
        pnr1 = "PN100"+str(len(pnr)+1)
        pnr.append(0)
        TiCount = 0
        seat = []
        for j in range(10):
            if TiCount==pasen:
                break
            if train[j][st1-1:st2-1]==[0]*(st2-st1):
                train[j][st1-1:st2-1]=[pnr1]*(st2-st1)
                TiCount+=1
                seat.append(j+1)
                if TiCount==pasen:
                    break
        self.history.append({pnr1:seat})
        print('\nSeats -> ',*seat,"\nPNR no is -> ",pnr1)
        input("\nSeat Booked successfully\n\n\tPress enter to continue ")
    def CancelTicket(self):
        print("\nMy Tickets : ")
        if self.history!=[]:
            for i in range(len(self.history)):
                for j in self.history[i]:
                    print(f"PNR -> {j}    Seats -> ",*self.history[i][j])
        CanTick = input("\nEnter PNR number to ticket -> ")
        for i in range(len(self.history)):
            if CanTick in self.history[i]:
                md = i
                break
        if CanTick in self.history[md]:
            for i in range(10):
                for j in range(5):
                    if train[i][j]==CanTick:
                        train[i][j]=0
            self.history.pop(md)
            input("\nTicket cancelled successfully\n\n\tPress enter to continue ")
        else:
            input("\nTicket not found\n\n\tPress enter to contiue ")
    def ViewTicket(self):
        for i in range(len(self.history)):
                for j in self.history[i]:
                    print(f"PNR -> {j}    Seats -> ",*self.history[i][j])
        input("\n\n\tPress enter to continue")

def NewUser():
    name = input("\nEnter new name -> ")
    passwrd = input("Set new Password -> ")
    if name in user:
        input("\nName already exsists\n\n\tPress enter to continue ")
    else:
        UserCls.append(UserClass(name,passwrd))
        user.append(name)
        input("\nUser created successfully\n\n\tPress enter to continue ")
    
UserCls.append(UserClass('aaa','111'))
UserCls.append(UserClass('bbb','222'))
while(True):
    os.system('cls')
    print("\tIRCTC")
    choice = input("\n1) Admin  2) User  3) Exit\n\nEnter your choice -> ")
    if choice=='1':
        os.system('cls')
        print(*train,sep="\n")
        input("\n\n\tPress enter to continue")
    elif choice=='2':
        while(True):
            os.system('cls')
            print("\tUser")
            choice = input("1) New User  2) Exising User 3) Exit\n\nEnter your choice -> ")
            if choice=='1':
                os.system('cls')
                NewUser()
            elif choice=='2':
                os.system('cls')
                name = input("\nEnter name -> ")
                passwrd = input("Enter password -> ")
                if name in user:
                    ind = user.index(name)
                    if UserCls[ind].UserAthentication(name,passwrd):
                        while(True):
                            os.system('cls')
                            print("\tWelcome back",name)
                            choice = input("1) Book Ticket 2) Cancel Ticket 3) View Ticket 4) Logout\n\nEnter your choice -> ")
                            if choice=='1':
                                os.system('cls')
                                UserCls[ind].BookTicket()
                            elif choice=='2':
                                os.system('cls')
                                UserCls[ind].CancelTicket()
                            elif choice=='3':
                                os.system('cls')
                                UserCls[ind].ViewTicket()
                            elif choice=='4':
                                break
                            else:
                                input("\n\n\tInvalid choice ")
                    else:
                        input("\nIncorrect password\n\n\tPress enter to continue ")
                else:
                    input("\nAccount not found\n\n\tPress enter to continue ")
            elif choice=='3':
                break
            else:
                input("\n\n\tInvalid choice ")
    elif choice=='3':
        break
    else:
        input("\n\n\tInvalid choice ")