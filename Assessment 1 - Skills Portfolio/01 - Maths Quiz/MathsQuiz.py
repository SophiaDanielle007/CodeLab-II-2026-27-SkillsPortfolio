from random import randint
from tkinter import *

def Show_Menu(Frame):
    Frame.tkraise()

current_frame = None
def show_frame(frame):
    global current_frame
    current_frame = frame
    frame.tkraise()

num_of_questions = 10
questions_asked = 0
attempts = 2

def display_Problem():
    global int1, int2, int3, attempts, questions_asked, mybutton

    if current_frame is frame_easy:
        int1 = randint(1, 10)
        int2 = randint(1, 10)
        question_label = easy_question
        answer_entry = easy_entry
        feedback_label = easy_message
    elif current_frame is frame_medium:
        int1 = randint(10, 100)
        int2 = randint(10, 100)
        question_label = medium_question
        answer_entry = medium_entry
        feedback_label = medium_message
    elif current_frame is frame_advanced:
        int1 = randint(1000, 10000)
        int2 = randint(1000, 10000)
        question_label = advanced_question
        answer_entry = advanced_entry
        feedback_label = advanced_message
    
    operation = randint(1, 2)

    my_questions = {1: f"What is {int1} + {int2}?",
                    2: f"What is {int1} - {int2}?"}

    answers = {1: int1 + int2,
               2: int1 - int2}

    questions_asked += 1
    question_label.config(text=f"{questions_asked} of {num_of_questions} Questions\n" f"{my_questions[operation]}")
    int3 = answers[operation]
    answer_entry.delete(0, END)
    attempts = 2
    feedback_label.config(text="")
    mybutton.config(state=DISABLED)

    if questions_asked == num_of_questions:
        question_label.config(text="Quiz complete!")
        feedback_label.config(text="")

def Is_correct(answer, feedback_label, mybutton):
    global attempts
    a = answer.get().strip()

    if a == str(int3):
        feedback_label.config(text="Correct! Click Next Question to continue.")
        mybutton.config(state=NORMAL, text="Next Question")
    else:
        attempts -= 1
        if attempts > 0:
            feedback_label.config(text=f"Wrong. You have {attempts} attempt left.")
            mybutton.config(state=DISABLED, text="Complete Question First")
        else:
            feedback_label.config(text=f"No attempts left. The answer was {int3}.")
            mybutton.config(state=NORMAL, text="Next Question")

score = 0
def display_Results(frame):
    frame.tkraise()

def Go_Home(HomeFrame):
    HomeFrame.tkraise()

root = Tk()
root.title("Math Quiz")

home_frame = Frame(root)
home_frame.place(relwidth=1 ,relheight=1)

label1 = Label(home_frame, text="Home", font=('Roboto',18))
label1.pack()
button1 = Button(home_frame, text="Menu", command=lambda: Show_Menu(Menu_Frame))
button1.pack()

Menu_Frame = Frame(root)
Menu_Frame.place(relwidth=1 ,relheight=1)

label2 = Label(Menu_Frame, text="Choose a level", font=('Roboto',16))
label2.pack()

frame1 = Frame(Menu_Frame)
frame1.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button1 = Button(frame1, text="Easy", command=lambda: [show_frame(frame_easy), display_Problem()])
button1.pack()

frame2= Frame(Menu_Frame)
frame2.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button2 = Button(frame2, text="Medium", command=lambda: [show_frame(frame_medium), display_Problem()])
button2.pack()

frame3= Frame(Menu_Frame)
frame3.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button3 = Button(frame3, text="Difficult", command=lambda: [show_frame(frame_advanced), display_Problem()])
button3.pack()

frame_easy = Frame(root)
frame_easy.place(relwidth=1 ,relheight=1)

easy_question = Label(frame_easy, text="")
easy_question.pack()

easy_entry = Entry(frame_easy)
easy_entry.pack()

easy_check_button = Button(frame_easy, text="Check Answer", command=lambda: Is_correct(easy_entry, easy_message, easy_next_button))
easy_check_button.pack()

easy_message = Label(frame_easy, text="")
easy_message.pack()

easy_next_button = Button(frame_easy, text="Next Question", command=display_Problem, state=DISABLED)
easy_next_button.pack()

goto_home_frame = Button(frame_easy, text="Home", command=lambda: Go_Home(home_frame))
goto_home_frame.pack()

frame_medium = Frame(root)
frame_medium.place(relwidth=1 ,relheight=1)

medium_question = Label(frame_medium, text="")
medium_question.pack()

medium_entry = Entry(frame_medium)
medium_entry.pack()

medium_check_button = Button(frame_medium, text="Check Answer", command=lambda: Is_correct(medium_entry, medium_message, medium_next_button))
medium_check_button.pack()

medium_message = Label(frame_medium, text="")
medium_message.pack()

medium_next_button = Button(frame_medium, text="Next Question", command=display_Problem, state=DISABLED)
medium_next_button.pack()

goto_home_frame = Button(frame_medium, text="Home", command=lambda: Go_Home(home_frame))
goto_home_frame.pack()

frame_advanced = Frame(root)
frame_advanced.place(relwidth=1 ,relheight=1)

advanced_question = Label(frame_advanced, text="")
advanced_question.pack()

advanced_entry = Entry(frame_advanced)
advanced_entry.pack()

advanced_check_button = Button(frame_advanced, text="Check Answer", command=lambda: Is_correct(advanced_entry, advanced_message, advanced_next_button))
advanced_check_button.pack()

advanced_message = Label(frame_advanced, text="")
advanced_message.pack()

advanced_next_button = Button(frame_advanced, text="Next Question", command=display_Problem, state=DISABLED)
advanced_next_button.pack()

goto_home_frame = Button(frame_advanced, text="Home", command=lambda: Go_Home(home_frame))
goto_home_frame.pack()

results_frame  = Frame(root)
results_frame.place(relwidth=1, relheight=1)

results = Label(results_frame, text=f"You scored {score} of 100")
results.pack()

show_frame(home_frame)
root.mainloop()