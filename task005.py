# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form_task005.html')


@app.post('/')
def index_post():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    symbol = request.form.get('symbol')

    if symbol in '+-*/':
        result = eval(f'{num1}{symbol}{num2}')
    else:
        result = 'Ошибка!'

    text = f'{num1} {symbol} {num2}'

    return render_template('form_task005.html', text=text, result=result)


if __name__ == '__main__':
    app.run(debug=True)
