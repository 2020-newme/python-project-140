from math import gcd

import prompt

from brain_games import cli, engine


def main():    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    if (ask_question(name)
            and ask_question(name)
            and ask_question(name)):
        print(f'Congratulations, {name}!')


def ask_question(name):
    num1 = engine.random_number()
    num2 = engine.random_number()
    expected_answer = gcd(num1, num2)
    print(f'Question: {num1} {num2}')
    answer = prompt.integer('Your answer: ')
    if answer == expected_answer:   
        print('Correct!')
        return True
    else:
        cli.answer_is_wrong(answer, expected_answer, name)

        return False
