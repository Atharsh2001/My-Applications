from tkinter import *
from pytube import YouTube 
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("youtube video downloader")
                                                                                   
Label(root,text = 'YouTube Downloader', font ='arial 20 bold').pack()
##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
#function to download video
def C360():
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="360p").first()
    video.download()
    Label(root, text = 'Downloaded at 360p Quality', font = 'arial 15').place(x= 120 , y = 230)
def C480():
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="480p").first()
    video.download()
    Label(root, text = 'Downloaded at 480p Quality', font = 'arial 15').place(x= 120 , y = 230)
def C720():
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="720p").first()
    video.download()
    Label(root, text = 'Downloaded at 720p Quality', font = 'arial 15').place(x= 120 , y = 230)  
def C1080():
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="1080p").first()
    video.download()
    Label(root, text = 'Downloaded at 1080p Quality', font = 'arial 15').place(x= 120 , y = 230)               
Label(root, text = 'Select Quality :', font = 'arial 10').place(x= 30 , y = 140)
button360 = Button(root,text="360p",bg='#99FFFF',command=C360)
button360.place(x=100,y=180)
button480 = Button(root,text="480p",bg='#99FFFF',command=C480)
button480.place(x=170,y=180)
button720 = Button(root,text="720p",bg='#99FFFF',command=C720)
button720.place(x=240,y=180)
button1080 = Button(root,text="1080p",bg='#99FFFF',command=C1080)
button1080.place(x=310,y=180)
root.mainloop()
