from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Student Manager")
root.geometry("500x500")
root.resizable(1, 1)
root.iconbitmap("asset 1.ico")

with open("studentMarks.txt", "r") as file:
    # next() skips the first line
    next(file)
    student_info = file.readlines()

def unpack_file():
    # initializing vars with empty lists
    student_nums = []
    student_names = []
    mark1s = []
    mark2s = []
    mark3s = []
    exam_marks = []

    # each line is split and unpacked into temporary vars. They are then appended into the vars that were intialized earlier.
    for line in student_info:
        num, name, mark1, mark2, mark3, exam = line.strip().split(",", 5)

        student_nums.append(int(num))
        student_names.append(name)
        mark1s.append(int(mark1))
        mark2s.append(int(mark2))
        mark3s.append(int(mark3))
        exam_marks.append(int(exam))

    return student_nums, student_names, mark1s, mark2s, mark3s, exam_marks

total_coursework_marks = []
def sum_coursework_marks():
    # used zip() in the list comprehension to avoid having to manage indexes
    total = [m1 + m2 + m3 for m1, m2, m3 in zip(mark1s, mark2s, mark3s)]
    total_coursework_marks.extend(total)

overvall_percentage = []
def find_overvall_percentage():
    # this calculates the total marks and convert it to a %
    total = [(coursework + exam) / 160 * 100 for coursework, exam in zip(total_coursework_marks, exam_marks)]
    # used extend() not append() so it won't return a nested list
    overvall_percentage.extend(total)

student_grade = []
def find_student_grade():
    for mark in overvall_percentage:
        if mark >= 70:
            student_grade.append("A")
        elif mark >= 60:
            student_grade.append("B")
        elif mark >= 50:
            student_grade.append("C")
        elif mark >= 40:
            student_grade.append("D")
        elif mark < 40:
            student_grade.append("F")

def show_frame(frame):
    frame.tkraise()

def search_by_name():
    name = entry1.get().strip().casefold()
    index = None
    for i, student_name in enumerate(student_names):
        if student_name.casefold() == name:
            index = i
            break

    record_info =(f"Name: {student_names[index]}\n" f"Student Number: {student_nums[index]}\n" f"Total Coursework Mark: {total_coursework_marks[index]}\n" f"Exam Mark: {exam_marks[index]}\n" f"Overall Percentage: {overvall_percentage[index]:.1f}%\n" f"Grade: {student_grade[index]}")
        
    messagebox.showinfo("Record Found", record_info, parent=root)

def search_by_ID():
    id_num = int(entry2.get().strip())
    index = student_nums.index(id_num)

    record_info =(f"Name: {student_names[index]}\n" f"Student Number: {student_nums[index]}\n" f"Total Coursework Mark: {total_coursework_marks[index]}\n" f"Exam Mark: {exam_marks[index]}\n" f"Overall Percentage: {overvall_percentage[index]:.1f}%\n" f"Grade: {student_grade[index]}")
    
    messagebox.showinfo("Record Found", record_info, parent=root)

def display_average_marks():
    average = sum(overvall_percentage) / len(overvall_percentage)
    average_marks_label.config(text=f"Average Percentage Mark: {average:.1f}%")

def show_score(which):
    total_scores = [coursework + exam for coursework, exam in zip(total_coursework_marks, exam_marks)]
    score = max(total_scores) if which == "Highest" else min(total_scores)
    index = total_scores.index(score)

    messagebox.showinfo(
        f"{which} Total Score",
        f"Name: {student_names[index]}\n"
        f"Student Number: {student_nums[index]}\n"
        f"Total Score: {score}",
        parent=root,
    )

def add_record():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    student_id = student_id_entry.get().strip()
    mark1 = mark1_entry.get().strip()
    mark2 = mark2_entry.get().strip()
    mark3 = mark3_entry.get().strip()
    exam = exam_mark_entry.get().strip()

    # used a try and except statement so user will know if the record was successfully added or not
    try:
        with open("studentMarks.txt", "a") as file:
            file.write(f"{student_id},{first_name} {last_name},{mark1},{mark2},{mark3},{exam}\n")
    except OSError as error:
        messagebox.showinfo(
            "Save Failed",
            f"Could not save the student record:\n{error}",
            parent=root,
        )
    else:
        messagebox.showinfo(
            "Record Added",
            f"Record for {first_name} {last_name} was added.",
            parent=root,
        )

