from brain_games.cli import welcome_user, return_input_name
from random import randint
from prompt import string

TEXT_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer(number):
    if is_prime_number(number) is True:
        return 'yes'
    else:
        return 'no'


def is_prime():
    welcome_user()
    print(TEXT_QUESTION)

    count = 0
    while count < 3:
        number = randint(1, 15)

        is_prime_number(number)

        print(f'Question: {number}')
        answer = string('Your answer: ')

        if (answer == "yes" and is_prime_number(number)) or \
                (answer == "no" and not is_prime_number(number)):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{get_correct_answer(number)}'. Let's try again, {return_input_name()}!")
            break
    if count == 3:
        print(f"Congratulations, {return_input_name()}!")
