from brain_games.engine import run_game
from brain_games.games.calc import generate_question

def main():
    print("What is the result of the expression?")
    run_game(generate_question, rounds=3)
