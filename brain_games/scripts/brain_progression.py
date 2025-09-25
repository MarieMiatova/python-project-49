from brain_games.engine import run_game
from brain_games.games.progression import generate_question


def main():
    print("What number is missing in the progression?")
    run_game(generate_question, rounds=3)
