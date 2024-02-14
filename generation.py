import tkinter
from tkinter import ttk

def generate_password(dlina=6):
    import random
    password=''
    alphabet='1234567890id23tyuioihgfdsasdfbnmFDFSF00'
    for i in range(dlina):
     password = password + random.choice(alphabet)
    entry.delete(0,'end')
    entry.insert(0,password)
dlina=10
window=tkinter.Tk()


window['bg']="pink"
# ttk.Button(background='red',foreground='yellow',font=('Arial',20))

window.title('Генератор паролей')
window.geometry('450x200')
window.resizable(False,False)
entry=ttk.Entry(width=dlina,justify='c',background='green',foreground='green',font=('Arial',20))
entry.place(width=400,height=50,x=10,y=30)

button=ttk.Button(text='Нажми',command=generate_password)
button.place(width=150,height=80,x=125,y=80)

window.mainloop()
