from brain_games.cli import welcome_user, return_input_name
from random import randint
from prompt import integer


text_question = "What number is missing in the progression?"

def miss_number_progression():
    #greeting
    welcome_user()
    print("What number is missing in the progression?")

    count = 0
    while count < 3:
        #параметры прогрессии
        length_progression = randint(6, 10)
        start_progression = randint(1, 6)
        distance_beetwen = randint(2, 5)
        
        #генерируем прогрессию
        progression = [start_progression + i*distance_beetwen for i in range(length_progression)]
        
        #замена числа на ..
        len_str = len(progression) - 1 
        replace_symbol = progression.index(progression[randint(0, len_str)])
        char = progression[replace_symbol]
        progression[replace_symbol] = ".."
        
        #вопрос-ответ
        print(f'Question: {progression}')
        answer = integer('Your answer: ')

        if answer == char:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{char}'.Let's try again, {return_input_name()}!")
            break
        
    if count == 3:
        print(f"Congratulations, {return_input_name()}!")


    


    





    