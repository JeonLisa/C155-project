from tkinter import *
import random
root=Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary={"color":["black","purple","pink","blue","white"]}
def color():
    random_num=random.randint(0,4)
    root.configure(background=dictionary["color"][random_num])
    
button_1=Button(root,text="Click Me!",command=color)
button_1.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()