import prompt

from brain_games import cli, engine


def main():
    counter = 0
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    while counter < 3:
        num1 = engine.random_number()
        expected_answer = engine.prime_number(num1)
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

