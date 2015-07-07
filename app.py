from bottle import (
    route, response, run, template, static_file, install, post, request
)
import json
import os

import models
import forms

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

install(models.plugin)


@route('/')
def index():
    return template('tasks')


@route('/api/tasks')
def tasks(db):
    response.content_type = 'application/json'
    tasks = [task.serialize for task in db.query(models.Task).all()]
    return json.dumps({'tasks': tasks})


@post('/api/tasks')
def create_task(db):
    form = forms.TaskForm(request.forms.decode())
    if form.validate():
        task = models.Task(
            title=form.title.data,
            memo=form.memo.data
        )
        db.add(task)
        return json.dumps(task.serialize)
    else:
        response.status_code = 400
        return json.dumps({'error': 'Validation is failed...'})


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=STATIC_DIR)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
