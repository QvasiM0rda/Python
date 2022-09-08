from flask import Flask, render_template, request
from vsearch import search_for_letters

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_letters(phrase, letters))
    return render_template('results.html', the_results=results, the_phrase=phrase, the_title=title, the_letters=letters,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search_for_letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
