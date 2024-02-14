import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Приложение')
window.geometry('1200x720')
# window.minsize(200,200)
# window.maxsize(1920,1920)
# window.resizable(False,True)
# window.attributes('-fullscreen',False)
# window.attributes("-alpha",1)
# window.attributes('-toolwindow',True)
# window['bg']='#1141f0'
# label=tkinter.Label(text='Привет')
# label.pack()
ttk.Label(text='Привет')
          #      background='purple',
          # foreground='black',
          # font=('Arial,20')).pack(expand=True)
# label.pack(anchor='se',expand=True)
# label.pack(fill='both',pady=50,padx=[20,100])
# label.pack(side='left')
# label.place(x=100,y=100,width=100,height=100)
# entry=ttk.Entry(width=60)
# entry.pack()
# entry.insert(0,'Привет')
# entry.get()
# entry.delete(0,'end')
a=0
def count():
    global a
    a +=1
    print(a)
button=ttk.Button(text='Тык')
button.pack()
window.mainloop()
