import MemoryGame, CurrencyRouletteGame, GuessGame
from Score import add_score


def welcome() -> None:
    name = input("Welcome, please enter your name:  ")
    print(
        f"Hello {name} and welcome to world of games (WoG) Here you can find many cool games to play\n"
    )


def get_diff():
    while True:
        game_diff = input("Please choose game difficulty from 1 to 5: ")
        if game_diff.isalpha() or not game_diff.isdigit():
            print(
                "difficulty should not include any characters (a-z) or any symbols, please try again\n"
            )
            continue
        else:
            if 1 <= int(game_diff) <= 5:
                return int(game_diff)
            else:
                print(" out of range try again\n")


def load_game():
    GAMEOPTIONS = {1: MemoryGame, 2: GuessGame, 3: CurrencyRouletteGame}
    Enter = True
    while Enter:
        print(
            """Please choose game to play:
             1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
             2. Guess Game - guess a number and see if you chose like the computer
             3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n"""
        )
        game_num = input("Please Chose a Game Number: ")
        if game_num.isalpha() or not game_num.isdigit():
            print(
                " game numer should not include any characters (a-z) or any symbols, please try again\n"
            )
            continue
        else:
            if int(game_num) < 1 or int(game_num) > 3:
                print(" game number is out of range, choose between 1-3: ")
                continue
            else:
                difficulty = get_diff()
                status = GAMEOPTIONS[int(game_num)].play(difficulty)
                if status:
                    add_score(difficulty)
                Enter = check_for_play_again()

    print("till next time !")


def check_for_play_again() -> bool:
    ans = input("would you like to play again? (y/n): ")
    while True:
        if ans == "y":
            return True
        elif ans == "n":
            return False
        else:
            ans = input(
                " must enter only y or n, would you like to play again? (y/n): "
            )
