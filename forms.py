from wtforms.form import Form
from wtforms import validators, StringField


class TaskForm(Form):
    title = StringField('タイトル', [
        validators.required(message='入力して下さい'),
        validators.length(min=1, max=100, message='100文字以内で入力して下さい')
    ])
