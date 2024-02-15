from math import gcd
from brain_games.cli import welcome_user, return_input_name
from prompt import integer
from random import randint


def find_gsd():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
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
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.Let's try again, {return_input_name()}!")
            break
    if count == 3:
        print(f"Congratulations, {return_input_name()}!")