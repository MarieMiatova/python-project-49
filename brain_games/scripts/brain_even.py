from brain_games.engine import run_game
from brain_games.games.even import generate_question


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    run_game(generate_question, rounds=3)
