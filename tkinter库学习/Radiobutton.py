import tkinter as tk

win = tk.Tk()
win.title('my win')
win.geometry('300x400')
var = tk.StringVar()
l = tk.Label(win,bg='yellow',height = 5,text = 'Empty' )
l.pack()

def print_selection():
    l.config(text = 'you have select '+var.get())

r1 = tk.Radiobutton(win,text= 'Option A',variable = var,value='A',command = print_selection)
r2 = tk.Radiobutton(win,text= 'Option B',variable = var,value='B',command = print_selection)
r3 = tk.Radiobutton(win,text= 'Option C',variable = var,value='C',command = print_selection)
r4 = tk.Radiobutton(win,text= 'Option D',variable = var,value='D',command = print_selection)
r1.pack()
r2.pack()
r3.pack()
r4.pack()



win.mainloop()