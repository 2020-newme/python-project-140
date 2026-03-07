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


def aritmetic_progression(num1, diff, num_prog):
    return [str(num1 + i * diff) for i in range(num_prog)]


def random_oper():
    op = ['+', '-', '*']
    return random.choice(op)


def prime_number(num1):
    
    if num1 <= 1:
        return 'no'
    if num1 % 2 == 0 and num1 != 2:
        return 'no'
    if num1 % 3 == 0 and num1 != 3:
        return 'no'
    if num1 % 5 == 0 and num1 != 5:
        return 'no'
    if num1 % 7 == 0 and num1 != 7:
        return 'no'
    if num1 % 11 == 0 and num1 != 11:
        return 'no'
    else:
        return 'yes'
