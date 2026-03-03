import random
from math import gcd

import prompt

from brain_games import cli


def main():    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    if (ask_question(name)
            and ask_question(name)
            and ask_question(name)):
        print(f'Congratulations, {name}!')


def random_number():
    return random.randint(1, 100)


def ask_question(name):
    num1 = random_number()
    num2 = random_number()
    expected_answer = gcd(num1, num2)
    print(f'Question: {num1} {num2}')
    answer = prompt.integer('Your answer: ')
    if answer == expected_answer:   
        print('Correct!')
        return True
    else:        
        print(f"'{answer}' is wrong answer ;(."
              + f" Correct answer was '{expected_answer}'.")
        print(f"Let's try again, {name}!")
        return False
