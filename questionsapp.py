from random import shuffle
from pathlib import Path
from tkinter import *
import json

questions = []

with open(Path(__file__).parent / 'questions.txt', 'r') as f:
    questions = json.load(f)

def is_valid(question):
    chs = question.get('Choices')   
    cr = question.get('Correct')    
    qt = question.get('Question')
    if isinstance(qt, str) and isinstance(chs, dict) and 2 <= len(chs) <= 4 and cr in chs and question['Question'].strip():
        return True
    else:
        return False

def question_loop(qlist):
    app = Tk()
    app.title("Quiz App")
    score = 0
    max_score = len(qlist)
    clicked = StringVar()
    for question in questions:
        if is_valid(question):
                for widget in app.winfo_children():
                    widget.destroy()
                # print(question['Question'])
                Label(app, text=f"{question['Question']}").grid(row=0, column=0)
                answers = {}
                choices = list(question['Choices'].items())
                shuffle(choices)
                letter_indexes = ['A', 'B','C','D']

                br = 1
                bc = 1
                answer = 0
                def myClick(answers, letter, key):
                    nonlocal score
                    if answers[letter] == question['Correct']:
                        score += 1
                        Label(app, text=f"Score: {score}/{max_score}").grid(row=3, column=0)
                        Label(app, text=f"Bravo !! :D").grid(row=3, column=3)
                    else:
                        Label(app, text=f"Wrong.. D:").grid(row=3, column=3)
                    clicked.set(letter)
                for letter, (key, choice_text) in zip(letter_indexes, choices):
                    # print(f"{letter}) {choice_text}"
                    answers[letter] = key
                    Button(app, text=f"{letter}) {choice_text}", command=lambda l=letter, k=key: myClick(answers, l, k)).grid(row=br, column=bc)
                    bc += 1
                Label(app, text=f"Score: {score}/{max_score}").grid(row=3, column=0)
                app.wait_variable(clicked)


        else:
            print('Skipping..')
    for widget in app.winfo_children():
        widget.destroy()
    Label(app, text=f"Quiz complete !").grid(row=0, column=0)
    Label(app, text=f"Score: {score}/{max_score}").grid(row=1, column=0)
    app.mainloop()
        

question_loop(questions)
