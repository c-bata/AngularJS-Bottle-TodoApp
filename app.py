from bottle import (
    route, response, run, template, static_file, install, post, request
)
import json
import os

import models

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
    task = models.Task(title=request.json['title'])
    db.add(task)
    db.commit()  # viewが終わるまでcommitされないからidとかを返せない
    return json.dumps(task.serialize)


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=STATIC_DIR)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
