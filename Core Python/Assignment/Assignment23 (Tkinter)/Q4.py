#4. Quiz Game: Create an interactive quiz game with multiple-choice questions. 
#Display questions one at a time and allow the user to select an answer.
#Provide feedback on whether the selected answer is correct or incorrect.

import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    }
]

index = 0
score = 0

def show_question():
    question_label.config(text=questions[index]["question"])
    selected_option.set("")  # reset selection

    for i in range(4):
        options[i].config(
            text=questions[index]["options"][i],
            value=questions[index]["options"][i]
        )

def check_answer():
    global index, score

    if selected_option.get() == "":
        messagebox.showwarning("Warning", "Please select an option")
        return

    if selected_option.get() == questions[index]["answer"]:
        score += 1
        messagebox.showinfo("Correct", "Correct Answer!")
    else:
        messagebox.showerror(
            "Incorrect",
            f"Wrong Answer!\nCorrect Answer: {questions[index]['answer']}"
        )

    index += 1

    if index < len(questions):
        show_question()
    else:
        messagebox.showinfo(
            "Quiz Over",
            f"Your Score: {score} / {len(questions)}"
        )
        root.destroy()


# Main Window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("450x300")

question_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400)
question_label.pack(pady=20)

selected_option = tk.StringVar()

options = []
for i in range(4):
    rb = tk.Radiobutton(
        root,
        text="",
        variable=selected_option,
        value="",
        anchor="w"
    )
    rb.pack(fill="x", padx=20)
    options.append(rb)

show_question()

next_btn = tk.Button(root, text="Next", command=check_answer)
next_btn.pack(pady=20)

root.mainloop()
