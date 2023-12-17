# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

from flask import Flask, redirect, render_template, url_for, request
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form/', methods=['GET'])
def form_get():
    return render_template('form.html')


@app.route('/form/', methods=['POST'])
def form_post():
    image = request.files.get('file')
    # file_name = secure_filename(image.filename)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)