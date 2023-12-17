# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    data = {'name': 'Роман'}
    return render_template('button.html', **data)


@app.route('/greet/<name>')
def greet(name: str):
    print(url_for('greet', name='Roman'))
    return render_template('name.html', context=name)


if __name__ == '__main__':
    app.run(debug=True)
