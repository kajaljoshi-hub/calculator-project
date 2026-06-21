from tkinter import *
import math

root = Tk()
root.title("Modern Scientific Calculator")
root.geometry("450x700")
root.configure(bg="#121212")
root.resizable(False, False)

# Display
display = Entry(
    root,
    font=("Segoe UI", 24),
    bg="#1E1E1E",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="both", padx=15, pady=15, ipady=20)

# Functions
def click(value):
    display.insert(END, value)

def clear():
    display.delete(0, END)

def backspace():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])

def calculate():
    try:
        expression = display.get()
        expression = expression.replace("%", "/100")
        result = eval(expression)
        display.delete(0, END)
        display.insert(0, str(result))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def sqrt_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, math.sqrt(value))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def square_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, value ** 2)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def cube_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, value ** 3)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def log_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, math.log10(value))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def ln_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, math.log(value))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def sin_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, math.sin(math.radians(value)))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def cos_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, math.cos(math.radians(value)))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def tan_func():
    try:
        value = float(display.get())
        display.delete(0, END)
        display.insert(0, math.tan(math.radians(value)))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

# Button Frame
frame = Frame(root, bg="#121212")
frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ["sin", "cos", "tan", "√"],
    ["log", "ln", "x²", "x³"],
    ["π", "e", "(", ")"],
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for r in range(len(buttons)):
    frame.rowconfigure(r, weight=1)

for c in range(4):
    frame.columnconfigure(c, weight=1)

for row, row_values in enumerate(buttons):
    for col, text in enumerate(row_values):

        bg = "#2D2D2D"
        fg = "white"

        if text in ["+", "-", "*", "/", "%"]:
            bg = "#FF9800"

        elif text == "=":
            bg = "#4CAF50"

        elif text in ["C", "⌫"]:
            bg = "#F44336"

        elif text in ["sin", "cos", "tan", "log", "ln", "√", "x²", "x³", "π", "e"]:
            bg = "#2196F3"

        if text == "=":
            cmd = calculate
        elif text == "C":
            cmd = clear
        elif text == "⌫":
            cmd = backspace
        elif text == "√":
            cmd = sqrt_func
        elif text == "x²":
            cmd = square_func
        elif text == "x³":
            cmd = cube_func
        elif text == "log":
            cmd = log_func
        elif text == "ln":
            cmd = ln_func
        elif text == "sin":
            cmd = sin_func
        elif text == "cos":
            cmd = cos_func
        elif text == "tan":
            cmd = tan_func
        elif text == "π":
            cmd = lambda: click(str(math.pi))
        elif text == "e":
            cmd = lambda: click(str(math.e))
        else:
            cmd = lambda t=text: click(t)

        btn = Button(
            frame,
            text=text,
            font=("Segoe UI", 16, "bold"),
            bg=bg,
            fg=fg,
            bd=0,
            activebackground=bg,
            activeforeground="white",
            command=cmd
        )

        if text == "=":
            btn.grid(
                row=row,
                column=2,
                columnspan=2,
                sticky="nsew",
                padx=5,
                pady=5
            )
        else:
            btn.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=5,
                pady=5
            )

root.mainloop()