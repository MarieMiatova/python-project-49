import random

def is_even(number: int) -> bool:
    return number % 2 == 0

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    rounds = 3
    correct_in_row = 0
    while True:
        number = random.randint(0, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer not in {"yes", "no"}:
            correct = is_even(number)
            expected = "yes" if correct else "no"
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{expected}'.")
            print(f"Let's try again, {name}!")
            rounds = 0
            correct_in_row = 0
            break

        answer_is_even = is_even(number)
        expected_answer = "yes" if answer_is_even else "no"

        if user_answer == expected_answer:
            print("Correct!")
            correct_in_row += 1
            rounds += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            rounds = 0
            correct_in_row = 0
            break

        if correct_in_row == 3:
            print(f"Congratulations, {name}!")
            break

if __name__ == "__main__":
    main()