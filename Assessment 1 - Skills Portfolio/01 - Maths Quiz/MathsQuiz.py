from random import randint
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

num_of_questions = 10
questions_asked = 0
attempts = 2
score = 0
question_scored = False

def displayMenu(Frame):
    Frame.tkraise()

current_frame = None
def show_frame(frame):
    global current_frame
    current_frame = frame
    frame.tkraise()

def randomInt():
    if current_frame is frame_easy:
        return randint(1, 10), randint(1, 10)
    elif current_frame is frame_medium:
        return randint(10, 100), randint(10, 100)
    elif current_frame is frame_advanced:
        return randint(1000, 10000), randint(1000, 10000)

# this function decides what operator the question will use
def decideOperation():
    # the if statement chooses what operator to use based on what the randint function returns
    return "+" if randint(1, 2) == 1 else "-"

def displayProblem():
    global int1, int2, randoperator, attempts, questions_asked, operation, question_scored

    if current_frame is frame_easy:
        question_label = easy_question
        answer_entry = easy_entry
        feedback_label = easy_message
        next_button = easy_next_button
    elif current_frame is frame_medium:
        question_label = medium_question
        answer_entry = medium_entry
        feedback_label = medium_message
        next_button = medium_next_button
    elif current_frame is frame_advanced:
        question_label = advanced_question
        answer_entry = advanced_entry
        feedback_label = advanced_message
        next_button = advanced_next_button

# if the user has completed all the questions, the message shows "Quiz Complete" and the text in feedback_label is cleared
    if questions_asked >= num_of_questions:
        show_frame(quiz_completed_frame)
        displayResults()
        return

    int1, int2 = randomInt()
    randoperator = decideOperation()
    questions_asked += 1

    question_label.config(text=f"{questions_asked} of {num_of_questions} Questions\n"f"What is {int1} {randoperator} {int2}?")

    answer_entry.delete(0, END)
    attempts = 2
    question_scored = False
    feedback_label.config(text="")
    next_button.config(state=DISABLED)

def IsCorrect(answer, feedback_label, mybutton):
    global attempts, score, question_scored
    # if the selected operator is +, the numbers are added and stored in the int3 var
    if randoperator == "+":
        int3 = int1 + int2
    # if the selected operator is -, the numbers are subtracted and stored in the int3 var
    elif randoperator == "-":
        int3 = int1 - int2

# the input is retireved from the entry widget
    a = answer.get().strip()

    # since the retrieved input is a str format, int3 is also converted to a str
    if a == str(int3):
        feedback_label.config(text="Correct! Click Next Question to continue.")
        mybutton.config(state=NORMAL, text="Next Question")
        # tracks if the current question has already been scored. This prevents points being added again when the user clicks the "Check Answer" again.
        if not question_scored:
            if attempts == 2:
                score += 10
            else:
                score += 5
            question_scored = True
    else:
        # the attempts var is a counter, if the user attempts again, 1 is subtracted.
        attempts -= 1
        if attempts > 0:
            feedback_label.config(text=f"Wrong. You have {attempts} attempt left.")
            # the button to move to the next question is disabled until the user completes the question
            mybutton.config(state=DISABLED, text="Complete Question First")
        else:
            feedback_label.config(text=f"No attempts left. The answer was {int3}.")
            mybutton.config(state=NORMAL, text="Next Question")

def displayResults():
    score_label.config(text=f"You have scored {score}")

# brings the home_frame to the front and resets everything when the user quits the game
def Go_Home(HomeFrame):
    global questions_asked, attempts, score, question_scored
    HomeFrame.tkraise()
    questions_asked = 0
    attempts = 2
    score = 0
    question_scored = False


root = Tk()
root.title("Math Quiz")
root.geometry("500x500")
root.resizable(1, 1)
root.iconbitmap("asset 2.ico")

# this is the first frame the user sees
home_frame = Frame(root)
home_frame.place(relwidth=1 ,relheight=1)
img = ImageTk.PhotoImage(Image.open("asset 1.webp"))
home_content = Label(home_frame, image=img, bd=0)
home_content.place(relwidth=1, relheight=1)

label1 = Label(home_content, text="Maths Quiz", font=('Roboto', 18, 'bold'), width=11, bg="#78A9F0", bd=1)
label1.place(relx=0.5, rely=0.47, anchor=CENTER)
# this button will bring the Menu_Frame to the front
button1 = Button(home_content, text="Menu", font=('Roboto', 10), width=20, bg="#D7FF00", command=lambda: displayMenu(Menu_Frame))
button1.place(relx=0.5, rely=0.53, anchor=CENTER)

# this frame contains the buttons to choose what level of dificulty the user wants
Menu_Frame = Frame(root)
Menu_Frame.place(relwidth=1 ,relheight=1)
menu_content = Frame(Menu_Frame)
menu_content.place(relx=0.5, rely=0.5, anchor=CENTER)

label2 = Label(menu_content, text="Choose a level", font=('Roboto', 16, 'bold'))
label2.pack()

button1 = Button(menu_content, text="Easy", bg="green", font=('Roboto', 10), width=20, command=lambda: [show_frame(frame_easy), displayProblem()])
button1.pack(pady=5)

