from tkinter import *
from tkinter import messagebox

T=Tk()#create main window
T.title("Event Handling")
T.geometry("200x300")

'''
def f1(event):
    print(event.char)#displays the key which was pressed

T.bind("<Key>",f1)#handle Key events
'''
L1=Label(T, text="Enter first number :")
e1=Entry(T)
L2=Label(T, text="Enter second number :")
e2=Entry(T)
L3=Label(T, text="Enter second number :")
e3=Entry(T)
n1=e1.get()
n2=e2.get()
n3=e2.get()
def f2(event):
    print("Button is clicked!!!")
    messagebox.showinfo("Addition",(n1*n2*n3/100))
    


b=Button(text="Click Me")
L1.pack()
e1.pack()
L2.pack()
e2.pack()
L3.pack()
e3.pack()

b.pack()
b.bind("<Button-1>",f2)#handle button clicks
T.mainloop()