from tkinter import ttk
from sympy import*
from tkinter import *


root = Tk()
fun = StringVar(root)
fun1 = StringVar(root)
xi = StringVar(root)
xf = StringVar(root)
tf = StringVar(root)
td = StringVar(root)

x = symbols('x')

s = Scale(root, orient=HORIZONTAL, width=20, length=200,
          from_=1, to=100,  background='white')
sq = Scale(root, orient=VERTICAL, width=20, length=200,
           from_=1, to=20,  background='white')
sa = Scale(root, orient=VERTICAL, width=20, length=100,
           from_=1, to=5,  background='white')
scr = Spinbox(root,
              font='Courier 20',
              values=('sin(x)', 'cos(x)', 'tan(x)', 'cot(x)', 'sec(x)', 'csc(x)', 'sinc(x)',
                      'asin(x)', 'acos(x)', 'atan(x)', 'acot(x)', 'asec(x)', 'acsc(x)',
                      'sinh(x)', 'cosh(x)', 'tanh(x)', 'coth(x)', 'sech(x)',
                      'csch(x)', 'asinh(x)', 'acosh(x)', 'atanh(x)', 'acoth(x)',
                      'asech(x)', 'acsch(x)', 'exp(x)', 'log(x,base)', 'x**(a/b)',
                      'sqrt(x)'), wrap=True, width=15)
scr.grid(column=0, row=3)

root['bg'] = '#0059b3'


def limite():
    fun.set(Limit(fun.get(), x, tf.get()).doit())


def integral():
    fun.set(Integral(fun.get(), (x, xi.get(), xf.get())).doit())


def derivada():
    fun.set(Derivative(fun.get(), x).doit())


def serie():
    fun.set(series(fun.get(), x, 0, s.get()).removeO())


def plotagem():
    plot(fun.get(), fun1.get(),
         (x, -5, 5), line_color=['red', 'black'])


def clear():
    fun.set(e0.delete(0, 'end'), e0.insert(0, '0'))


def clear2():
    fun.set(e5.delete(0, 'end'), e5.insert(0, '0'))


# entrada da função
t1 = Label(root, text='Functions', font="Courier 30",
           bg='#0059b3', fg='black', relief=RIDGE)
t1.grid(column=0, row=2, rowspan=2)
bc = Button(text="Clear", command=clear, width=20, font="Arial 20",
            bg='black', fg='white')
bc.grid(column=2, row=2, rowspan=2)
e0 = Entry(textvar=fun, width=10, font="Courier 30")
e0.grid(column=1, row=2, rowspan=2)
# calculos
b0 = Button(text="Limite", command=limite, width=20, font="Courier 20",
            bg='black', fg='white')
b0.grid(column=0, row=4)
e1 = Entry(textvar=tf, width=10, font="Courier 15")
e1.grid(column=1, row=4)
b1 = Button(text="Derivada", command=derivada, width=20, font="Courier 20",
            bg='black', fg='white')
b1.grid(column=0, row=5)
# e2 = Entry(textvar=td, width=10, font="Arial 10")
# e2.grid(column=1, row=2)
b2 = Button(text="IntegraL", command=integral, width=20, font="Courier 20",
            bg='black', fg='white')
b2.grid(column=0, row=6)
e3 = Entry(textvar=xi, width=10, font="Courier 15")
e3.grid(column=1, row=6)
e4 = Entry(textvar=xf, width=10, font="Courier 15")
e4.grid(column=2, row=6)
b3 = Button(text="Serie", command=serie, width=20, font="Courier 20",
            bg='black', fg='white')
b3.grid(column=0, row=7)
s.grid(column=1, row=7)
b4 = Button(text="Plotar", command=plotagem, width=20, font="Courier 20",
            bg='black', fg='white')
b4.grid(column=0, row=8)
e5 = Entry(textvar=fun1, width=10, font="Courier 30")
e5.grid(column=1, row=3)
bc2 = Button(text="Clear", command=clear2, width=20, font="Courier 20",
             bg='black', fg='white')
bc2.grid(column=2, row=3)
ty = Label(text='Resultado', font="Courier 30", bg='black', fg='white')
ty.grid(column=0, row=0)
t2 = Label(textvar=fun, font="Courier 20",
           bg='#0059b3', fg='white', relief=SUNKEN, wraplength=800)
t2.grid(column=0, row=0, columnspan=5, rowspan=2)


canvas_width = 1000
canvas_height = 1000
c = Canvas(width=canvas_width, height=canvas_height, bg='white')
c.grid(column=6, row=0, columnspan=2, rowspan=10)
sq.grid(column=5, row=1)
sa.grid(column=5, row=2)

b = ['black', 'white', 'green', 'red', 'blue']


def novalinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    c.create_line(x, y, x, y, smooth=TRUE, tags="corrente",
                  width=sq.get(), fill=b[sa.get()-1])


def estendelinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    coords = c.coords("corrente") + [x, y]
    c.coords("corrente", *coords)


def fechalinha(e):
    c.itemconfig("corrente", tags=())


def clear3():
    c.delete(ALL)


c.bind("<Button-1>", novalinha)
c.bind("<B1-Motion>", estendelinha)
c.bind("<ButtonRelease-1>", fechalinha)
z = Button(text="Clear", command=clear3)
z.grid(column=5, row=0)

root.mainloop()
