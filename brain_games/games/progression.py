import random


def generate_progression(length=10, min_length=5):
    length = max(length, min_length)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    hidden_index = random.randint(0, length - 1)
    progression = [start + i * step for i in range(length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


def generate_question():
    return generate_progression()

