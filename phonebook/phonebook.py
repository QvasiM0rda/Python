from flask import Flask, render_template, request, redirect
from DBcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'rustam',
                          'password': '',
                          'database': 'phonebook', }
app.config['titles'] = ('Таб. номер', 'Фамилия', 'Имя', 'Отчество', 'Отдел', 'Должность', 'Вн. номер')
app.config['names'] = ('id', 'last_name', 'first_name', 'patronymic', 'department', 'post', 'phone_number')


@app.route('/')
def phonebook():
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''SELECT id, last_name, first_name, patronymic, department, post, phone_number
                  FROM users'''
        cursor.execute(_SQL)
        content = cursor.fetchall()
        return render_template('phonebook.html', titles=app.config['titles'], content=content)


@app.route('/edit')
def edit():
    return render_template('edit.html', titles=app.config['titles'], names=app.config['names'])


@app.route('/add_user', methods=['POST'])
def add_user():
    user_id = request.form['id']
    last_name = request.form['last_name']
    first_name = request.form['first_name']
    patronymic = request.form['patronymic']
    department = request.form['department']
    post = request.form['post']
    phone_number = request.form['phone_number']
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = f'''INSERT INTO users (id, last_name, first_name, patronymic, department, post, phone_number)
                  VALUES ({user_id}, '{last_name}', '{first_name}', '{patronymic}',
                          '{department}', '{post}', '{phone_number}')'''
        cursor.execute(_SQL)
        
    return redirect('http://localhost:5000/')


app.run(debug=True)
