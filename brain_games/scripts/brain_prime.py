import random

import prompt

from brain_games import cli


def main():
    counter = 0
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    while counter < 3:
        num1 = random_number()
        expected_answer = prime_number(num1)
        print(f'Question: {num1}')
        answer = prompt.string('Your answer: ')

        if expected_answer == answer:
            print('Correct!')
            counter += 1
            
        else:
            print(f"'{answer}' is wrong answer ;(."
                   + f" Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f'Congratulations, {name}!')  



def random_number():
    return random.randint(1, 99)


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
