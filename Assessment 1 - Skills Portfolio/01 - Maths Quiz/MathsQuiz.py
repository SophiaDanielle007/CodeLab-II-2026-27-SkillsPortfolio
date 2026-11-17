from random import randint
from tkinter import *

def show_frame(frame):
    frame.tkraise()

def IsRight():
    while i != 10:
        if entry.get() == str(int3):
            continue

root = Tk()
root.title("Math Quiz")

home_frame = Frame(root)
home_frame.place(relwidth=1 ,relheight=1)

label1 = Label(home_frame, text="Home", font=('Roboto',18))
label1.pack()
label2 = Label(home_frame, text="Choose a level", font=('Roboto',16))
label2.pack()

frame1 = Frame(home_frame, bg="green")
frame1.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button1 = Button(frame1, text="Easy", command=lambda: show_frame(frame_easy))
button1.pack()

frame2= Frame(home_frame, bg="orange")
frame2.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button2 = Button(frame2, text="Medium")
button2.pack()

frame3= Frame(home_frame, bg="red")
frame3.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button3 = Button(frame3, text="Difficult")
button3.pack()

frame_easy = Frame(root, bg="yellow")
frame_easy.place(relwidth=1 ,relheight=1)

for i in range(10):
    int1, int2 = randint(1, 9), randint(1, 9)
    int3 = int1 + int2
    if i == 0:
        question = Label(frame_easy, text=f"What is {int1} + {int2}?")
        question.pack()
        entry = Entry(frame_easy)
        entry.pack()
        check_anwer = Button(frame_easy, text="Check Answer", command=IsRight)
        i=+i

show_frame(home_frame)
root.mainloop()