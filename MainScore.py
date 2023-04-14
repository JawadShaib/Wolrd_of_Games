from flask import Flask
import Utills as u

app = Flask(__name__)


@app.route("/")
def show_status():
    try:
        with open(u.SCORES_FILE_NAME, "r") as f:
            SCORE = f.read()
            current_status = f"""<html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1>Score<div id="score">{SCORE}</div></h1>
            </body>
            </html>"""
            return current_status
    except FileNotFoundError:
        return f""" <html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <body>
                    <h1><div id="score" style="color:red">{u.BAD_RETURN_CODE}</div></h1>
                    </body>
                    </html>"""


if __name__ == "__main__":
    app.run(debug=True)
