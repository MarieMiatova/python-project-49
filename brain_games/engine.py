from brain_games.cli import welcome_user

def run_game(game_logic, rounds=3):
    """
    Универсальный движок для игр.
    game_logic — функция, возвращающая (question, correct_answer)
    rounds — количество правильных ответов для победы
    """
    print("Welcome to the Brain Games!")
    name = welcome_user()
    correct_count = 0

    while correct_count < rounds:
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()

        if answer != str(correct_answer):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return 
        print("Correct!")
        correct_count += 1 

    print(f"Congratulations, {name}!")  