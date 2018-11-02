import tkinter as tk

win = tk.Tk()
win.title('my win')
win.geometry('300x400')
en = tk.Entry(win,show = None)
en.pack()
def intsert_point():
    var = en.get()
    t.config(state = 'normal')
    t.delete(1.0, tk.END)
    t.insert('insert',var)
    t.config(state='disabled')
def end():
    var = en.get()
    t.config(state='normal')
    t.insert('end',var)
    t.config(state='disabled')
b = tk.Button(win,text = 'insert point',width = 10,height = 2,command = intsert_point)
b2 = tk.Button(win,text = 'insert end',width = 10,height = 2,command = end)
t = tk.Text(win)
b.pack()
b2.pack()
t.pack()


win.mainloop()