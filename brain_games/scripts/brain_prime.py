from brain_games import cli
import prompt  
import random

def main():
    counter = 0
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    while counter < 3:
        num1 = random_number()
        expected_answer = prime_number(num1)
        print (f'Question: {num1}')
        answer = prompt.string('Your answer: ')

        if expected_answer == answer:
            print (f'Correct!')
            counter +=1
            
        else:
            print (f"{answer} is wrong answer ;(. Correct answer was {expected_answer}.")
            quit()
            
    print (f'Congratulations, {name}!')  

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def random_number():
    return random.randint(1, 99)


def prime_number(num1):
    
    if num1%2 == 0:
        return 'no'
    if num1%3 == 0:
        return 'no'
    if num1%5 == 0:
        return 'no'
    if num1%7 == 0:
        return 'no'
    if num1%11 == 0:
        return 'no'
    else:
        return 'yes'
