from random import shuffle
import json
from pathlib import Path
from tkinter import *



questions = []

with open(Path(__file__).parent / 'questions.txt', 'r') as f:
    questions = json.load(f)

def is_valid(question):
    chs = questions.get('Choices')
    cr = questions.get('Correct')
    qt = question.get('question')
    if isinstance(qt, str) and isinstance(chs, dict) and 2 <= len(chs) <= 4 and cr in chs and question['Question'].strip():
        return True
    else:
        return False



def question_loop(qlist):
    score = 0
    max_score = len(qlist)
    for question in questions:
        if is_valid(question):
                print(question['Question'])
                answers = {}
                choices = list(question['Choices'].items())
                shuffle(choices)
                letter_indexes = ['A', 'B','C','D']
              
            
                for letter, (key, choice_text) in zip(letter_indexes, choices):
                    print(f"{letter}) {choice_text}")
                    answers[letter] = key
            
            
                answer = input("Your answer here: ").strip().upper()
            
                while answer not in ['A', 'B', 'C', 'D']:
                    print("Please enter a valid answer (A, B, C, or D).")
                    answer = input("Your answer here: ").strip().upper()
            
                if answers[answer] == question['Correct']:
                    print('Bravo!! :D')
                    score += 1
                    print(f"{score}/{max_score}")
                else:
                    print('Wrong.. D:')
                    print(f"{score}/{max_score}")
        else:
            print('Skipping..')
            
        

question_loop(questions)





    





    