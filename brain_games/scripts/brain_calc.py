#from brain_games import cli
import prompt
import random

def main():    
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    if not ask_question(name):
        return
    if not ask_question(name):
        return
    if not ask_question(name):
        return
    print(f'Congratulations, {name}!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(name):
    num1 = random_number()
    op = random_oper()
    num2 = random_number()
    print(f'Question: {num1} {op} {num2}')
    answer = prompt.integer('Your answer: ')
    correct_answer = get_correct_answer(num1, op, num2)
    was_correct = answer == correct_answer
    if was_correct:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
    return was_correct


def random_number():
    return random.randint(1, 100)

def random_oper():
    op = ['+','-','*']
    return random.choice(op)

def get_correct_answer(num1, op, num2):
    if op == '-':
        return num1 - num2
    if op == '+':
        return num1 + num2
    if op == '*':
        return num1 * num2
