import tkinter as tk
from tkinter import messagebox
import random
import os

# Question bank
questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

# Global variables
question_keys = list(questions.keys())
total_questions = 5
selected_questions = random.sample(question_keys, total_questions)
score = 0
current_question = 0
highscore_file = "highscore.txt"


def check_answer():
    global score, current_question
    user_ans = answer_entry.get().lower().strip()
    correct_ans = questions[selected_questions[current_question]].lower()

    if user_ans == correct_ans:
        score += 1
        messagebox.showinfo("Correct!", "That's the right answer!")
    else:
        messagebox.showerror("Wrong!", f"Correct answer: {correct_ans}")

    current_question += 1
    answer_entry.delete(0, tk.END)

    if current_question < total_questions:
        load_question()
    else:
        finish_quiz()


def load_question():
    question_label.config(text=selected_questions[current_question])
    score_label.config(text=f"Score: {score}")


def finish_quiz():
    update_highscore(score)
    messagebox.showinfo("Quiz Completed", f"Your score: {score}/{total_questions}")
    root.destroy()


def update_highscore(new_score):
    # Read existing high score
    if os.path.exists(highscore_file):
        with open(highscore_file, "r") as f:
            try:
                high_score = int(f.read())
            except:
                high_score = 0
    else:
        high_score = 0

    if new_score > high_score:
        with open(highscore_file, "w") as f:
            f.write(str(new_score))
        messagebox.showinfo("New High Score!", f"🎉 New High Score: {new_score}")


# GUI Setup
root = tk.Tk()
root.title("Python Trivia Quiz")
root.geometry("500x250")

question_label = tk.Label(root, text="", wraplength=450, font=("Arial", 12))
question_label.pack(pady=20)

answer_entry = tk.Entry(root, width=40)
answer_entry.pack()

submit_btn = tk.Button(root, text="Submit", command=check_answer)
submit_btn.pack(pady=10)

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 10))
score_label.pack()

load_question()
root.mainloop()
