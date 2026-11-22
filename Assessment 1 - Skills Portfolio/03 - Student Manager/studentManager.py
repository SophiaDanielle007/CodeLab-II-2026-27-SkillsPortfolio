from tkinter import *
from tkinter import messagebox
from functools import reduce

root = Tk()
root.title("Student Manager")
root.geometry("500x500")
root.resizable(1, 1)

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
    total = [(coursework + exam) / 160 * 100 for coursework, exam in zip(total_coursework_marks, exam_marks)]
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
    name = entry2.get().strip().casefold()
    index = student_names.index(name)

    record_info =(f"Name: {student_names[index]}\n" f"Student Number: {student_nums[index]}\n" f"Total Coursework Mark: {total_coursework_marks[index]}\n" f"Exam Mark: {exam_marks[index]}\n" f"Overall Percentage: {overvall_percentage[index]:.1f}%\n" f"Grade: {student_grade[index]}")
        
    messagebox.showinfo("Record Found", record_info, parent=root)

def search_by_ID():
    id_num = int(entry2.get().strip())
    index = student_nums.index(id_num)

    record_info =(f"Name: {student_names[index]}\n" f"Student Number: {student_nums[index]}\n" f"Total Coursework Mark: {total_coursework_marks[index]}\n" f"Exam Mark: {exam_marks[index]}\n" f"Overall Percentage: {overvall_percentage[index]:.1f}%\n" f"Grade: {student_grade[index]}")
    
    messagebox.showinfo("Record Found", record_info, parent=root)

def display_average_marks():
    add_nums = lambda x, y: x + y
    sum = reduce(add_nums, overvall_percentage)
    average = sum / len(overvall_percentage)
    average_marks_label.config(text=f"Average Percentage Mark: {average:.1f}")



student_nums, student_names, mark1s, mark2s, mark3s, exam_marks = unpack_file()
sum_coursework_marks()
find_overvall_percentage()
find_student_grade()

menu_frame = Frame(root)
menu_frame.place(relwidth=1 ,relheight=1)
button1 = Button(menu_frame, text="View All Student Records", command=lambda: show_frame(student_records_frame))
button1.pack()
button2 = Button(menu_frame, text="View Individual Student Record", command= lambda: show_frame(individual_student_frame))
button2.pack()
button3 = Button(menu_frame, text="Show Student With Highest Total Score")
button3.pack()
button4 = Button(menu_frame, text="Show Student With Lowest Total Score")
button4.pack()

student_records_frame = Frame(root)
student_records_frame.place(relwidth=1 ,relheight=1)

# applies equal 15px padding to all the columns
for col in range(6):
    student_records_frame.grid_columnconfigure(col, pad=15)

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

# the enumerate function gives the column index, the heading and the values. The heading and vaules are unpacked from the tuple
for col, (heading, values) in enumerate(columns):
    # the column's heading is placed in row 0
    Label(student_records_frame, text=heading).grid(row=0, column=col, sticky=W)
    # the data is placed starting from row 1. Row 0 is left for the heading
    for row, value in enumerate(values, start=1):
        Label(student_records_frame, text=value).grid(row=row, column=col, sticky=W)

summary_row = len(student_names) + 1
num_of_students_label = Label(student_records_frame, text=f"Number of Students: {len(student_names)}")
num_of_students_label.grid(row=summary_row, column=5, sticky=E)
average_marks_label = Label(student_records_frame, text="")
average_marks_label.grid(row=summary_row + 1, column=5, sticky=E)
display_average_marks()

go_home_button = Button(student_records_frame, text="Go Home", command=lambda: show_frame(menu_frame))
go_home_button.grid(row=summary_row + 2, column=5, sticky=E)

individual_student_frame = Frame(root)
individual_student_frame.place(relwidth=1, relheight=1)

Label1 = Label(individual_student_frame, text="Search By Name")
Label1.pack()
entry1 = Entry(individual_student_frame)
entry1.pack()
search_button1 = Button(individual_student_frame, text="Search", command=search_by_name)
search_button1.pack()

Label2 = Label(individual_student_frame, text="Search By ID Number")
Label2.pack()
entry2 = Entry(individual_student_frame)
entry2.pack()
search_button2 = Button(individual_student_frame, text="Search", command=search_by_ID)
search_button2.pack()

show_frame(menu_frame)
root.mainloop()