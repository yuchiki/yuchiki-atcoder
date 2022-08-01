

from colorama import Fore, Style
import subprocess
from enum import Enum
from typing import Dict, Optional, List
from dataclasses import dataclass

from yaml import YAMLObject


class TestStatus(Enum):
    AC = 1
    WA = 2
    ERROR = 3
    JUSTSHOW = 4

    def _dye(self, message: str, color: Fore) -> str:
        return color + message + Style.RESET_ALL

    @property
    def dyed(self) -> str:
        table = {TestStatus.AC: Fore.GREEN,
                 TestStatus.WA: Fore.YELLOW,
                 TestStatus.ERROR: Fore.RED,
                 TestStatus.JUSTSHOW: Fore.BLUE}

        return self._dye(self.name, table[self])


@dataclass
class TestResult:
    name: str
    status: TestStatus
    actual: str
    error: str
    expected: Optional[str] = None


@dataclass
class TestCase(YAMLObject):
    """テストケース"""
    name: str
    given: str
    expected: Optional[str]

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "given": self.given,
            "expected": self.expected
        }

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
