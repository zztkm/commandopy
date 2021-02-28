# wip Commando

Commando(コマンドー)。

コマンドラインツールを脳筋で実行していくバッチ処理のためのフレームワーク。
基本的にPythonの構文でワークフローを構築できるので、バッチ処理での変数の取り回しなどがしやすいのがメリット。

Shell Script や Bat ファイルを書かなくても実行したいコマンドさえわかっていればバッチ処理が書ける。

**コンセプト**
- バッチ処理ワークフローを構築するためのフレームワーク
- 逐次処理で書く
- 外部コマンドに関しては subprocess.run()が走る

**Feature**
- add()でコマンド追加
- 追加された順に処理する
- execute() で追加されたコマンドの実行
- 関数もコマンドとして実行できる

**課題**
- エラーハンドリングとかどうする？
	- エラーがあればすぐに落とす仕様にする？？？


## Usage

以下のイメージで使えるようにする予定です。

```python
 import os
 from pathlib import Path
 
 from commando import commando
 
 
 def set_mycmd_path():
     os.environ["MY_COMMAND_PATH"] = "C:\\\\Users\\me\\cmd\\mycmd.exe"
 
 
 # コマンド文字列
 commando.add("mkdir test")
 # リスト形式のコマンド
 commando.add(["touch", "test\test.txt"])

 # 独自定義の関数
 commando.add(set_mycmd_path)
 
 # 追加した順でコマンドを実行
 commando.execute()
```