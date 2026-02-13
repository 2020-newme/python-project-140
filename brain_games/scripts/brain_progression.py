from brain_games import cli
import prompt  
import random

def main():
    num_prog = 10
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')

    ask_question(name, num_prog)
    ask_question(name, num_prog)
    ask_question(name, num_prog)
    print(f'Congratulations, {name}!')

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def aritmetic_progression(num1,diff,num_prog):
    return [str(num1 + i * diff) for i in range(num_prog)]

def ask_question(name, num_prog):
    num1 = random.randint(1, 20)
    diff = random.randint(3, 20)
    
    question = aritmetic_progression(num1,diff,num_prog)
    hide_pos = random.randint(1,num_prog - 1)
    elem = question[hide_pos]
    hidden_num = question[hide_pos]
    question[hide_pos] = ".."
    print(f'Question: {" ".join(question)}')
    answer = prompt.integer('Your answer: ')
    expected_answer = int(hidden_num)
    if answer == expected_answer:
        print(f'Correct!')
    else:
        print(f"{'answer'} is wrong answer ;(. Correct answer was {'expected_answer'}.")
        print (f"Let's try again, {name}!'")
        quit()
