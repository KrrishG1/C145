# -*- coding: utf-8 -*-
from tkinter import *
root = Tk()
root.title("Addition")
root.geometry("200x400")

show_result=Label(root)

def add():
    result= 4+1
    show_result["text"]=result

btn = Button(root, text="Add", command=btn.pack())

show_result.pack()

root.mainloop()