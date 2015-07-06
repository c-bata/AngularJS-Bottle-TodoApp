<html ng-app="ToDo">
<head>
    <meta lang="ja" charset="UTF-8">
    <title>ToDo</title>
    <script type="text/javascript" src="/static/build/js/bundle.js"></script>
</head>
<body>
<h1>ToDoリスト</h1>
<div ng-controller="TodoController as vm">
    <ul ng-repeat="todo in vm.todos">
        <li>[[todo]]</li>
    </ul>
</div>
</body>
</html>