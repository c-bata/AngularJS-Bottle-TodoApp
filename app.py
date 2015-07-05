from bottle import route, response, run, template
import json

@route('/')
def index():
    return template('tasks')


@route('/api/tasks')
def tasks():
    response.content_type = 'application/json'
    tasks = [
        {'id': '1', 'title': 'タスク表題1', 'memo': 'タスクのメモ1'},
        {'id': '2', 'title': 'タスク表題2', 'memo': 'タスクのメモ2'},
        {'id': '3', 'title': 'タスク表題3', 'memo': 'タスクのメモ3'},
    ]
    return json.dumps({'tasks': tasks})

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
