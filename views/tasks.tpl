<html ng-app="ToDo">
<head>
    <meta lang="ja" charset="UTF-8">
    <title>ToDo</title>
    <script type="text/javascript" src="/static/build/js/bundle.js"></script>
</head>
<body>
<h1>ToDoリスト</h1>
<div ng-controller="TodoController as vm">
    <form ng-submit="vm.createTodo()">
        <input type="text" ng-model="vm.newTodo" placeholder="ToDo名を入力">
        <input type="button" value="新規作成">
    </form>

    <ul ng-repeat="todo in vm.todos">
        <li>[[todo.title]]</li>
    </ul>
</div>
</body>
</html>