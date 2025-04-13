import tkinter as tk
from tkinter import messagebox
import random
from quiz_questions import quiz_qs

options_list = []

def add_question():
    if not quiz_qs:
        messagebox.showerror("Error", "No questions available.")
        return
    
    start_button.pack_forget()
    
    global question_no,options_list
    options_list.clear()
    skip_button.config(state="normal")


    if question_no >= len(quiz_qs):
        messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(quiz_qs)}")
        root.destroy()
        return

    for widget in main_frame.winfo_children():
        if isinstance(widget, tk.Button) and widget != start_button:
            widget.destroy()

    question = quiz_qs[question_no]["question"]
    ques_label.config(text=f"{question_no + 1}. {question}")
    options = quiz_qs[question_no]["options"]
    random.shuffle(options)

    for option in options:
        # Create a button for each option  
        option_buttons = tk.Button(master=main_frame,text=option,font=("Helvetica", 15,"bold"), width=30,cursor = "hand2", fg="White", bg="Black",command=lambda opt=option: check_ans(opt))
        option_buttons.pack(pady=5)
        options_list.append(option_buttons)
    
    skip_button.pack(pady=25)
    score_label.config(text=f"Your Score: {score}/{len(quiz_qs)}")

    
def check_ans(selected_option):
    global question_no,score
    
    for buttons in options_list:
        buttons.config(state="disabled")
    
    skip_button.config(state="disabled")
    
    
    correct_answer = quiz_qs[question_no]["answer"]

    if selected_option == correct_answer:
        feedback_label.config(text="Correct Answer!", fg="Green")
        feedback_label.pack(pady=1)
        score += 1
        score_label.config(text=f"Your Score: {score}/{len(quiz_qs)}")
        root.after(1000,next_question)
    
    else:
        feedback_label.config(text=f"Wrong Answer!\nCorrect Answer: {correct_answer}", fg="Red")
        feedback_label.pack(pady=1)

        root.after(1000,next_question)
    
def next_question():
    global question_no
    feedback_label.pack_forget()
    question_no += 1
 
    add_question()


root = tk.Tk()
root.title("Quiz App")
root.geometry("600x600")

header_frame = tk.Frame(root, bg="Yellow")
header_frame.pack(fill=tk.X)

header = tk.Label(master=header_frame, text="Quiz App", font=("Eras Bold ITC", 60, "bold"), fg="Black",bg="Yellow")
header.pack(pady=20)

question_no = 0
score = 0

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both")

start_button = tk.Button(master=main_frame, text="Start Quiz", font=("Bahnschrift SemiBold", 20), fg="Yellow", bg="Black",relief=tk.RAISED, cursor = "hand2",command=add_question)
start_button.pack(pady=50)

ques_label = tk.Label(master=main_frame, text="", font=("Bahnschrift SemiBold", 17), fg="Black")
ques_label.pack(pady=20)

feedback_label = tk.Label(master=main_frame, text="", font=("Impact", 17), fg="Black")
feedback_label.pack_forget()


skip_button = tk.Button(root, text="Skip", font=("Arial", 10,"bold"), fg="White", bg="Black",width=10, cursor = "hand2",command=next_question)
skip_button.pack_forget()

score_label = tk.Label(root, text="", font=("Bahnschrift SemiBold", 17), fg="Black")
score_label.pack(pady=5)

root.mainloop()