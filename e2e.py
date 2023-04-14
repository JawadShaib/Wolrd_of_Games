from selenium import webdriver
from selenium.webdriver.common.by import By
from Utills import URL
import MainScore


def test_score_service() -> bool:
    try:
        my_driver = webdriver.Chrome()
        my_driver.get(URL)
        actual_score = int(my_driver.find_element(By.ID, "score").text)
        if 1 < actual_score < 1000:
            return True
        else:
            return False
    except:
        return False


def main_function() -> int:
    score = test_score_service()
    return (-1) * (not score)


if __name__ == "__main__":
    print(main_function())
