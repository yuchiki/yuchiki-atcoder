# 概要
atcoder用のrepository

# 最初にやること

- makefileの先頭の LANGUAGE を指定しろ！
- make watch をたたいて watch modeをオンにしろ！
    - watch modeとは？？？
        - ソースコードとテストケースの変更を検知して、testcases.txtに書かれたテストケースを都度走らせてくれるモードです

# コードを書くところ

cpp/main.cpp か
csharp/Program.cs か
python/main.py

# テストケースを書くところ

testcases.txt

以下の形式で書いてください。


```
TEST1
ここに
入力を
書く
TEST1-END

TEST2
ここに入力
を
書く
TEST2-EXP
期待される
出力も
書ける
TEST2-END

TEST3
テストケースは
いくつでも
書ける
TEST3-EXP
たくさん
書こう！
TEST3-END

FOOBARBAZ
ケース名は
それなりに
自由が効く
FOOBARBAZ-END

```
