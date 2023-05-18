from tkinter import *

def FUNC():
    x=0
    x=x+1
    print("Press = ",x)







window_1 = Tk() 


window_1.title("Hello From Tkinter ")


label_1  =Label(window_1 , text = "Ahmed")
window_1.geometry('720x360')

Label(window_1 , text = "Image Button " ,bd=7,background="blue", font = ('Verdana', 30)).pack(side=TOP)

b1  =Button(window_1 , text = "Exit",bd=5 ,background="red",command = window_1.destroy)
photo_1 = PhotoImage(file='download.png')

photo_1 = photo_1.subsample(2,2)

b2  =Button(window_1 , text = "Increment The button " , bd = '5' ,image=photo_1)

b2.pack(side = TOP)




b1.pack(side = BOTTOM)


label_1.pack(side = TOP)


window_1.mainloop()