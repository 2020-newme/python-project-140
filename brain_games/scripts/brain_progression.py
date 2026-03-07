import random

import prompt

from brain_games import cli, engine


def main():
    num_prog = 10
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What number is missing in the progression?')

    if (engine.ask_question_progression(name, num_prog)
            and engine.ask_question_progression(name, num_prog)
            and engine.ask_question_progression(name, num_prog)):
        print(f'Congratulations, {name}!')