button2 = Button(menu_content, text="Moderate", bg="yellow", font=('Roboto', 10), width=20, command=lambda: [show_frame(frame_medium), displayProblem()])
button2.pack(pady=5)

button3 = Button(menu_content, text="Advanced", bg="red", font=('Roboto', 10), width=20, command=lambda: [show_frame(frame_advanced), displayProblem()])
button3.pack(pady=5)

# this frame shows the easy question
frame_easy = Frame(root)
frame_easy.place(relwidth=1 ,relheight=1)
easy_content = Frame(frame_easy)
easy_content.place(relx=0.5, rely=0.5, anchor=CENTER)

# this label will display the question
easy_question = Label(easy_content, text="", font=('Roboto', 10), bg="light grey", width=20, height=3)
easy_question.pack(fill=X, pady=5)

# this is where the user enters their answer
easy_entry = Entry(easy_content, font=('Roboto', 10), width=20)
easy_entry.pack(fill=X, pady=5)

# this button checks if the answer in easy_entry is right or wrong and displays a message
easy_check_button = Button(easy_content, text="Check Answer", font=('Roboto', 10), bg="#39FF14", width=20, command=lambda: IsCorrect(easy_entry, easy_message, easy_next_button))
easy_check_button.pack(fill=X, pady=5)

# this label is where the message after the question is checked will be displayed
easy_message = Label(easy_content, text="", font=('Roboto', 10))
easy_message.pack(fill=X, pady=5)

# this button allows the user to go to the next question, the button remains disabled until the user enters a correct answer or they have run out of attempts
easy_next_button = Button(easy_content, text="Next Question", font=('Roboto', 10), width=20, command=displayProblem, state=DISABLED)
easy_next_button.pack(fill=X, pady=5)

# this button allows the user to quit the game at any time
goto_home_frame = Button(easy_content, text="Home", font=('Roboto', 10), bg="#FF3131", width=20, command=lambda: Go_Home(home_frame))
goto_home_frame.pack(fill=X, pady=5)

frame_medium = Frame(root)
frame_medium.place(relwidth=1 ,relheight=1)
medium_content = Frame(frame_medium)
medium_content.place(relx=0.5, rely=0.5, anchor=CENTER)

medium_question = Label(medium_content, text="", font=('Roboto', 10), bg="light grey", width=20, height=3)
medium_question.pack(fill=X, pady=5)

medium_entry = Entry(medium_content, font=('Roboto', 10), width=20)
medium_entry.pack(fill=X, pady=5)

medium_check_button = Button(medium_content, text="Check Answer", font=('Roboto', 10), bg="#39FF14", width=20, command=lambda: IsCorrect(medium_entry, medium_message, medium_next_button))
medium_check_button.pack(fill=X, pady=5)

medium_message = Label(medium_content, text="", font=('Roboto', 10))
medium_message.pack(fill=X, pady=5)

medium_next_button = Button(medium_content, text="Next Question", font=('Roboto', 10), width=20, command=displayProblem, state=DISABLED)
medium_next_button.pack(fill=X, pady=5)

goto_home_frame = Button(medium_content, text="Home", font=('Roboto', 10), bg="#FF3131", width=20, command=lambda: Go_Home(home_frame))
goto_home_frame.pack(fill=X, pady=5)

frame_advanced = Frame(root)
frame_advanced.place(relwidth=1 ,relheight=1)
advanced_content = Frame(frame_advanced)
advanced_content.place(relx=0.5, rely=0.5, anchor=CENTER)

advanced_question = Label(advanced_content, text="", font=('Roboto', 10), bg="light grey", width=20, height=3)
advanced_question.pack(fill=X, pady=5)

advanced_entry = Entry(advanced_content, font=('Roboto', 10), width=20)
advanced_entry.pack(fill=X, pady=5)

advanced_check_button = Button(advanced_content, text="Check Answer", font=('Roboto', 10), bg="#39FF14", width=20, command=lambda: IsCorrect(advanced_entry, advanced_message, advanced_next_button))
advanced_check_button.pack(fill=X, pady=5)

advanced_message = Label(advanced_content, text="", font=('Roboto', 10))
advanced_message.pack(fill=X, pady=5)

advanced_next_button = Button(advanced_content, text="Next Question", font=('Roboto', 10), width=20, command=displayProblem, state=DISABLED)
advanced_next_button.pack(fill=X, pady=5)

goto_home_frame = Button(advanced_content, text="Home", font=('Roboto', 10), bg="#FF3131", width=20, command=lambda: Go_Home(home_frame))
goto_home_frame.pack(fill=X, pady=5)

quiz_completed_frame = Frame(root)
quiz_completed_frame.place(relwidth=1 ,relheight=1)
results_content = Frame(quiz_completed_frame)
results_content.place(relx=0.5, rely=0.5, anchor=CENTER)
mylabel = Label(results_content, text="Quiz Completed", font=('Roboto', 10))
mylabel.pack()
score_label = Label(results_content, text="", font=('Roboto', 10))
score_label.pack()
displayResults()

show_frame(home_frame)
root.mainloop()