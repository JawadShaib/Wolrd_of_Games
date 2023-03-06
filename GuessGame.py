import random
import Live


def generate_number(difficulty) -> int:
    print("number is generated")
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    user_number = int(input(f"enter a number between 1 to {difficulty}: "))
    return user_number


def compare_results(difficulty):
    secret_num = generate_number(difficulty)
    user_num = get_guess_from_user(difficulty)
    if secret_num != user_num:
        return False
    else:
        return True


def play(difficulty) -> bool:
    print("welcome to Guess Game !")
    res = compare_results(difficulty)
    print(f"hey user you", res * "won" + (not res) * "lost")
    return res
