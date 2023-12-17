# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    make_response,
    url_for,
)

app = Flask(__name__)


def get_users_data() -> dict:
    return {
        'admin@mail.com': ['admin', 'admin'],
        'user@mail.com': ['12345', 'user'],
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form_task009_HW.html')

    mail = request.form.get('email')
    password = request.form.get('password')

    users_data = get_users_data()

    db_password, username = users_data.get(mail, [None, None])

    if db_password is not None:
        if password == db_password:
            response = make_response(redirect(url_for('greet')))
            response.set_cookie('username', username)

            return response

    return redirect(url_for('index'))


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('username')

    return response


@app.route('/greet/')
def greet():
    username = request.cookies.get('username')

    return render_template('greet.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
