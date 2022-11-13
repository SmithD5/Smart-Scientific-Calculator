from tkinter import *
import tkinter
from tkinter.messagebox import *
import math as m

#some useful variables
font=('arial',20,'bold')

# important functions
def all_clear():
    textField.delete(0, END)

def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0, END)
    textField.insert(0, ex)

def click_btn_function(event):
    b = event.widget
    text = b['text']
    
    if text == 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            showerror("Error", e)

        return

    textField.insert(END, text)


#creating a window
window=Tk()
window.title('Scientific Calculator')
window.geometry('340x390') 
window.resizable(width=False,height=False) 

#text field 
textField = Entry(window, font= font, bd=17, bg= 'gray60', width=25, justify= RIGHT)
textField.pack(side=TOP, pady=5)
# textField.insert(0,'0')

#buttons

#creating the frame for buttons
buttonFrame = Frame(window)
buttonFrame.place(x=15,y=90)
#adding button
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame, text=str(temp), font=font, width=2, relief= RAISED,bd=7, activebackground='gray50')
        btn.grid(row=i, column=j,padx=2,pady=2)
        temp = temp+1
        btn.bind('<Button-1>',click_btn_function)

zeroBtn=Button(buttonFrame, text='0', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
zeroBtn.grid(row=3, column=0,padx=2,pady=2)
dotBtn=Button(buttonFrame, text='. ', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
dotBtn.grid(row=3, column=1,padx=2,pady=2)
remainderBtn=Button(buttonFrame, text='%', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
remainderBtn.grid(row=3, column=2,padx=2,pady=2)
plusBtn=Button(buttonFrame, text='+', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
plusBtn.grid(row=0, column=3,padx=2,pady=2)
minusBtn=Button(buttonFrame, text='-', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
minusBtn.grid(row=1, column=3,padx=2,pady=2)
multBtn=Button(buttonFrame, text='x', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
multBtn.grid(row=2, column=3,padx=2,pady=2)
divBtn=Button(buttonFrame, text='/', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
divBtn.grid(row=3, column=3,padx=2,pady=2)
delBtn=Button(buttonFrame, text='DEL', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60', command=clear)
delBtn.grid(row=0, column=4,padx=2,pady=2)
clearBtn=Button(buttonFrame, text='AC', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60', command=all_clear)
clearBtn.grid(row=1, column=4,padx=2,pady=2)
equalBtn=Button(buttonFrame, text='=', font=font, width=3, height=3, relief= RAISED,bd=7, activebackground='gray60')
equalBtn.grid(row=2, rowspan=2 , column=4,padx=2,pady=2)

plusBtn.bind('<Button-1>',click_btn_function)
minusBtn.bind('<Button-1>',click_btn_function)
multBtn.bind('<Button-1>',click_btn_function)
divBtn.bind('<Button-1>',click_btn_function)
remainderBtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
zeroBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)

'''----------------------------------------------Scientific functions----------------------------------------------------'''

scFrame = Frame(window)
scFrame.place(x=340,y=90)
sqrtBtn=Button(scFrame, text='√', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
sqrtBtn.grid(row=0, column=0,padx=2,pady=2)
powerBtn=Button(scFrame, text='^', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
powerBtn.grid(row=0, column=1,padx=2,pady=2)
factBtn=Button(scFrame, text='!', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
factBtn.grid(row=0, column=2,padx=2,pady=2)
logBtn=Button(scFrame, text='log', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
logBtn.grid(row=0, column=3,padx=2,pady=2)
radBtn=Button(scFrame, text='toRad', font=('arial',20,'bold'), width=7,relief= RAISED,bd=7, activebackground='gray60')
radBtn.grid(row=3,columnspan=2, column=2,padx=2,pady=2)
degBtn=Button(scFrame, text='toDeg', font=('arial',20,'bold'), width=7, relief= RAISED,bd=7, activebackground='gray60')
degBtn.grid(row=3,columnspan=2, column=0,padx=2,pady=2)
sinBtn=Button(scFrame, text='sin', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
sinBtn.grid(row=1, column=0,padx=2,pady=2)
cosBtn=Button(scFrame, text='cos', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
cosBtn.grid(row=1, column=1,padx=2,pady=2)
tanBtn=Button(scFrame, text='tan', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
tanBtn.grid(row=1, column=2,padx=2,pady=2)
piBtn=Button(scFrame, text='π', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
piBtn.grid(row=1, column=3,padx=2,pady=2)
sinhBtn=Button(scFrame, text='sinh', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
sinhBtn.grid(row=2, column=0,padx=2,pady=2)
coshBtn=Button(scFrame, text='cosh', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
coshBtn.grid(row=2, column=1,padx=2,pady=2)
tanhBtn=Button(scFrame, text='tanh', font=font, width=3, relief= RAISED,bd=7, activebackground='gray60')
tanhBtn.grid(row=2, column=2,padx=2,pady=2)
eBtn=Button(scFrame, text='e', font=font, width=2, relief= RAISED,bd=7, activebackground='gray60')
eBtn.grid(row=2, column=3,padx=2,pady=2)


def calculate_sc(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))
    elif text == 'log':
        answer = str(m.log(int(ex)))
    elif text == '!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sin':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cos':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tan':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == 'sinh':
        answer = str(m.sinh(m.radians(int(ex))))
    elif text == 'cosh':
        answer = str(m.cosh(m.radians(int(ex))))
    elif text == 'tanh':
        answer = str(m.tanh(m.radians(int(ex))))
    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))
    elif text == 'e':
        answer = str(m.e)
    elif text == 'π':
        answer = str(m.pi)
    
    textField.delete(0, END)
    textField.insert(0, answer)

sqrtBtn.bind('<Button-1>',calculate_sc)
powerBtn.bind('<Button-1>',calculate_sc)
factBtn.bind('<Button-1>',calculate_sc)
logBtn.bind('<Button-1>',calculate_sc)
radBtn.bind('<Button-1>',calculate_sc)
degBtn.bind('<Button-1>',calculate_sc)
piBtn.bind('<Button-1>',calculate_sc)
eBtn.bind('<Button-1>',calculate_sc)
sinBtn.bind('<Button-1>',calculate_sc)
cosBtn.bind('<Button-1>',calculate_sc)
tanBtn.bind('<Button-1>',calculate_sc)
sinhBtn.bind('<Button-1>',calculate_sc)
coshBtn.bind('<Button-1>',calculate_sc)
tanhBtn.bind('<Button-1>',calculate_sc)

'''-------------------------------------------------Phrases--------------------------------------------------------------'''
phraseFrame = Frame(window)
phraseFrame.place(x = 70, y = 390)

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textField.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                textField.delete(0,END)
                textField.insert(END,r)
            except:
                textField.delete(0,END)
                textField.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            textField.delete(0,END)
            textField.insert(END,'something went wrong please enter again')

operations = {'ADD':add ,'+':add ,'ADDITION':add , 'SUM':add , 'PLUS':add ,
              'SUB':sub,'-':sub, 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
              'PRODUCT':mul , 'MULTIPLICATION':mul,'*':mul,
              'MULTIPLY':mul , 'DIVISION':div ,'/':div ,'DIV':div ,'DIVIDE':div, 'MOD':mod ,'%':div,
              'REMAINDER':mod , 'MODULUS':mod , 'LCM':lcm , 'HCF':hcf  }


calBtn=Button(phraseFrame, text='CALCULATE', font=font, width=10, relief= RAISED,bd=7, activebackground='gray60', command=calculate)
calBtn.grid(row=0, column=1 , padx=2, pady=2)

'''-------------------------------------------------File Menu--------------------------------------------------------------'''
def Exit():
    if tkinter.messagebox.askyesno("Calculator","Confirm if you want to quit") >0 :
        window.destroy()
        return

def Sci():
    window.resizable(width=False,height=False)
    window.geometry("650x390")


def Std():
    window.resizable(width=False,height=False)
    window.geometry("340x390")

def Phrase():
    window.resizable(width=False,height=False)
    window.geometry("340x490")

menubar=Menu(window)

mode=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Mode", menu=mode)
mode.add_command(label="Standard",command=Std)
mode.add_command(label="Scientific",command=Sci)
mode.add_command(label="Smart",command=Phrase)
mode.add_separator()
mode.add_command(label="Exit",command=Exit)

window.config(menu=menubar)
window.mainloop()

