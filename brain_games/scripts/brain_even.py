
import prompt

from brain_games import cli, engine


def main():
    
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    if (ask_question(name)
            and ask_question(name)
            and ask_question(name)):

        print(f'Congratulations, {name}!')
        

def ask_question(name):
    num1 = engine.random_number()
    answer = engine.even_number(num1)
    print(f'Question: {num1}')
    user_input = prompt.string('Your answer: ')
    if user_input == answer:
        print('Correct!')
        return True
    else:
        cli.answer_is_wrong(user_input, answer, name)
        return False


    

    
