from brain_games import cli, engine


def main():    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    if (engine.ask_question_gcd(name)
            and engine.ask_question_gcd(name)
            and engine.ask_question_gcd(name)):
        print(f'Congratulations, {name}!')


