from ..repositories.test_case import TestCaseRepository
from ..repositories.atcoder import AtCoderRepository
import sys


def main():
    args = sys.argv
    contest = args[1]
    task = args[2]

    atcoder_repo = AtCoderRepository("session/session_dump.pkl")
    test_case_repo = TestCaseRepository("testcases.yaml")

    test_cases = [case.to_dict()
                  for case in atcoder_repo.fetch_test_cases(contest, task)]

    test_case_repo.write(test_cases)


main()
