from bottle import (
    route, response, run, template, static_file, install, post, request
)
import json
import os
import jsonschema

import models
import schemas

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
    response.content_type = 'application/json'
    try:
        jsonschema.validate(request.json, schemas.task_schema)
        task = models.Task(title=request.json['title'])
        db.add(task)
        db.commit()  # ここでコミットしないとidとかdefault値を返せない
        return json.dumps(task.serialize)
    except jsonschema.ValidationError:
        response.status_code = 400
        return json.dumps({
            'error': {'message': 'Validation is failed...'}
        })


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=STATIC_DIR)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
