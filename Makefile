
# LANGUAGE python, cpp, csharp のうちのいずれかを設定してください
LANGUAGE=csharp

run: run-$(LANGUAGE)

run-python:
	python python/main.py < input.txt

run-cpp: bin/cpp/main
	./bin/cpp/main < input.txt

run-csharp: bin/csharp/csharp.dll
	dotnet ./bin/csharp/csharp.dll < input.txt

bin/cpp/main: cpp/main.cpp
	g++ cpp/main.cpp -o bin/cpp/main

bin/csharp/csharp.dll: csharp/Program.cs
	dotnet build csharp -o bin/csharp

watch:
	./watch.sh "input.txt cpp/main.cpp csharp/Program.cs python/main.py" "make run"

.PHONY: run run-python run-cpp run-csharp watch
