var angular = require('angular');

var app = angular.module('ToDo', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller('TodoController', function($http){
    var self = this;
    self.todos = $http.get('/api/tasks')
        .success(function(data) {
            self.todos = data['tasks'];
        });

    self.create = function() {
        self.todos.push({'title': self.newTodo});
        self.newTodo = '';
    }
});
