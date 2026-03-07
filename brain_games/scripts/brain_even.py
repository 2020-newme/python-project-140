

from brain_games import cli, engine


def main():
    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    if (engine.ask_question_even(name)
            and engine.ask_question_even(name)
            and engine.ask_question_even(name)):

        print(f'Congratulations, {name}!')
        


    

    
