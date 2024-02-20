from brain_games.cli import welcome_user, return_input_name
from prompt import integer
from random import randint
from math import gcd


GREETING_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def find_gsd():
    welcome_user()
    print(GREETING_GAME)

    count = 0
    while count < 3:
        first_number = randint(1, 10)
        second_number = randint(1, 10)
        print(f"Question: {first_number} {second_number}")
        answer = integer("Your answer: ")
        result = gcd(first_number, second_number)
        if answer == result:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{result}'.Let's try again, {return_input_name()}!")
            break
    if count == 3:
        print(f"Congratulations, {return_input_name()}!")
