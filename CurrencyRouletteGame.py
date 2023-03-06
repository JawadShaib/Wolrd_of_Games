import random
import Live
from currency_converter import CurrencyConverter


TOTAL = 100
c = CurrencyConverter()


def get_money_interval(difficulty):
    current_rate = c.convert(1, "USD", "ILS")
    return TOTAL - (5 - difficulty), TOTAL + (5 - difficulty)


def get_guess_from_user():
    t = int(input("please enter your total value: "))
    return t


def check_amount(amount, difficulty):
    low, high = get_money_interval(difficulty)
    print(low, high)
    return low <= amount <= high


def play(difficulty) -> bool:
    print("welcome to Currency game !")
    amount = get_guess_from_user()
    res = check_amount(amount, difficulty)
    print(f"hey user you", res * "won" + (not res) * "lost")
    return res
