from tkinter import *
master = Tk()
Label(master, text='Annual Rate').grid(row=0)
Label(master, text='Number of Payments').grid(row=1)
Label(master, text='Loan Principle').grid(row=2)
Label(master, text='Monthly Payment').grid(row=3)
Label(master, text='Remaining Loan').grid(row=3)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
fb = Button(master, text = 'Final Balance', fg ='black')
fb.grid(row=6,column=0)
mp = Button(master, text = 'Monthly Payment', fg ='black')
mp.grid(row=6,column=1)
qt = Button(master, text ='Quit', fg ='black')
qt.grid(row=6,column=2)
mainloop()
