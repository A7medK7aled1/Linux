from tkinter import *

window_1 = Tk() 


window_1.title("Hello From Tkinter ")


label_1  =Label(window_1 , text = "Ahmed")
window_1.geometry('720x360')

b1  =Button(window_1 , text = "Ahmed")
b2  =Button(window_1 , text = "Ahmed")

b3  =Button(window_1 , text = "Ahmed")

b4  =Button(window_1 , text = "Ahmed")

b1.pack(side = TOP)
b2.pack(side = BOTTOM)
b3.pack(side = RIGHT)
b4.pack(side = LEFT)

label_1.pack(side = TOP)

window_1.mainloop()