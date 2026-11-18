from random import randint
from tkinter import *

current_frame = None
def show_frame(frame):
    global current_frame
    current_frame = frame
    frame.tkraise()

num_of_questions = 10
questions_asked = 0
attempts = 4

def next_question():
    global int1, int2, int3, attempts, questions_asked

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


    if questions_asked == num_of_questions:
        question_label.config(text="Quiz complete!")
        feedback_label.config(text="")
    
    operation = randint(1, 3)

    my_questions = {1: f"What is {int1} + {int2}?",
                    2: f"What is {int1} - {int2}?",
                    3: f"What is {int1} * {int2}?"}

    answers = {1: int1 + int2,
               2: int1 - int2,
               3: int1 * int2}

    questions_asked += 1
    question_label.config(text=f"{questions_asked} of {num_of_questions} Questions\n" f"{my_questions[operation]}")
    int3 = answers[operation]
    answer_entry.delete(0, END)
    attempts = 4
    feedback_label.config(text="")


def check_if_correct(answer, feedback_label):
    global attempts
    a = answer.get().strip()

    if a == str(int3):
        feedback_label.config(text="Correct! Click Next Question to continue.")
    else:
        attempts -= 1
        if attempts > 0:
            feedback_label.config(text=f"Wrong. You have {attempts} attempts left.")
        else:
            feedback_label.config(text=f"No attempts left. The answer was {int3}.")


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
button1 = Button(frame1, text="Easy", command=lambda: [show_frame(frame_easy), next_question()])
button1.pack()

frame2= Frame(home_frame, bg="orange")
frame2.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button2 = Button(frame2, text="Medium", command=lambda: [show_frame(frame_medium), next_question()])
button2.pack()

frame3= Frame(home_frame, bg="red")
frame3.pack(side=LEFT, expand=YES, fill=X, anchor=N)
button3 = Button(frame3, text="Difficult")
button3.pack()

frame_easy = Frame(root)
frame_easy.place(relwidth=1 ,relheight=1)

easy_question = Label(frame_easy, text="")
easy_question.pack()

easy_entry = Entry(frame_easy)
easy_entry.pack()

easy_check_button = Button(frame_easy, text="Check Answer", command=lambda: check_if_correct(easy_entry, easy_message))
easy_check_button.pack()

easy_message = Label(frame_easy, text="")
easy_message.pack()

easy_next_button = Button(frame_easy, text="Next Question", command=next_question)
easy_next_button.pack()

frame_medium = Frame(root)
frame_medium.place(relwidth=1 ,relheight=1)

medium_question = Label(frame_medium, text="")
medium_question.pack()

medium_entry = Entry(frame_medium)
medium_entry.pack()

medium_check_button = Button(frame_medium, text="Check Answer", command=lambda: check_if_correct(medium_entry, medium_message))
medium_check_button.pack()

medium_message = Label(frame_medium, text="")
medium_message.pack()

medium_next_button = Button(frame_medium, text="Next Question", command=next_question)
medium_next_button.pack()

show_frame(home_frame)
root.mainloop()