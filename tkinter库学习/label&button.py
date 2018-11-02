import tkinter as tk

win = tk.Tk()
win.title('my win')
win.geometry('200x100')
var = tk.StringVar()
l =  tk.Label(win,textvariable = var,bg = 'red',font = ('Arial',12),width = 15,height = 2)
l.pack()
on_hit = False
def hti():
    global on_hit
    if on_hit==False:
        on_hit = True
        var.set('hit me')
    else:
        on_hit = False
        var.set('')
b = tk.Button(win,text = 'hit me',width = 10,height = 5,command = hti)
b.pack()
win.mainloop()