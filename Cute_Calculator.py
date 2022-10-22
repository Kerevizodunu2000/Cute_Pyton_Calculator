from tkinter import *

def writeNumbers(x):
    s = len(textBox.get())
    textBox.insert(s, str(x))

check = 5
s1 = 0

def process(x):
    global check
    check = x
    global s1
    s1 = float(textBox.get())
    textBox.delete(0, 'end')

s2 = 0
def calculate():
    global s2
    s2 = float(textBox.get())
    global check
    results = 0
    if (check == 0): results = s1 + s2
    elif (check == 1): results = s1 - s2
    elif (check == 2): results = s1 * s2
    elif (check == 3): results = s1 / s2
    textBox.delete(0, 'end')
    textBox.insert(0, str(results))

def clearScreen():
    textBox.delete(0, 'end')
    #uzun = len(textBox.get())-1
    #textBox.delete(uzun, 'end')

screen = Tk()
screen.minsize(250, 310)
screen.maxsize(250, 310)
screen.title("<3")

textBox = Entry(font="Verdana 14 bold", width=9, justify=RIGHT)
textBox.place(x=20, y=20)

ramNumber = []

for i in range(1, 10):
    ramNumber.append(Button(text=str(i), font="Verdana 14 bold", command=lambda x=i:writeNumbers(x)))

counter = 0
for i in range(0, 3):
    for j in range(0, 3):
        ramNumber[counter].place(x=30+j*50, y=60+i*60)
        counter += 1

ramSymbol = []

for i in range(0, 4):
    ramSymbol.append(Button(font="Verdana 14 bold", width=2, command=lambda x=i:process(x)))

ramSymbol[0]['text'] = "+"
ramSymbol[1]['text'] = "-"
ramSymbol[2]['text'] = "x"
ramSymbol[3]['text'] = "/"

for i in range(0, 4):
    ramSymbol[i].place(x=180, y=60+60*i)

zero_b = Button(text=0, font="Verdana 14 bold",borderwidth = 1, command=lambda x=0: writeNumbers(x))
zero_b.place(x=80, y=240)

dot_b = Button(text='.', font="Verdana 14 bold", width=2, command=lambda x=".": writeNumbers(x))
dot_b.place(x=30, y=240)

equal_b = Button(text='=', font="Verdana 14 bold", fg='red', command=calculate)
equal_b.place(x=130, y=240)

CE_b = Button(text='CE', font="Verdana 14 bold", command=clearScreen)
CE_b.place(x=175, y=5)

screen.mainloop()