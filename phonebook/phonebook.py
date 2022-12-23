from flask import Flask, render_template, request, redirect
from DBcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'rustam',
                           'password': '',
                           'database': 'phonebook', }


@app.route('/')
def phonebook():
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''SELECT id, last_name, first_name, patronymic, department, post, phone_number
                  FROM users'''
        cursor.execute(_SQL)
        content = cursor.fetchall()
        titles = ('Табельный номер', 'Фамилия', 'Имя', 'Отчество', 'Отдел', 'Должность', 'Внутренний номер')
        return render_template('phonebook.html', titles=titles, content=content)


@app.route('/edit')
def edit():
    return render_template('edit.html')



@app.route('/add_user', methods=['POST'])
def add_user():
    id = request.form['id']
    last_name = request.form['last_name']
    first_name = request.form['first_name']
    patronymic = request.form['patronymic']
    department = request.form['department']
    post = request.form['post']
    phone_number = request.form['phone_number']
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = f'''INSERT INTO users (id, last_name, first_name, patronymic, department, post, phone_number)
                  VALUES ({id}, '{last_name}', '{first_name}', '{patronymic}', '{department}', '{post}', '{phone_number}')'''
        cursor.execute(_SQL)
        
    return redirect('http://127.0.0.1:5000/')


app.run(debug=True)
