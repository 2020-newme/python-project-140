import random


def random_number():
    return random.randint(1, 99)

def even_number(num1):
    if num1 % 2 == 0:
        return 'yes'
    else:
        return 'no'

def get_correct_answer(num1, op, num2):
    if op == '-':
        return num1 - num2
    if op == '+':
        return num1 + num2
    if op == '*':
        return num1 * num2

