from math import gcd


def main():    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    if (ask_question(name)
            and ask_question(name)
            and ask_question(name)):
        print(f'Congratulations, {name}!')


