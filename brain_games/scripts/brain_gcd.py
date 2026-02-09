from brain_games import cli
import prompt  
from math import gcd
import random

def main():    
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    answer, expected_answer = ask_question(name)
    ask_question(name)
    ask_question(name)

    if answer == expected_answer:
        print(f'Congratulations, {name}!')
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {expected_answer}.")
        print (f"Let's try again, {name}!'")

    


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

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
        return answer, expected_answer
    else:        
        print(f"{answer} is wrong answer ;(. Correct answer was {expected_answer}.")
        print (f"Let's try again, {name}!")
        quit()
