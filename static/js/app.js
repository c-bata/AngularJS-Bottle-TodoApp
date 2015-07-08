var angular = require('angular');

var app = angular.module('ToDo', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller('TodoController', function($http){
    var self = this;
    self.todos = [];

    self.getTodo = function() {
        self.todos = $http.get('/api/tasks')
            .success(function(data) {
                self.todos = data['tasks'];
            });
    };

    self.create = function() {
        $http.post('/api/tasks', {'title': self.newTodo}).
            success(function(data, status, headers, config){
                console.log(data);
                self.getTodo();
            }).
            error(function(data, status, headers, config){
                console.log(data);
            });

        self.newTodo = '';
    };

    self.getTodo();
});
