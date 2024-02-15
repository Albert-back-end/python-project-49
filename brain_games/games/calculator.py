from brain_games.cli import welcome_user
from brain_games.cli import return_input_name
from random import randint
from random import choice
from prompt import integer


def logic_of_brain_calc():
    welcome_user()
    print("What is the result of the expression?")
    count = 0
    while count < 3:
        first_operand = randint(1, 15)
        second_operand = randint(1, first_operand)
        sign = choice(['+', '-', '*'])
        print(f"Question: {first_operand} {sign} {second_operand}")
        answer = integer("Your answer: ")
        result = None
        match sign:
            case "+":
                result = first_operand + second_operand
            case "-":
                result = first_operand - second_operand
            case "*":
                result = first_operand * second_operand
        if result == answer:        
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.Let's try again, {return_input_name()}!")
            break
    if count == 3:
        print(f"Congratulations, {return_input_name()}!")
