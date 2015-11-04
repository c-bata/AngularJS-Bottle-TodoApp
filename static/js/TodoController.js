class TodoController {
    constructor($http) {
        this.$http = $http;
        this.todos = [];
        this.getTodo();
    }

    getTodo() {
        this.todos = this.$http.get('/api/tasks')
            .success((data) => {
                this.todos = data['tasks'];
            });
    }

    createTodo() {
        this.$http.post('/api/tasks', {'title': this.newTodo})
            .success((data, status, headers, config) => {
                console.log(data);
                this.todos.push(data);
            })
            .error((data, status, headers, config) => {
                console.log(data);
            });

        this.newTodo = '';
    }
}

export { TodoController }

