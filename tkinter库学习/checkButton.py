import tkinter as tk

win = tk.Tk()
win.title('my win')
win.geometry('300x100')
l = tk.Label(win)
l.pack()
var1 = tk.IntVar()
var2 = tk.IntVar()


def print_selection():
    if (var1.get() == 0) & (var2.get() == 0):
        l.config(text='i do not love either')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='i love C++')
    elif (var1.get() == 1) & (var2.get() == 1):
        l.config(text='i love both')
    else:
        l.config(text='i love python')


s1 = tk.Checkbutton(win, text='python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
s2 = tk.Checkbutton(win, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
s1.pack()
s2.pack()

win.mainloop()
