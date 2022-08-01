from write_test_cases import write_test_cases
from atcoder_repository import AtCoderRepository
import sys


def main():
    args = sys.argv
    contest = args[1]
    task = args[2]

    atcoder_repo = AtCoderRepository("session/session_dump.pkl")
    test_cases = [case.to_dict()
                  for case in atcoder_repo.fetch_test_cases(contest, task)]
    write_test_cases(test_cases, "testcases.yaml")


main()
