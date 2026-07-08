from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("520x600")
root.configure(bg="black")
root.resizable(False, False)

expression = ""

# Display
entry = Entry(root, font=("Arial", 22), bd=10, relief=RIDGE,
              justify="right", bg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# Functions
def press(num):
    global expression
    expression += str(num)
    entry.delete(0, END)
    entry.insert(END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, END)

def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, END)
    entry.insert(END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = result
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        expression = ""

# Button Layout
buttons = [
    ('C',1,0), ('⌫',1,1), ('%',1,2), ('/',1,3),
    ('7',2,0), ('8',2,1), ('9',2,2), ('*',2,3),
    ('4',3,0), ('5',3,1), ('6',3,2), ('-',3,3),
    ('1',4,0), ('2',4,1), ('3',4,2), ('+',4,3),
    ('00',5,0), ('0',5,1), ('.',5,2), ('=',5,3)
]

for (text, row, col) in buttons:
    if text == "C":
        cmd = clear
        color = "red"
    elif text == "⌫":
        cmd = backspace
        color = "gray"
    elif text == "=":
        cmd = equal
        color = "orange"
    else:
        cmd = lambda t=text: press(t)
        color = "#333333"

    Button(root,
           text=text,
           font=("Arial", 18, "bold"),
           width=5,
           height=2,
           bg=color,
           fg="white",
           command=cmd).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
