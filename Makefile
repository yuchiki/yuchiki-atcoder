
# LANGUAGE python, cpp, csharp のうちのいずれかを設定してください
LANGUAGE=python

run: run-$(LANGUAGE)

run-python:
	python python/main.py

run-cpp: bin/cpp/main
	./bin/cpp/main

run-csharp: bin/csharp/csharp.dll
	dotnet ./bin/csharp/csharp.dll

bin/cpp/main: cpp/main.cpp
	g++ cpp/main.cpp -o bin/cpp/main

bin/csharp/main.dll:
	dotnet build csharp -o bin/csharp

.PHONY: run run-python run-cpp run-csharp
