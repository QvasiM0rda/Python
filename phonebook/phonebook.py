from flask import Flask, render_template
from DBcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'rustam',
                           'password': '',
                           'database': 'phonebook', }


@app.route('/')
def hello_world():
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''SELECT id, last_name, first_name, patronymic, department, post, phone_number
                  FROM users'''
        cursor.execute(_SQL)
        content = cursor.fetchall()
        titles = ('Табельный номер', 'Фамилия', 'Имя', 'Отчество', 'Отдел', 'Должность', 'Внутренний номер')
        return render_template('phonebook.html', titles=titles, content=content)


app.run(debug=True)
