import tkinter
from turtle import left

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=400)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial",24))
my_label.pack()






window.mainloop()