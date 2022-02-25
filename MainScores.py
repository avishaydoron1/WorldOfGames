
from flask import Flask, render_template
import Utils

def score_server():
    score = 0
    Total_points = open("scores_file_name", "r")
    for i in Total_points:
        score =  int(score) + int(i)
    return score

app = Flask(__name__)


@app.route('/score')
def score():
    return render_template("score.html",SCORE=score_server())

@app.route('/error')
def error():
    return render_template("error.html",ERROR=Utils.BAD_RETURN_CODE)
app.run(debug=True)
