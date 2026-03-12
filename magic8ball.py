import random
import tkinter as tk
from tkinter import simpledialog, messagebox

ANSWERS = [
    "Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
    "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
    "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
    "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"
]

def enter_name():
    new_name = simpledialog.askstring("Ввести имя", "Как тебя зовут?", parent=root)
    if new_name is not None:
        new_name = new_name.strip()
        label_welcome.config(text=f"Привет, {new_name}!" if new_name else "Привет!")

def ask_question_dialog():
    question = simpledialog.askstring("Задать вопрос", "Какой у тебя вопрос?", parent=root)
    if question is None:
        return
    question = question.strip()
    if not question:
        messagebox.showinfo("Magic 8 Ball", "Пожалуйста, введи вопрос.")
        return
    answer = random.choice(ANSWERS)
    label_answer.config(text=answer)

root = tk.Tk()
root.title("Magic 8 Ball")
root.resizable(False, False)
root.geometry("420x220")

label_intro = tk.Label(root, text="Привет! Я магический шар и знаю ответ на любой твой вопрос.", wraplength=400)
label_intro.pack(pady=(10,6))

label_welcome = tk.Label(root, text="Привет!", font=("Arial", 10))
label_welcome.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=8)

btn_name = tk.Button(buttons_frame, text="Ввести имя", width=15, command=enter_name)
btn_name.pack(side="left", padx=6)

btn_question = tk.Button(buttons_frame, text="Задать вопрос", width=15, command=ask_question_dialog)
btn_question.pack(side="left", padx=6)

label_answer = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", wraplength=400)
label_answer.pack(pady=(12,5))

def on_close():
    if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
