
# LANGUAGE python, cpp, csharp のうちのいずれかを設定してください
LANGUAGE=csharp

run: run-$(LANGUAGE)

run-python:
	python python/main.py

run-cpp: bin/cpp/main
	./bin/cpp/main

run-csharp: bin/csharp/csharp.dll
	dotnet ./bin/csharp/csharp.dll

bin/cpp/main: cpp/main.cpp
	g++ cpp/main.cpp -o bin/cpp/main 1>&2

bin/csharp/csharp.dll: csharp/Program.cs
	dotnet build csharp -o bin/csharp 1>&2

watch:
	./watch.sh "testcases.yaml cpp/main.cpp csharp/Program.cs python/main.py" "python -m atcoder_ctl.scripts.main exec"

.PHONY: run run-python run-cpp run-csharp watch
