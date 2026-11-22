from tkinter import *

# importing the choice function from random module, to be used to randomly select a joke
from random import choice

with open("randomJokes.txt", "r") as Jokes:
    # reads the jokes as separate lines
    myJokes = Jokes.readlines()

# initializing an empty variable where the punchline will later be stored.
current_punchline = ""

# this function will bring the selected frame to the front
def Switch_frame(frame):
    frame.tkraise()

# this function will randomly choose a line with the joke and punchline and will unpack them into separate variables when the line is split. The joke variable is used in the joke_label and the punchline_label text remains empty so it won't show until the user clicks the punchline_button
def show_joke():
    global current_punchline
    joke, current_punchline = choice(myJokes).strip().split("?", 1)
    joke_label.config(text=joke + "?")
    punchline_label.config(text="")

# this function displays the punchline of the joke when the user clicks the punchline_button
def show_punchline():
    punchline_label.config(text=current_punchline)

root = Tk()
root.title("Alexa, Tell Me A Joke")
root.geometry("500x500")
root.resizable(1, 1)

# this is the first frame the user sees
home_frame = Frame(root)
home_frame.place(relwidth=1 ,relheight=1)
label1 = Label(home_frame, text="Click On the Button to See A Joke")
label1.pack()
# this button brings the jokes_frame to the front and updates the joke_label
button1 = Button(home_frame, text="Alexa Tell Me A Joke", command=lambda: [Switch_frame(jokes_frame), show_joke()])
button1.pack()

# this frame contains the joke, the button to show the punchline, the button to show the next joke and the button to quit.
jokes_frame = Frame(root, bg="yellow")
jokes_frame.place(relwidth=1, relheight=1)
joke_label = Label(jokes_frame, text="[The Joke goes here]")
joke_label.pack()
punchline_button = Button(jokes_frame, text="Show Punchline", command=lambda: show_punchline())
punchline_button.pack()
punchline_label = Label(jokes_frame, text="")
punchline_label.pack()
# the show_joke function is called when the user clicks on the next_joke_button
next_joke_button = Button(jokes_frame, text="Next Joke", command=show_joke)
next_joke_button.pack()
quit_button = Button(jokes_frame, text="Quit", command=lambda: Switch_frame(home_frame))
quit_button.pack()

# this is added to ensure that the user sees the home_frame first
Switch_frame(home_frame)
root.mainloop()