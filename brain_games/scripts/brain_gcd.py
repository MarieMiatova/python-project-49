from brain_games.engine import run_game
from brain_games.games.gcd import generate_question

def main():
    print("Find the greatest common divisor of given numbers.")
    run_game(generate_question, rounds=3)
