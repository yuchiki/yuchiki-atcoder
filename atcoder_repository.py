from copyreg import pickle
from fileinput import filename
import sys
from pkg_resources import require
import requests
from parse_test_cases import parse_task
from textwrap import indent
from typing import List
import pickle
import os

from test_case import TestCase


def get_task_url(contest: str, task: str) -> str:
    return f"https://atcoder.jp/contests/{contest}/tasks/{contest}_{task}"


class AtCoderRepository:
    def __init__(self, session_filename):
        self._session_filename = session_filename
        if os.path.isfile(session_filename):
            with open(session_filename, 'rb') as file:
                self._session = pickle.load(file)
        else:
            self._session = requests.session()

    def __del__(self):
        with open(self._session_filename, 'wb') as file:
            pickle.dump(self._session, file)

    def fetch_test_cases(self, contest: str, task: str) -> List[TestCase]:
        url = get_task_url(contest, task)
        task_page = self._session.get(url)
        return parse_task(task_page.text)


def main():
    args = sys.argv

    atcoder_repository = AtCoderRepository("session/session_dump.pkl")
    test_cases = atcoder_repository.fetch_test_cases(args[1], args[2])

    for case in test_cases:
        print(f"CASE-{case.name}")
        print("    input:")
        print(indent(case.given, "        "))
        print("    expected:")
        print(indent(case.expected, "        "))


if __name__ == '__main__':
    main()
