from flask import Flask, render_template, request, escape, session
from vsearch import search_for_letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecretKey'

app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'brickofdawn',
                           'password': '',
                           'database': 'vsearchlogDB', }

def log_request(req: 'flask_request', res: str) -> None:
    """Журналирует веб-запрос и возвращает результаты."""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        
        index_first = req.user_agent.string.rfind(' ') + 1
        index_last = req.user_agent.string.rfind('/')
        browser = req.user_agent.string[index_first:index_last]
        
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              browser,
                              res, ))


@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    """Извлекает данные из запроса; выполняет поиск; возвращает результаты."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as error:
        print('Logging failed with this error:', str(error))
    return render_template('results.html',
                           the_results=results,
                           the_phrase=phrase,
                           the_title=title,
                           the_letters=letters,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Выводит HTML-форму."""
    return render_template('entry.html',
                           the_title='Welcome to search_for_letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Выводит содержимое журнала запросов в виде HTML-таблицы."""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results
                      from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote address', 'User agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)
    except ConnectionError as error:
        print('Is your database switched on? Error:', str(error))
    except CredentialsError as error:
        print('User-id/Password issues. Error:', str(error))
    except SQLError as error:
        print('Is your query correct? Error:', str(error))
    except Exception as error:
        print('Something went wrong:', str(error))
    return 'Error'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


if __name__ == '__main__':
    app.run(debug=True)
