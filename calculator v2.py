from cgitb import text
import tkinter as tk
from tokenize import Number
from turtle import width

global number 
number = "0"


def new_text(text):
    text_feld.insert("end", text)

def equal_func():
    print("3")





calculator_window = tk.Tk()
calculator_window.title("Calculator")
calculator_window.geometry("315x500")

text_feld = tk.Text(calculator_window)
text_feld.pack(ipadx=100, ipady= 40)

seven_button = tk.Button(calculator_window, text="7", command=lambda:new_text("7 "))
seven_button.pack(ipadx=30,
    ipady=30)
seven_button.place(x=20, y=100)
seven_button.config(height = 5, width=8)

eight_button = tk.Button(calculator_window, text="8", command=lambda:new_text("8 "))
eight_button.pack(ipadx=30,
    ipady=30)
eight_button.place(x=90, y=100)
eight_button.config(height = 5, width=8)

nine_button = tk.Button(calculator_window, text="9", command=lambda:new_text("9 "))
nine_button.pack(ipadx=30,
    ipady=30)
nine_button.place(x=160, y=100)
nine_button.config(height = 5, width=8)

divide_button = tk.Button(calculator_window, text="÷", command=lambda:new_text("÷ "))
divide_button.pack(ipadx=30,
    ipady=30)
divide_button.place(x=230, y=100)
divide_button.config(height = 5, width=8)

four_button = tk.Button(calculator_window, text="4", command=lambda:new_text("4 "))
four_button.pack(ipadx=30,
    ipady=30)
four_button.place(x=20, y=200)
four_button.config(height = 5, width=8)

five_button = tk.Button(calculator_window, text="5", command=lambda:new_text("5 "))
five_button.pack(ipadx=30,
    ipady=30)
five_button.place(x=90, y=200)
five_button.config(height = 5, width=8)

six_button = tk.Button(calculator_window, text="6", command=lambda:new_text("6 "))
six_button.pack(ipadx=30,
    ipady=30)
six_button.place(x=160, y=200)
six_button.config(height = 5, width=8)

multiplicate_button = tk.Button(calculator_window, text="×", command=lambda:new_text("x "))
multiplicate_button.pack(ipadx=30,
    ipady=30)
multiplicate_button.place(x=230, y=200)
multiplicate_button.config(height = 5, width=8)

one_button = tk.Button(calculator_window, text="1", command=lambda:new_text("1 "))
one_button.pack(ipadx=30,
    ipady=30)
one_button.place(x=20, y=300)
one_button.config(height = 5, width=8)

two_button = tk.Button(calculator_window, text="2", command=lambda:new_text("2 "))
two_button.pack(ipadx=30,
    ipady=30)
two_button.place(x=90, y=300)
two_button.config(height = 5, width=8)

three_button = tk.Button(calculator_window, text="3", command=lambda:new_text("3 "))
three_button.pack(ipadx=30,
    ipady=30)
three_button.place(x=160, y=300)
three_button.config(height = 5, width=8)

substract_button = tk.Button(calculator_window, text="-", command=lambda:new_text("- "))
substract_button.pack(ipadx=30,
    ipady=30)
substract_button.place(x=230, y=300)
substract_button.config(height = 5, width=8)

zero_button = tk.Button(calculator_window, text="0", command=lambda:new_text("0 "))
zero_button.pack(ipadx=30,
    ipady=30)
zero_button.place(x=90, y=400)
zero_button.config(height = 5, width=8)

def calculate():
    input= text_feld.get(1.0, "end")
    x,y,z = input.split()
    x = int(x)
    z = int(z)
    def calculator(operator, num1, num2):
        if operator == "-":
            print(x-z) 
        elif operator == "+":
            print(x+z)
        elif operator == "x":
            print(x*z)
        elif operator == "÷":
            print(x/z)
        
    calculator(y, x, z)

def clear():
    text_feld.delete(1.0, "end")

equal_button = tk.Button(calculator_window, text="=", command=calculate)
equal_button.pack(ipadx=30,
    ipady=30)
equal_button.place(x=160, y=400)
equal_button.config(height = 5, width=8)

plus_button = tk.Button(calculator_window, text="+", command=lambda:new_text("+ "))
plus_button.pack(ipadx=30,
    ipady=30)
plus_button.place(x=230, y=400)
plus_button.config(height = 5, width=8)

next_button = tk.Button(calculator_window, text="",command = lambda:new_text(""))
next_button.pack(ipadx=30,
    ipady=30)
next_button.place(x=20, y=400)
next_button.config(height = 5, width=8)

clear_button = tk.Button(calculator_window, text="C",command = clear)
clear_button.pack(ipadx=30,
    ipady=30)
clear_button.place(x=230, y=0)
clear_button.config(height = 5, width=8)

calculator_window.mainloop()

