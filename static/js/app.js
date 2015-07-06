var angular = require('angular');

var app = angular.module('ToDo', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller('TodoController', function(){
    this.todos = [
        'タスク1',
        'タスク2',
        'タスク3',
        'タスク4'
    ]
});

