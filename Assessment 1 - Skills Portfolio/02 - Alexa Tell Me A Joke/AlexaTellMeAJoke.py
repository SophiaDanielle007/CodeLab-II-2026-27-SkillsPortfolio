from tkinter import *

with open("randomJokes.txt", "r") as Jokes:
    myJokes = Jokes.read()

def Switch_frame(frame):
    frame.tkraise()

def show_punchline():
    punchline_label.config(text=myJokes)

root = Tk()
root.title("Alexa, Tell Me A Joke")

home_frame = Frame(root)
home_frame.place(relwidth=1 ,relheight=1)
label1 = Label(home_frame, text="Click On the Button to See A Joke")
label1.pack()
button1 = Button(home_frame, text="Alexa Tell Me A Joke", command=lambda: Switch_frame(jokes_frame))
button1.pack()

jokes_frame = Frame(root, bg="yellow")
jokes_frame.place(relwidth=1, relheight=1)
joke_label = Label(jokes_frame, text="The Joke")
joke_label.pack()
punchline_button = Button(jokes_frame, text="Show Punchline", command=lambda: show_punchline())
punchline_button.pack()
punchline_label = Label(jokes_frame, text="")
punchline_label.pack()
quit_button = Button(jokes_frame, text="Quit", command=lambda: Switch_frame(home_frame))
quit_button.pack()

Switch_frame(home_frame)
root.mainloop()