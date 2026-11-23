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
root.iconbitmap("asset 1.ico")

# this is the first frame the user sees
home_frame = Frame(root, bg="#E8EFE7")
home_frame.place(relwidth=1 ,relheight=1)
home_content = Frame(home_frame, bg="#F8FAF6", padx=36, pady=30)
home_content.place(relx=0.5, rely=0.5, anchor=CENTER)
labels_row = Frame(home_content, bg="#F8FAF6")
labels_row.pack()
label1 = Label(labels_row, text="Need A Joke?", font=('Roboto', 14, 'bold'), bg="#F8FAF6", fg="#263A32")
label1.pack(side=LEFT)
label2 = Label(labels_row, text="Ask Alexa", font=('Roboto', 14), bg="#F8FAF6", fg="#638276")
label2.pack(side=LEFT)
# this button brings the jokes_frame to the front and updates the joke_label
button1 = Button(home_content, text="Alexa Tell Me A Joke", width=30, font=('Roboto', 10), bg="#638276", fg="white", activebackground="#506E62", activeforeground="white", relief=FLAT, command=lambda: [Switch_frame(jokes_frame), show_joke()])
button1.pack(pady=(12, 0), ipady=4)

# this frame contains the joke, the button to show the punchline, the button to show the next joke and the button to quit.
jokes_frame = Frame(root, bg="#E8EFE7")
jokes_frame.place(relwidth=1, relheight=1)
jokes_frame_content = Frame(jokes_frame, bg="#F8FAF6", padx=36, pady=30)
jokes_frame_content.place(relx=0.5, rely=0.5, anchor=CENTER)
heading_label = Label(jokes_frame_content, text="A MOMENT OF FUN", font=('Roboto', 11, 'bold'), bg="#F8FAF6", fg="#638276")
heading_label.pack(pady=(0, 14))
joke_label = Label(jokes_frame_content, text="", font=('Roboto', 16), bg="#F8FAF6", fg="#263A32", wraplength=380, justify=CENTER)
joke_label.pack(pady=(0, 12))
punchline_button = Button(jokes_frame_content, text="Show Punchline", width=20, font=('Roboto', 10), bg="#638276", fg="white", activebackground="#506E62", activeforeground="white", relief=FLAT, command=show_punchline)
punchline_button.pack(pady=5, ipady=4)
punchline_label = Label(jokes_frame_content, text="", font=('Roboto', 14), bg="#F8FAF6", fg="#638276", wraplength=380, justify=CENTER)
punchline_label.pack(pady=8)
# the show_joke function is called when the user clicks on the next_joke_button
next_joke_button = Button(jokes_frame_content, text="Next Joke", width=20, font=('Roboto', 10), bg="#E0E8DE", fg="#263A32", activebackground="#D1DDD0", activeforeground="#263A32", relief=FLAT, command=show_joke)
next_joke_button.pack(pady=5, ipady=4)
quit_button = Button(jokes_frame_content, text="Back to Home", width=20, font=('Roboto', 10), bg="#E0E8DE", fg="#263A32", activebackground="#D1DDD0", activeforeground="#263A32", relief=FLAT, command=lambda: Switch_frame(home_frame))
quit_button.pack(pady=(5, 0), ipady=4)

# this is added to ensure that the user sees the home_frame first
Switch_frame(home_frame)
root.mainloop()