from brain_games import cli
import prompt  
import random

def main():
    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print ('Answer "yes" if the number is even, otherwise answer "no".')

    ask_question(name)
    ask_question(name)
    ask_question(name)

    print (f'Congratulations, {name}!') 

def ask_question(name):
    num1 = random_number()
    answer = even_number(num1)
    print (f'Question: {num1}')
    user_input = prompt.string('Your answer: ')
    if user_input == answer:
        print ('Correct!')
    else:
        print (f"'{user_input}' is wrong answer ;(. Correct answer was '{answer}'.")
        print (f"Let's try again, {name}!")    
        quit()



def random_number():
    return random.randint(1, 100)
    
def even_number(num1):
    if num1%2 == 0:
        return 'yes'
    else:
        return 'no'
    
