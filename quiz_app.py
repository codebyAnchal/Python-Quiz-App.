import tkinter as tk
from tkinter import messagebox

# Questions, options and answers
questions = [
    "What is the full form of CPU?",
    "Which data type is used to store text in Python?",
    "Which symbol is used for comments in Python?",
    "What does BCA stand for?",
    "Which company developed Python?"
]

options = [
    ["Central Processing Unit", "Computer Personal Unit", "Central Performance Utility", "Control Processing Unit"],
    ["int", "str", "float", "char"],
    ["//", "#", "/* */", "<!-- -->"],
    ["Bachelor of Computer Applications", "Business Computer Analysis", "Basic Coding Applications", "Binary Coded Arithmetic"],
    ["Microsoft", "Google", "Guido van Rossum", "Apple"]
]

answers = [0, 1, 1, 0, 2]  # correct option index for each question

# Quiz App class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.q_no = 0
        self.score = 0

        self.question_label = tk.Label(root, text=questions[self.q_no], font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()
        self.opts = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value=i, font=("Arial", 12))
            btn.pack(anchor="w")
            self.opts.append(btn)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        self.question_label.config(text=questions[self.q_no])
        self.var.set(-1)
        for i, opt in enumerate(options[self.q_no]):
            self.opts[i].config(text=opt)

    def next_question(self):
        if self.var.get() == answers[self.q_no]:
            self.score += 1

        self.q_no += 1
        if self.q_no == len(questions):
            messagebox.showinfo("Result", f"Your Score: {self.score}/{len(questions)}")
            self.root.destroy()
        else:
            self.display_question()

# Run the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()