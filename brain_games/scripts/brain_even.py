import random
from brain_games.cli import welcome_user


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user() 
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")
