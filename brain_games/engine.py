from brain_games.cli import welcome_user


def run_game(game_logic, rounds=3):
    print()
    name = welcome_user() 

    for _ in range(rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer != str(correct_answer):
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")
