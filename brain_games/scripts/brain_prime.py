from brain_games.engine import run_game
from brain_games.games.prime import generate_question

def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    run_game(generate_question, rounds=3)
