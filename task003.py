# Задание №3
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('login_form.html')


@app.post('/login/')
def login():
    login = request.form.get('username')
    password = request.form.get('password')

    users_data = {'123': ('admin', 'admin')}

    if (login, password) not in users_data.values():
        print('Invalid user data!')
        return redirect(url_for('index'))

    return redirect(url_for('login_success', name=login))


@app.route('/success/<name>')
def login_success(name: str):
    return render_template('name.html', context=name)


if __name__ == '__main__':
    app.run(debug=True)
