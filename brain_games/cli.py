import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def answer_is_wrong(user_input, answer, name):
    print(f"'{user_input}' is wrong answer ;(."
              + f" Correct answer was '{answer}'.")
    print(f"Let's try again, {name}!")    
