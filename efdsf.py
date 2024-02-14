import tkinter
from tkinter import ttk
window=tkinter.Tk()
a=0

def count():
    global a
    a += 1
    print(a)
button=ttk.Button(text='Тык',command=count)
button.pack()
window.mainloop()