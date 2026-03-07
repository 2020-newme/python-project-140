import random

import prompt

from brain_games import cli, engine


def main():
    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    if (ask_question(name)
            and ask_question(name)
            and ask_question(name)):

        print(f'Congratulations, {name}!') 


def ask_question(name):
    num1 = engine.random_number()
    answer = engine.even_number(num1)
    print(f'Question: {num1}')
    user_input = prompt.string('Your answer: ')
    if user_input == answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_input}' is wrong answer ;(."
              + f" Correct answer was '{answer}'.")
        print(f"Let's try again, {name}!")    
        return False


    

    
