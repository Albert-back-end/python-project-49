from brain_games.cli import welcome_user, return_input_name
from random import randint
from prompt import string
import math


text_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime():
    welcome_user()
    print(text_question)

    count = 0
    while count < 3:
        number = randint(1, 15)
        
        def isprime():
            if number < 2:
                return False
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    return False
            return True

        #вопрос-ответ
        print(f'Question: {number}')
        answer = string('Your answer: ')

        #данный код для вывода текста в случай неправильного ответа 
        yes_or_no = ""
        match answer:
            case "yes":
                yes_or_no = "no"
            case "no":
                yes_or_no = "yes"
        #проверка
        if (answer == "yes" and isprime() == True) or (answer == "no" and isprime() == False):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{yes_or_no}'.Let's try again, {return_input_name()}!")
            break
    if count == 3:
        print(f"Congratulations, {return_input_name()}!")
