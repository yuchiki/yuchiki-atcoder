"""テストケースを実行するスクリプト"""

from dataclasses import dataclass
from textwrap import indent
from typing import Optional, List
from enum import Enum
import subprocess
from colorama import Fore, Style


class TestStatus(Enum):
    AC = 1
    WA = 2
    ERROR = 3
    JUSTSHOW = 4


@dataclass
class TestResult:
    name: str
    status: TestStatus
    actual: str
    error: str
    expected: Optional[str] = None


def dye(message: str, color: Fore) -> str:
    return color + message + Style.RESET_ALL


def dye_status(status: TestStatus) -> str:
    table = {TestStatus.AC: Fore.GREEN,
             TestStatus.WA: Fore.YELLOW,
             TestStatus.ERROR: Fore.RED,
             TestStatus.JUSTSHOW: Fore.BLUE}

    return dye(status.name, table[status])


@dataclass
class TestCase:
    """テストケース"""
    name: str
    given: str
    expected: Optional[str]

    def execute(self) -> TestResult:
        """テストを実行して結果を返します"""
        completed_process = subprocess.run(
            ["make", "-s", "run"], input=self.given, text=True, capture_output=True)

        if completed_process.returncode != 0:
            return TestResult(self.name, TestStatus.ERROR, actual=completed_process.stdout, error=completed_process.stderr)

        if self.expected is None:
            return TestResult(self.name, TestStatus.JUSTSHOW, actual=completed_process.stdout, error="")

        if self.expected == completed_process.stdout:
            return TestResult(self.name, TestStatus.AC, actual=completed_process.stdout, error="")
        else:
            return TestResult(self.name, TestStatus.WA, actual=completed_process.stdout, expected=self.expected, error="")


class TestCaseSuitParser:
    """ テストケーススイートをパースするクラス"""

    def __init__(self, lines: List[str]):
        self._index = 0
        self._lines = lines

    def _readline(self) -> Optional[str]:
        """ 1行読み込みます"""

        if self._index == len(self._lines):
            return None

        answer = self._lines[self._index]
        self._index += 1

        return answer

    def _read_not_empty_line(self) -> Optional[str]:
        """1行読み込みます。空行の場合は読み飛ばします"""
        line = self._readline()
        if line is None:
            return None
        elif line == "":
            return self._read_not_empty_line()
        else:
            return line

    def parse_test_case_suit(self) -> List[TestCase]:
        """ テストケーススイートをパースします"""

        test_cases = []
        test_case_name = self._read_not_empty_line()

        while test_case_name:
            test_case = self._parse_test_case(test_case_name)
            test_cases.append(test_case)
            test_case_name = self._read_not_empty_line()

        return test_cases

    def _parse_test_case(self, test_case_name: str) -> TestCase:
        """テストケースを一つ読み込みます"""

        given = []

        line = self._readline()
        while line is not None:
            if line == f"{test_case_name}-EXP":
                return TestCase(name=test_case_name, given="\n".join(given) + "\n", expected=self._parse_expected(test_case_name))
            elif line == f"{test_case_name}-END":
                return TestCase(name=test_case_name, given="\n".join(given) + "\n", expected=None)

            given.append(line)
            line = self._readline()

        raise Exception(
            f"{test_case_name}に対応する{test_case_name}-ENDがありません")

    def _parse_expected(self, test_case_name: str) -> str:
        """expected部分を読み込みます"""

        expected = []

        line = self._readline()
        while line is not None:
            if line == f"{test_case_name}-END":
                return "\n".join(expected) + "\n"

            expected.append(line)

            line = self._readline()

        raise Exception(
            f"{test_case_name}に対応する{test_case_name}-ENDがありません")


def execute_and_show(test_cases: List[TestCase]) -> List[TestResult]:
    results = []
    for test_case in test_cases:
        print("-----------------------------------")
        result = test_case.execute()
        print(f"{test_case.name:<15}: {dye_status(result.status)}")
        results.append(result)

        if result.status == TestStatus.JUSTSHOW:
            print("    output:")
            print(indent(result.actual, "       >"))
        if result.status == TestStatus.ERROR:
            print(result.error)
        if result.status == TestStatus.WA:
            print("    expected:")
            print(indent(result.expected, "       >"))
            print("    but got:")
            print(indent(result.actual, "       >"))

    return results


def show_summary(results: List[TestResult]):
    print("========================================")
    print("SUMMARY:")
    for result in results:
        print(f"{result.name:<15}: {dye_status(result.status)}")


def main():
    with open("testcases.txt") as f:
        lines = f.read().splitlines()
    parser = TestCaseSuitParser(lines)
    test_cases = parser.parse_test_case_suit()
    results = execute_and_show(test_cases)
    show_summary(results)


main()
