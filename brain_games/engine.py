import random

import prompt

from brain_games import cli


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


def ask_question_even(name):
    num1 = random_number()
    answer = even_number(num1)
    print(f'Question: {num1}')
    user_input = prompt.string('Your answer: ')
    if user_input == answer:
        print('Correct!')
        return True
    else:
        cli.answer_is_wrong(user_input, answer, name)
        return False

def ask_question_calc(name):
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
        cli.answer_is_wrong(answer, correct_answer, name)

    return was_correct

def ask_question_gcd(name):
    num1 = random_number()
    num2 = random_number()
    expected_answer = gcd(num1, num2)
    print(f'Question: {num1} {num2}')
    answer = prompt.integer('Your answer: ')
    if answer == expected_answer:   
        print('Correct!')
        return True
    else:
        cli.answer_is_wrong(answer, expected_answer, name)

        return False

def ask_question_progression(name, num_prog):
    num1 = random.randint(1, 20)
    diff = random.randint(3, 20)
    
    question = aritmetic_progression(num1, diff, num_prog)
    hide_pos = random.randint(1, num_prog - 1)
    hidden_num = question[hide_pos]
    question[hide_pos] = ".."
    print(f'Question: {" ".join(question)}')
    answer = prompt.integer('Your answer: ')
    expected_answer = int(hidden_num)
    if answer == expected_answer:
        print('Correct!')
        return True
    else:
        cli.answer_is_wrong(answer, expected_answer, name)

        return False




