import os
import time


SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = 2304


def clear_screen() -> None:
    """clearing screen"""
    time.sleep(0.7)
    os.system("cls" if os.name == "nt" else "clear")
