# AngularJS Bottle ToDo Application

## About

BottleとAngularJSの勉強用に作ったシンプルなToDoアプリ。
使い方がわかったもの。

* AngularJS
* Bottle
* SQLAlchemy
* Bottle-SQLAlchemy
* jsonschema

## 所感

- AngularJSはこれぐらいの規模なら簡単に使えた。
  - API覚えてしまえば実装できることが多いので楽ではある。資料にも困らなかった。
  - 今回は `$http` 使ったけど、調べた感じ `$resource` っていうのがあった。
    - こっちのほうがなんか良さそう。ちょっとAPI覚えるのが面倒に感じてしまった。
    - 今頑張って覚えてもAngular2で大きく変わるらしいのでちょっとモチベーションが保てないかも
    - React.jsかmithril.jsやるのが良さそう
- Bottleはシンプルなものなら全然簡単に使えていい。
- SQLAlchemyちょっと慣れない.
- jsonschemaも初めて書いてみたけど特に使いづらいとは感じなかった。

## メモ

#### AngularJSの変数のタグ

Bottleのテンプレートとかぶるから変える。

```
app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});
```

#### ToDoの追加処理

最初はToDo追加してSuccessとなったら、毎回 `getTodo()` でAPI叩いて全部描画してしまってた。
当たり前だったんだけど、postが成功したら成功したToDoをidとかも含めてレスポンスとして返して、Angular側のリストに追加してあげる。


## 参考資料

- Pythonエンジニア養成読本 BottleとSQLAlchemy
- jsonschemaは適当にググった
- AngularJSは
