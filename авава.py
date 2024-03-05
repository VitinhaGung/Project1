import tkinter

from tkinter import messagebox

window=tkinter.Tk()
window.title('ПРИЛОЖЕНИЕ')
window.geometry('450x200')

tkinter.Label(text='Логин: ',font=('Arial',18) ).pack()
entry=tkinter.Entry()
entry.pack()
def func():
    if entry.get()   =="Gamer2000" and  entry.get() in data['users']:
        return messagebox.showinfo('Warning',"Вы ввели верный логин.")
    else:
        return messagebox.showerror('Warning', "Вы ввели неверный логин.")









tkinter.Label(text='Пароль: ',font=('Arial',18) ).pack()
entry1=tkinter.Entry()
entry1.pack()
def func():
    if entry1.get()  =="5555" and entry1.get() == data['users']:
        return messagebox.showinfo('Warning',"Вы успешно вошли!")
    else:
        return messagebox.showerror('Warning', "Вы ввели неверный логин или пароль.")




button=tkinter.Button(text='Войти',font=("Arial",25),command=func).pack()
def start_up():
    import json
    with open("users.json",'r',encoding="utf-8") as f:
        data=json.load(f)
        return data
data=start_up()
print(data)
# def func():
#     if (entry.get() in data['users'].keys() and entry1.get() == data['users'][entry.get()]):
#         return 1
#     else:
#         return 0
window.mainloop()
