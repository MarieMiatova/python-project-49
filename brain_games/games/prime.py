import random
import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_question():
    number = random.randint(2, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer
