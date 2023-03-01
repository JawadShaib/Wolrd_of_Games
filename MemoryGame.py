import random
import time
import Live
import os


def generate_sequence(diff):
    arr = []
    print("generating sequence-->")
    for i in range(diff):
        arr.append(random.randint(1, 101))
    print(arr)
    time.sleep(0.7)
    os.system("cls" if os.name == "nt" else "clear")
    return arr


def get_list_from_user(diff):
    user_arr = []
    print("hey user please generate your list: ")
    for i in range(diff):
        user_arr.append(int(input(f"please enter value number {i + 1}: ")))
    return user_arr


def is_list_equal(diff):
    comp_arr = generate_sequence(diff)
    user_arr = get_list_from_user(diff)
    print(comp_arr, user_arr)
    for i in range(diff):
        if user_arr[i] not in comp_arr:
            return False
    return True


def play(difficulty):
    print("welcome to Memory Game !")
    res = is_list_equal(difficulty)
    print(f"hey user you", res * "won" + (not res) * "lost")
