import yaml
from test_case import TestCase
from typing import List


def write_test_cases(test_cases: List[TestCase], filename: str):

    def str_presenter(dumper, data):
        if len(data.splitlines()) > 1:  # check for multiline string
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    yaml.add_representer(str, str_presenter)

    with open(filename, "w") as file:
        yaml.dump(test_cases, file, sort_keys=False)
