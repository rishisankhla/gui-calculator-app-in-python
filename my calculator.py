from tkinter import *
w = Tk()
w.title("the calculator")

#w.geometry("312x324")  # size of the window width:- 500, height:- 375
#w.resizable(0, 0)  # this prevents from resizing the window
input_text = StringVar()

f1 = Frame(w, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)
f1.pack(side=TOP)
l1 = Entry(f1,textvariable=input_text, width=23, bg="#eee", bd=5, justify=LEFT, font=('arial', 18, 'bold'))
l1.grid(row=0, column=0)
l1.pack(ipady=10)
e = ""

def ins(a):
    global e
    e = e + str(a)
    input_text.set(e)
def equal():
    global e
    asd=eval(e)
    l1.delete(0,'end')
    input_text.set(asd)
    e=''

def btn_clear():
    global e
    e = ""
    input_text.set("")

f2 = Frame(w, width=312, height=272.5, bg="grey")

f2.pack()

bt1 = Button(f2, text="1", command=lambda: ins(1), width=10, height=3, bd=0).grid(row=3, column=0, padx=1, pady=1)
bt2=Button(f2,text="2",command=lambda: ins(2), width=10, height=3, bd=0).grid(row=3, column=1, padx=1, pady=1)
bt3 = Button(f2, text="3", command=lambda: ins(3), width=10, height=3, bd=0).grid(row=3, column=2, padx=1, pady=1)
bt4=Button(f2,text="4",command=lambda: ins(4), width=10, height=3, bd=0).grid(row=2, column=0, padx=1, pady=1)
bt5 = Button(f2, text="5", command=lambda: ins(5), width=10, height=3, bd=0).grid(row=2, column=1, padx=1, pady=1)
bt6=Button(f2,text="6",command=lambda: ins(6), width=10, height=3, bd=0).grid(row=2, column=2, padx=1, pady=1)
bt7 = Button(f2, text="7", command=lambda: ins(7), width=10, height=3, bd=0).grid(row=1, column=0, padx=1, pady=1)
bt8=Button(f2,text="8",command=lambda: ins(8), width=10, height=3, bd=0).grid(row=1, column=1, padx=1, pady=1)
bt9 = Button(f2, text="9", command=lambda: ins(9), width=10, height=3, bd=0).grid(row=1, column=2, padx=1, pady=1)
bt0=Button(f2,text="0",command=lambda: ins(0), width=21, height=3, bd=0).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
pto=Button(f2,text='.',command=lambda: ins('.'), width=10, height=3, bd=0).grid(row=4, column=2, padx=1, pady=1)
pl=Button(f2,text="+",command=lambda: ins("+"), width=10, height=3, bd=0).grid(row=3, column=3, padx=1, pady=1)
mn=Button(f2,text="-",command=lambda: ins("-"), width=10, height=3, bd=0).grid(row=2, column=3, padx=1, pady=1)
ml=Button(f2,text="*",command=lambda: ins("*"), width=10, height=3, bd=0).grid(row=1, column=3, padx=1, pady=1)
di=Button(f2,text="/",command=lambda: ins("/"), width=10, height=3, bd=0).grid(row=0, column=3, padx=1, pady=1)

eq=Button(f2,text="=",command=equal, width=10, height=3, bd=0).grid(row=4, column=3, padx=1, pady=1)
cl=Button(f2,text='clear',command=btn_clear, width=32, height=3, bd=0).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

w.mainloop()
