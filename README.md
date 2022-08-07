# 概要
atcoder用のrepository


![テストランナーの図](docs/watch-system.png)

# 最初にやること

- makefileの先頭の LANGUAGE を指定しろ！
- `python -m atcoder-ctl.services.fetch_task abc162 b` などのようにして、テストケースをfetchして来よう。
- make watch をたたいて watch modeをオンにしろ！
    - watch modeとは？？？
        - ソースコードとテストケースの変更を検知して、testcases.txtに書かれたテストケースを都度走らせてくれるモードです

# コードを書くところ

cpp/main.cpp か
csharp/Program.cs か
python/main.py

# テストケース
testcases.yaml にあります。
