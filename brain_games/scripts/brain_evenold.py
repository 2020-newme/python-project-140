from brain_games import cli
import random
import prompt

question = 0
name = ''
expected_answer = ''
game_over = False
counter = 0

def main():
    global game_over, name

    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('"yes" if the number is even, otherwise answer "no"')
    while game_over == False:
        if counter == 3: # game won
            print(f'Congratulations, {name}!')
            return
        run_question()
        run_answer()

def run_question():
    global question, expected_answer
    
    question = random_number()
    print(f'Question: {question}')
    
    if question % 2 == 0:
        expected_answer = 'yes'
    else:
        expected_answer = 'no'

def run_answer():
    global name, game_over, counter
    
    your_answer = prompt.string('Your answer: ')
    if your_answer == expected_answer: # correct answer
        print('Correct!')
        counter += 1
    else: # wrong answer
        print(f'{your_answer} is wrong answer ;(. Correct answer was {expected_answer}.')
        print(f'Let´s try again, {name}!')
        game_over = True

def random_number():
    return random.randint(1, 100)
