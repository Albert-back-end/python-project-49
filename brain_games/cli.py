from prompt import string


def welcome_user():
    print("Welcome to the Brain Games!")
    input_name = string("May I have your name? ")
    print(f"Hello, {input_name}!")
