from brain_games.cli import welcome_user, return_input_name
from random import randint
from prompt import string


GREETING_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic_of_brain_even():
    welcome_user()
    print(GREETING_GAME)
    count = 0
    while count < 3:
        magic_number = randint(1, 10)
        print(f"Question: {magic_number}")
        answer = string("Your answer: ")
        # данный код для вывода текста в случай неправильного ответа
        yes_or_no = ""
        match answer:
            case "yes":
                yes_or_no = "no"
            case "no":
                yes_or_no = "yes"
        # до сюда
        if (magic_number % 2 == 0 and answer == "yes") or \
                (magic_number % 2 != 0 and answer == "no"):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{yes_or_no}'.Let's try again, {return_input_name()}!")
            break
    if count == 3:
        print(f"Congratulations, {return_input_name()}!")
