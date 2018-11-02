import tkinter as tk

win = tk.Tk()
win.title('my win')
win.geometry('300x100')
var = tk.StringVar()
l = tk.Label(win)
l.pack()

def print_selection(v):
    l.config(text = 'you have select '+v)
s = tk.Scale(win,label = 'try me',from_ = 0,to = 10,orient = tk.HORIZONTAL,length = 200,showvalue = 0,tickinterval = 2,resolution = 0.01,command = print_selection)
s.pack()



win.mainloop()