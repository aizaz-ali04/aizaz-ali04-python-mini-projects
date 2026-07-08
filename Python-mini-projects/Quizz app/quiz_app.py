import tkinter as tk

questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "5 * 3 = ?",
        "options": ["15", "10", "20", "25"],
        "answer": "15"
    },
    {  
        "question": "5 - 3 = ?",
        "options": ["15", "10", "2", "25"],
       "answer": "2"
    }
]

q_index = 0
score = 0


def check_answer(selected):
    global q_index, score

    correct = questions[q_index]["answer"]

    if selected == correct:
        score += 1

    q_index += 1

    if q_index < len(questions):
        show_question()
    else:
        question_label.config(text=f"Quiz Finished!\nYour Score: {score}/{len(questions)}")
        for btn in buttons:
            btn.config(state="disabled")


def show_question():
    q = questions[q_index]
    question_label.config(text=q["question"])

    for i in range(4):
        buttons[i].config(text=q["options"][i])


window = tk.Tk()
window.title("Quiz App")
window.geometry("400x300")

question_label = tk.Label(window, text="", font=("Arial", 14))
question_label.pack(pady=20)

buttons = []
for i in range(4):
    btn = tk.Button(window, text="", width=20,
    command=lambda i=i: check_answer(buttons[i].cget("text")))
    btn.pack(pady=5)
    buttons.append(btn)

show_question()

window.mainloop()