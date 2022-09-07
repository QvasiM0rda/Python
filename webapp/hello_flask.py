from flask import Flask, render_template
from vsearch import search_for_letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'


@app.route('/search')
def do_search():
    return str(search_for_letters('life, the universe and everyting!', 'eiru, !'))


app.run()
