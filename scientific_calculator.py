from tkinter import *
import math

root = Tk()
root.title("Vishal Scientific Calculator")
root.geometry("350x500")
root.configure(bg="black")

entry = Entry(
    root,
    width=25,
    font=("Arial", 20),
    borderwidth=5,
    bg="black",
    fg="white",
    insertbackground="white"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '⪻', '%',
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        Button(root, text=button, width=8, height=2,
               bg="#333333", fg="white",
               command=calculate).grid(row=row, column=col)
    else:
        Button(root, text=button, width=8, height=2,
               bg="#333333", fg="white",
               command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

Button(root, text="C", width=8, height=2,
       bg="red", fg="white",
       command=clear).grid(row=row, column=0)

Button(root, text="√", width=8, height=2,
       bg="#333333", fg="white",
       command=sqrt).grid(row=row, column=1)

Button(root, text="%", width=8, height=2,
       bg="#333333", fg="white",
       command=percentage).grid(row=row, column=2)

Button(root, text="⪻", width=8, height=2,
       bg="#333333", fg="white",
       command=backspace).grid(row=row, column=3)

root.mainloop()









from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.geometry("500x650")
root.configure(bg="black")

entry = Entry(
    root,
    width=25,
    font=("Arial Narrow", 30),
    borderwidth=5,
    bg="black",
    fg="white",
    insertbackground="white"
)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def click(value):
    pos = entry.index(INSERT)
    entry.insert(pos, value)
 
def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        if isinstance(result, float) and result.is_integer():
                result = int(result)

        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

def sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")


def tan():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def log():
    try:
        result = math.log10(float(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def ln():
    try:
        result = math.log(float(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def factorial():
        try:
            num = int(entry.get())
            result = math.factorial(num)
            entry.delete(0, END)
            entry.insert(0, result)
        except:
            entry.delete(0, END)
            entry.insert(0, "Error")

def power():
        click("**")

def pi():
    entry.insert(INSERT,
str(math.pi))

def cosec():
    try:
        x = math.radians(float(entry.get()))
        result = 1 / math.sin(x)
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def sec():
    try:
        x = math.radians(float(entry.get()))
        result = 1 / math.cos(x)
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def cot():
    try:
        x = math.radians(float(entry.get()))
        result = 1 / math.tan(x)
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

 

Button(root, text="C", width=8, height=2,
       bg="red", fg="white",
command=clear).grid(row =5, column=0)

Button(root, text="√", width=8, height=2,
       bg="#333333", fg="white",
command=sqrt).grid(row=4, column=1)

Button(root, text="=", width=8, height=2,
       bg="#333333", fg="white",
command=calculate).grid(row=5, column=3)

Button(root, text="%", width=8,
height=2,
        bg="#333333", fg="white",
command=percentage).grid(row=3, column=2)

Button(root, text="sin", width=8,
height=2,
        bg="#333333", fg="white",
        command=sin).grid(row=1, column=0)

Button(root, text="cos", width=8,
height=2,
        bg="#333333", fg="white",
        command=cos).grid(row=1, column=1,)

Button(root, text="tan", width=8,
height=2,
       bg="#333333", fg="white",
       command=tan).grid(row=1, column=2,)

Button(root, text="log", width=8,
height=2,
       bg="#333333", fg="white",
       command=log).grid(row=1, column=3, )

Button(root, text="ln", width=8,
height=2,
        bg="#333333", fg="white",
        command=ln).grid(row=1, column=4,)

Button (root, text="7", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("7")).grid(row=2, column=0,)

Button(root, text="8", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("8")).grid(row=2, column=1,)

Button(root, text="9", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("9")).grid(row=2, column=2,)

Button(root, text="⪻", width=8,
height=2,
        bg="#333333", fg="white",
        command=backspace,).grid(row=2, column=3,)

Button(root, text="/", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("/")).grid(row=2, column=4,)

Button(root, text="4", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("4")).grid(row=3, column=0,)

Button(root, text="5", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("5")).grid(row=3, column=1,)

Button(root, text="6", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("6")).grid(row=3, column=2,)

Button(root, text="%", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("%")).grid(row=3, column=3,)

Button(root, text="×", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("*")).grid(row=3, column=4,)

Button(root, text="1", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("1")).grid(row=4, column=0,)

Button(root, text="2", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("2")).grid(row=4, column=1,)

Button(root, text="3", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("3")).grid(row=4, column=2,)

Button(root, text="√", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("√")).grid(row=4, column=3,)

Button(root, text="-", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("-")).grid(row=4, column=4,)

Button(root, text="C", width=8,
height=2,
        bg="red", fg="white",
        command=clear).grid(row=5, column=0,)

Button(root, text="0", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda:click("0")).grid(row=5, column=1,)

Button(root, text=".", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click(".")).grid(row=5, column=2,)
Button(root, text="=", width=8,
height=2,
        bg="#333333", fg="white",
        command=calculate).grid(row=5, column=3,)
Button(root, text="+", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("+")).grid(row=5, column=4,)

Button(root, text="(", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click("(")).grid(row=6, column=3,)

Button(root, text=")", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda: click(")")).grid(row=6, column=4,)

Button(root, text="00", width=8,
height=2,
        bg="#333333", fg="white",
        command=lambda:click("00")).grid(row=6, column=0,)

Button(root, text="!", width=8,
height=2,
        bg="#333333", fg="white",
        command=factorial).grid(row=6, column=1,)

Button(root, text="**", width=8,
height=2,
        bg="#333333", fg="white",
        command=power).grid(row=6, column=2,)

Button(root, text="₶", width=8,
height=2,
        bg="#333333", fg="white",
        command=pi).grid(row=7, column=0,)

Button(root, text="cosec", width=8,
height=2,
        bg="#333333", fg="white",
        command=cosec).grid(row=7, column=1,)

Button(root, text="sec", width=8,
height=2,
        bg="#333333", fg="white",
        command=sec).grid(row=7, column=2,)

Button(root, text="cot", width=8,
height=2,
        bg="#333333", fg="white",
        command=cot).grid(row=7, column=3,)

root.mainloop()
