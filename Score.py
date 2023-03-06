import Utills as u

import time


def add_score(dif: int) -> None:
    """adding  score to the curretnt score points points file"""
    with open(u.SCORES_FILE_NAME, "r") as f:
        current_points = f.read()
        if not (current_points):
            current_points = 0
        res = int(current_points)
        res += dif * 3 + 5
    with open(u.SCORES_FILE_NAME, "w") as f:
        f.write(str(res))
