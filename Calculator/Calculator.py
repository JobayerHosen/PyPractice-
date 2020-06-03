from tkinter import *


class Btn:
    buttons = []
    backg = 'white'
    fg = 'black'
    height = 2
    width = 8
    pady = 5
    rowspan = 1

    def __init__(self, text, row, col):
        self.text = text
        self.row = row
        self.col = col
        self.command = lambda: getvalue(self)
        Btn.buttons.append(self)

    def makeBtn(self):
        self.btn = Button(bottomframe, text=self.text, command=self.command, backg=self.backg, fg=self.fg, width=self.width, height=self.height, padx=1, pady=self.pady, font=("calibri", 20))
        self.btn.grid(row=self.row, column=self.col, rowspan=self.rowspan, sticky="E, S")


#------------- Button's Functions---------------
def getvalue(btn):
    global buffer
    buffer += btn.text
    display2.set(buffer)

def press_add():
    global buffer
    global expression
    expression += buffer
    buffer = ""
    expression += '+'
    display.set(expression)
    display2.set("")

def press_minus():
    global buffer
    global expression
    if not buffer and not expression:
        buffer += '-'
        display2.set(buffer)
    else:
        expression += buffer
        buffer = ""
        expression += '-'
        display.set(expression)
        display2.set("")

def press_multi():
    global buffer
    global expression
    expression += buffer
    buffer = ""
    expression += '*'
    display.set(expression)
    display2.set("")

def press_div():
    global buffer
    global expression
    expression += buffer
    buffer = ""
    expression += '/'
    display.set(expression)
    display2.set("")

def press_modulas():
    global buffer
    global expression
    expression += buffer
    buffer = ""
    expression += '%'
    display.set(expression)
    display2.set("")

def press_equal():
    global buffer
    global expression
    if buffer:
        expression += buffer
        buffer = ""
        display2.set("")
        try:
            result = eval(expression)
            buffer = "= " + str(result)
            display.set(expression)
            display2.set(buffer)
        except Exception as e:
            display.set("Error!")
            display2.set(e)

def press_ac():
    global buffer
    global expression
    buffer = ""
    expression = ""
    display.set(expression)
    display2.set(buffer)

def press_del():
    global buffer
    global expression
    if buffer:
        buffer = buffer[:-1]
        display2.set(buffer)
    else:
        expression = expression[:-1]
        display.set(expression)


root = Tk()
root.title("Jobayer's Calculator")
topframe = Frame(root, width=400, height=100,)
topframe.pack()
bottomframe = Frame(root, width=400, height=400,)
bottomframe.pack()

expression = ""
buffer = ""
#Upper portion of display
display = StringVar()
entry = Label(topframe, text=display, width=16, height=1, bg="#cde2aa", textvariable=display, font=("calibri", 44))
entry.pack(side="top")
#Lower portion of display
display2 = StringVar()
entry2 = Label(topframe, text=display2, width=16, height=1, bg="#cde2aa", textvariable=display2, font=("calibri", 44))
entry2.pack(side="bottom") 


# -----------Creating all the button objects-------------
btn_ac = Btn("AC", 0, 0)
btn_ac.command = press_ac
btn_ac.fg = '#fa5900'
btn_del = Btn("DEL", 0, 1)
btn_del.command = press_del
btn_div = Btn("/", 0, 2)
btn_div.command = press_div
btn_x = Btn("x", 0, 3)
btn_x.command = press_multi

btn_7 = Btn("7", 1, 0)
btn_8 = Btn("8", 1, 1)
btn_9 = Btn("9", 1, 2)
btn_min= Btn("-", 1, 3)
btn_min.command = press_minus

btn_4 = Btn("4", 2, 0)
btn_5 = Btn("5", 2, 1)
btn_6 = Btn("6", 2, 2)
btn_add = Btn("+", 2, 3)
btn_add.command = press_add

btn_1 = Btn("1", 3, 0)
btn_2 = Btn("2", 3, 1)
btn_3 = Btn("3", 3, 2)
btn_equal = Btn("=", 3, 3)
btn_equal.command = press_equal
btn_equal.rowspan = 2
btn_equal.height = 5
btn_equal.backg = "#fa5700"

btn_modulas = Btn("mod", 4, 0)
btn_modulas.command = press_modulas
btn_0 = Btn("0", 4, 1)
btn_dot = Btn(".", 4, 2)

for button in Btn.buttons:
    button.makeBtn()

root.mainloop()