from brain_games import cli
import prompt  
import random

def main():
    num1 = random_number()
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    print (f'Question: {num1}')
    answer = prompt.string('Your answer: ')
    expected_answer = prime_number(num1)
    
    if expected_answer == answer:
        print (f'Correct!')
    else:
        print (f"{answer} is wrong answer ;(. Correct answer was {expected_answer}.")

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def random_number():
    return random.randint(1, 100)


def prime_number(num1):
    
    if num1%2 == 0:
        return 'no'
    if num1%3 == 0:
        return 'no'
    if num1%4 == 0:
        return 'no'
    if num1%5 == 0:
        return 'no'
    if num1%7 == 0:
        return 'no'
    if num1%9 == 0:
        return 'no'
    if num1%11 == 0:
        return 'no'
    else:
        return 'yes'
