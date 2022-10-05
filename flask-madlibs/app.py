from flask import Flask, request, render_template
from stories import story

app  = Flask(__name__)



@app.route('/homepage')
def homepage():
    words = story.prompts
    return render_template("index.html",words = words)

@app.route('/madlib')
def madlib():
    chosen_words = request.args
    new_story = story.generate(chosen_words)
    return render_template('madlib.html',new_story = new_story)
