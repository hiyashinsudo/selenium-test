# selenium-test
- dockerコンテナ上でスクレイピングができる
  - seleniumを含む任意のpythonコードを実行できる
- コンテナ内のjupyter-labをホストマシンのwebブラウザで操作できる
  - jupyter-labで開発・実行・テストなどできる

# 使い方
Image作成〜コンテナ内に入る

`sh build.sh`

jupyter-lab起動

`jupyter-lab --allow-root --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' --notebook-dir=/app`

jupyter-labに入って開発

`http://localhost:8888/`

あとは自由

# 動作環境
- Intel Mac ○
- M1 Mac ×
