import tkinter as tk

win = tk.Tk()
win.title('my win')
win.geometry('300x400')
var = tk.StringVar()
l = tk.Label(win,textvariable =var,bg='yellow',width = 15,height = 5 )
l.pack()
def print_selection():
    var.set(lb.get(lb.curselection()))
b = tk.Button(win,text = 'print selection',width = 10,height = 2,command = print_selection)
b.pack()
var2 = tk.StringVar()
var2.set((11,22,44,55))
lb = tk.Listbox(win,listvariable=var2 )
list_item = [55,33,88,9]
for item in list_item:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()



win.mainloop()