# TODOリスト作成を通して学んだこと

## JSの基礎文法

- **`const` / `let`**: `const`は再代入不可。`counter++`のように後から書き換える変数は`let`で宣言する。
- **`=` と `===` の違い**: `if (counter = 0)`のように`=`（代入）を`===`（比較）と間違えると、常にfalse扱いになるなどのバグを生む。
- **配列の破壊的/非破壊的メソッド**
  - 破壊的: `push`, `pop`, `splice`, `sort`, `reverse`, `fill`
  - 非破壊的: `map`, `filter`, `slice`, `concat`, `find`
  - `sort()`はデフォルトで文字列比較になる（`[10, 1, 2].sort()`が`[1, 10, 2]`になる）ので、数値ソートには比較関数`(a, b) => a - b`が必須。
  - JSの配列には負のインデックス（Pythonの`arr[-1]`）が無い。`arr.at(-1)`を使う。
- **`forEach` と `for...of`**
  - `forEach`は「配列を舐めて副作用を起こす」だけの単純な用途向き。`break`/`continue`ができない。
  - `for...of`は`break`/`continue`が使え、`await`も直接書ける、配列以外のiterable（Map, Setなど）も回せる。
  - 今回のように単純な繰り返しなら`forEach`で十分、複雑な制御が必要になったら`for...of`に切り替える。
- **`.then()` チェーン と `async/await`**
  - `await`は`async`関数の中でしか使えない（トップレベルscriptタグでは不可）。
  - `async/await`は「完全上位互換」ではなく、単純な処理は`.then()`の方がシンプルなこともある。複雑な条件分岐・ループ・try/catchを伴う非同期処理では`async/await`が読みやすい。

## DOM操作

- `document.getElementById(...)` / `document.querySelector(...)` は必ず`document.`が必要（`querySelector`単体では呼べない）。
- `document.createElement(tag)` で要素を作成 → `.textContent = "..."` で中身を設定 → `親.appendChild(子)` で実際に画面へ挿入、という3ステップが基本の流れ。
- HTMLの`id`属性は一意でなければならないが、`name`属性は重複可（ラジオボタンのグループ化などにわざと使う）。

## `<form>` と `fetch` の使い分け

- `<form>`はページ遷移を伴うブラウザ標準の送信機能。フロントJSなしでも動く「壊れにくさ」がメリット。
- `fetch`はページ遷移せず、JSがレスポンス（JSON）を受け取って自分でDOMを更新する必要がある。その分、読み込み中表示やエラー処理などをすべて自前で書く必要がある。
- 「ページ遷移なしの方が上位互換」ではなく、シンプルさ・堅牢さ vs インタラクティブ性のトレードオフ。
- `<button>`の`type`属性は`submit`(デフォルト) / `reset` / `button`の3種類。`<form>`内でページ遷移させたくないボタンは`type="button"`にする。

## Flask（サーバー側）

- `request.form['key']` はフォーム形式（`application/x-www-form-urlencoded`）のデータを受け取る。
- `request.json` は**プロパティ**（呼び出し不要、`()`を付けるとエラー）。JSON形式で送られたボディ全体（辞書）が入るので、値を取り出すには`request.json['key']`とキー指定が必要。
- サーバーからJSONを返す（`jsonify(...)`）場合は、`redirect`は不要になる。ページ遷移しないので「次にどこへ飛ばすか」を指示する必要がなくなるため。
- Jinja2のテンプレート内で、HTMLコメント`<!-- -->`は**Jinjaの構文を無効化しない**。`{{ }}`や`{% %}`はコメントの中でも評価されてしまう（`{% for %}`を消したのに`{{ loop.index0 }}`だけ残してエラーになった実例あり）。

## アーキテクチャ／設計の考え方

- JSがデータベースに直接触ることはない。「ブラウザ(JS) → API(Flaskのルート) → データベース」という順で、APIが橋渡し役になる。
- 単一ブラウザでの利用なら、Pythonにデータを送る必然性は薄い。送る意味が出るのは「リロードに耐えたい」「複数端末/タブで共有したい」場合。
- ネイティブスマホアプリ（Swift/Kotlin/React Native/Flutterなど）はHTMLを使わずAPI(JSON)でサーバーと通信する。WebViewアプリやブラウザはHTMLを使う。
- DjangoとFlaskの違いは「JSの必要量」ではなく、フォーム/認証/管理画面などが標準搭載か否か（Djangoはフルスタック、Flaskは最小構成）。

## VSCodeの設定

- `editor.tabSize`は言語ごとに`settings.json`の`"[html]"`のようなセクションで個別設定できるが、**同一ファイル内の埋め込み言語（HTML内の`<script>`のJSなど）には別設定を適用できない**。
- `editor.detectIndentation`（デフォルトtrue）が有効だと、ファイル内の既存インデントを自動検出して設定より優先してしまう。
- `editor.quickSuggestions.strings`（デフォルトfalse）を`true`にすると、`""`の中でも自動補完が出るようになる。ただし列挙型（enumのように決まった値がある属性）でないと候補は出ない（例: `headers`内の`"Content-Type"`のような自由文字列は候補が出ない）。

## つまずいた実例（デバッグの記録）

- `console.log(compare(score))`のように、内部で既に`console.log`している関数の戻り値をさらに`console.log`すると`undefined`が出る。
- `judge(score)`のように、DOM要素そのもの（`.value`を付け忘れ）を関数に渡すと、比較が常にfalseになるなど意図しない挙動になる。
- `fetch`の`.then(response => { response.json() })`で`return`を忘れると、次の`.then`に`undefined`が渡る。
- ブラウザの「Unsafe attempt to load URL ... file: URLs are treated as unique security origins」という警告は、`file://`で直接HTMLを開いたときのブラウザ側の挙動で、コード自体のバグではないことが多い。