student_nums, student_names, mark1s, mark2s, mark3s, exam_marks = unpack_file()
sum_coursework_marks()
find_overvall_percentage()
find_student_grade()

img = ImageTk.PhotoImage(Image.open("asset 2.jpg"))
menu_frame = Frame(root)
menu_frame.place(relwidth=1 ,relheight=1)
menu_background = Label(menu_frame, image=img)
menu_background.place(relwidth=1, relheight=1)
menu_content = Frame(menu_frame, bg="#F4F8FC", padx=20, pady=16)
menu_content.place(relx=0.5, rely=0.5, anchor=CENTER)
title = Label(menu_content, text="Student Manager", font=("Roboto", 20, "bold"), bg="#F4F8FC", fg="#23415A")
title.pack()
button1 = Button(menu_content, text="View All Student Records", width=30, height=2, command=lambda: show_frame(student_records_frame), bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
button1.pack(pady=4)
button2 = Button(menu_content, text="View Individual Student Record", width=30, height=2, command= lambda: show_frame(individual_student_frame), bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
button2.pack(pady=4)
button3 = Button(menu_content, text="Show Student With Highest Total Score", width=30, height=2, command=lambda: show_score("Highest"), bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
button3.pack(pady=4)
button4 = Button(menu_content, text="Show Student With Lowest Total Score", width=30, height=2, command=lambda: show_score("Lowest"), bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
button4.pack(pady=4)
button5 = Button(menu_content, text="Add Student Record", width=30, height=2, command=lambda: show_frame(add_record_frame), bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
button5.pack(pady=4)

student_records_frame = Frame(root)
student_records_frame.place(relwidth=1 ,relheight=1)
student_records_background = Label(student_records_frame, image=img)
student_records_background.place(relwidth=1, relheight=1)
student_records_background.lower()
student_records_content = Frame(student_records_frame, bg="#F4F8FC", padx=8, pady=8)
student_records_content.place(relx=0.5, rely=0.05, anchor=N)

# Adds light spacing between table columns.
for col in range(6):
    student_records_content.grid_columnconfigure(col, pad=3)

records_title = Label(student_records_content, text="Student Records", font=("Roboto", 16, "bold"), bg="#F4F8FC", fg="#23415A")
records_title.grid(row=0, column=0, columnspan=6, pady=(0, 12))

# the var columns contains a list of tuples containing the column header and column items.
columns = [
    ("Student Name", student_names),
    ("Student Number", student_nums),
    ("Total Coursework Marks", total_coursework_marks),
    ("Exam Mark", exam_marks),
    # the list comprehension formats the items in the list overall_percentage to 1 decimal point.
    ("Overall Percentage", [f"{mark:.1f}%" for mark in overvall_percentage]),
    ("Student Grade", student_grade),
]

# Displays the headings above the student data.
for col, (heading, values) in enumerate(columns):
    Label(student_records_content, text=heading, font=("Roboto", 10, "bold"), bg="#DCEAF5", fg="#23415A", padx=6, pady=7, wraplength=110, justify=CENTER, relief=SOLID, bd=1).grid(row=1, column=col, sticky=NSEW)
    for row, value in enumerate(values, start=2):
        Label(student_records_content, text=value, bg="white", fg="#333333", padx=6, pady=5, relief=SOLID, bd=1).grid(row=row, column=col, sticky=NSEW)

# The summary rows follow the last student row.
summary_row = len(student_names) + 2
num_of_students_label = Label(student_records_content, text=f"Number of Students: {len(student_names)}", font=("Roboto", 10, "bold"), bg="#F4F8FC", fg="#23415A")
num_of_students_label.grid(row=summary_row, column=0, columnspan=6, sticky=E, pady=(8, 2))
average_marks_label = Label(student_records_content, text="", font=("Roboto", 10, "bold"), bg="#F4F8FC", fg="#23415A")
average_marks_label.grid(row=summary_row + 1, column=0, columnspan=6, sticky=E, pady=2)
display_average_marks()

go_home_button = Button(student_records_content, text="Go Home", padx=10, command=lambda: show_frame(menu_frame), bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
go_home_button.grid(row=summary_row + 2, column=0, columnspan=6, sticky=E, pady=(4, 0))

individual_student_frame = Frame(root)
individual_student_frame.place(relwidth=1, relheight=1)
individual_student_background = Label(individual_student_frame, image=img)
individual_student_background.place(relwidth=1, relheight=1)
individual_student_background.lower()
individual_student_content = Frame(individual_student_frame, bg="#F4F8FC", padx=24, pady=20)
individual_student_content.place(relx=0.5, rely=0.5, anchor=CENTER)

Label1 = Label(individual_student_content, text="Search By Name", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
Label1.pack(pady=(0, 5))
entry1 = Entry(individual_student_content, width=24)
entry1.pack(ipady=3, pady=(0, 10))
search_button1 = Button(individual_student_content, text="Search", width=20, command=search_by_name, bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
search_button1.pack(pady=(0, 16))

Label2 = Label(individual_student_content, text="Search By ID Number", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
Label2.pack(pady=(0, 5))
entry2 = Entry(individual_student_content, width=24)
entry2.pack(ipady=3, pady=(0, 10))
search_button2 = Button(individual_student_content, text="Search", width=20, command=search_by_ID, bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
search_button2.pack()
search_home_button = Button(individual_student_content, text="Go Home", width=20, command=lambda: show_frame(menu_frame), bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED", relief=FLAT)
search_home_button.pack(pady=(16, 0))

add_record_frame = Frame(root)
add_record_frame.place(relwidth=1, relheight=1)
add_record_background = Label(add_record_frame, image=img)
add_record_background.place(relwidth=1, relheight=1)
add_record_background.lower()
add_record_content = Frame(add_record_frame, bg="#F4F8FC", padx=20, pady=16)
add_record_content.place(relx=0.5, rely=0.5, anchor=CENTER)

for row in range(8):
    add_record_content.grid_rowconfigure(row, pad=7)

first_name_label = Label(add_record_content, text="Enter First Name", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
first_name_label.grid(row=0, column=0, sticky=E)
first_name_entry = Entry(add_record_content, width=20, bg="white")
first_name_entry.grid(row=0, column=1, ipady=3)

last_name_label = Label(add_record_content, text="Enter Last Name", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
last_name_label.grid(row=1, column=0, sticky=E)
last_name_entry = Entry(add_record_content, width=20, bg="white")
last_name_entry.grid(row=1, column=1, ipady=3)

student_id_label = Label(add_record_content, text="Enter Student ID", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
student_id_label.grid(row=2, column=0, sticky=E)
student_id_entry = Entry(add_record_content, width=20, bg="white")
student_id_entry.grid(row=2, column=1, ipady=3)

mark1_label = Label(add_record_content, text="Enter Coursework Mark 1", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
mark1_label.grid(row=3, column=0, sticky=E)
mark1_entry = Entry(add_record_content, width=20, bg="white")
mark1_entry.grid(row=3, column=1, ipady=3)

mark2_label = Label(add_record_content, text="Enter Coursework Mark 2", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
mark2_label.grid(row=4, column=0, sticky=E)
mark2_entry = Entry(add_record_content, width=20, bg="white")
mark2_entry.grid(row=4, column=1, ipady=3)

mark3_label = Label(add_record_content, text="Enter Coursework Mark 3", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
mark3_label.grid(row=5, column=0, sticky=E)
mark3_entry = Entry(add_record_content, width=20, bg="white")
mark3_entry.grid(row=5, column=1, ipady=3)

exam_mark_label = Label(add_record_content, text="Enter Exam Mark", font=("Roboto", 10), bg="#F4F8FC", fg="#23415A")
exam_mark_label.grid(row=6, column=0, sticky=E)
exam_mark_entry = Entry(add_record_content, width=20, bg="white")
exam_mark_entry.grid(row=6, column=1, ipady=3)

submit_button = Button(add_record_content, text="Submit Record", command=add_record, relief=FLAT, bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED")
submit_button.grid(row=7, columnspan=2, sticky=EW)
go_home_button = Button(add_record_content, text="Go Home", command=lambda: show_frame(menu_frame), relief=FLAT, bg="#DCEAF5", fg="#23415A", activebackground="#C9DDED")
go_home_button.grid(row=8, columnspan=2, sticky=EW)

show_frame(menu_frame)
root.mainloop()