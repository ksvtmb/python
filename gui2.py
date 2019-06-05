"это я метка"

from tkinter import *
#создание базового окна

root = Tk()
root.title("Это я! метка")
root.geometry("200x50")

#рамка для размещеня элемементов
app = Frame(root)
app.grid()
#создаем метку
lbl = Label(app, text="Вот она я!")
lbl.grid()

#старт событийноо цикла
root.mainloop()
