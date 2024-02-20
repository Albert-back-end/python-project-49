from prompt import string

input_name = None


def welcome_user():
    global input_name
    print("Welcome to the Brain Games!")
    input_name = string("May I have your name? ")
    print(f"Hello, {input_name}!")


def return_input_name():
    return input_name
