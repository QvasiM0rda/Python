from flask import Flask, render_template, request, redirect
from markupsafe import escape
from DBcm import UseDatabase

app = Flask(__name__)

# Настройки подключения к БД
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'rustam',
                          'password': '',
                          'database': 'phonebook', }

# titles - Названия столбцов, names - значение для тега input
app.config['titles'] = ('Таб. номер', 'Фамилия', 'Имя', 'Отчество', 'Отдел', 'Должность', 'Вн. номер')
app.config['names'] = ('id', 'last_name', 'first_name', 'patronymic', 'department', 'post', 'phone_number')


def execute_script(script: str) -> list:
    # подключается к БД использую класс UseDatabase, возвращает результат выполнения
    with UseDatabase(app.config['dbconfig']) as cursor:
        cursor.execute(script)
        return cursor.fetchall()


@app.route('/', methods=['GET', 'POST'])
def phonebook():
    # Начальная страница. Выводит информацию из БД
    script = '''SELECT id, last_name, first_name, patronymic, department, post, phone_number
              FROM users'''
    content = execute_script(script)
    return render_template('phonebook.html', titles=app.config['titles'], content=content)


@app.route('/edit')
def edit():
    # Страница редактирования. Пока из редактирования только добавление новой записи.
    return render_template('edit.html', titles=app.config['titles'], names=app.config['names'])


@app.route('/add_user', methods=['POST'])
def add_user():
    # Добавление новой записи.
    user_id = escape(request.form['id'])
    last_name = escape(request.form['last_name'])
    first_name = escape(request.form['first_name'])
    patronymic = escape(request.form['patronymic'])
    department = escape(request.form['department'])
    post = escape(request.form['post'])
    phone_number = escape(request.form['phone_number'])
    script = f'''INSERT INTO users (id, last_name, first_name, patronymic, department, post, phone_number)
                      VALUES ({user_id}, '{last_name}', '{first_name}', '{patronymic}',
                              '{department}', '{post}', '{phone_number}')'''
    execute_script(script)
    return redirect('http://localhost:5000/')


@app.route('/delete', methods=['POST'])
def delete():
    # Удаление записи.
    script = f'''DELETE FROM users WHERE id = {request.form.to_dict()['id']}'''
    execute_script(script)
    return redirect('http://localhost:5000/')


app.run(debug=True)
