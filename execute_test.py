"""テストケースを実行するスクリプト"""

from dataclasses import dataclass
from textwrap import indent
from typing import Optional, List
from enum import Enum
import subprocess
from colorama import Fore, Style
from test_case import TestCase, TestStatus, TestResult
from read_write_test_cases import read_test_cases, write_test_cases


def execute_and_show(test_cases: List[TestCase]) -> List[TestResult]:
    results = []
    for test_case in test_cases:
        print("-----------------------------------")
        result = test_case.execute()
        print(f"{test_case.name:<15}: {result.status.dyed}")
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
        print(f"{result.name:<15}: {result.status.dyed}")


def main():
    test_cases = read_test_cases("testcases.yaml")
    results = execute_and_show(test_cases)
    show_summary(results)


main()
