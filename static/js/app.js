import angular from 'angular';
import { TodoController } from './TodoController';

let app = angular
    .module('ToDo', [])
    .controller('TodoController', TodoController);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

