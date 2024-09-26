from tkinter import*
from time import strftime
root=Tk()
root.title('Live_Digital_Clock')
root.geometry('250x150')

def time():
    string= strftime('%H:%M:%S \n %D')
    l.config(text=string)
    l.after(1000,time)

#Adding Label
l=Label(root,text='time', font=('bold',25), bg='white', fg='red', anchor='center')
l.place(x=40,y=40,width=150)

time()
root.mainloop()
