

from brain_games import cli, engine


def main():    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What is the result of the expression?')

    if (engine.ask_question_calc(name)
            and engine.ask_question_calc(name)
            and engine.ask_question_calc(name)):
        print(f'Congratulations, {name}!')





