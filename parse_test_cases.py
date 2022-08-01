from textwrap import indent
from bs4 import BeautifulSoup
from test_case import TestCase
from typing import List
import requests
import sys


def parse_task(text: str) -> List[TestCase]:
    html = BeautifulSoup(text, 'html.parser')

    sections = html.find('div', id='task-statement').find(
        'span',
        attrs={'class': 'lang-ja'}).find_all('section')

    input_sections = {
        section.find('h3').text.split()[1]: section.find('pre').text
        for section in sections if "入力例" in section.find('h3').text}

    output_sections = {
        section.find('h3').text.split()[1]: section.find('pre').text
        for section in sections if "出力例" in section.find('h3').text}

    return [TestCase(name,  given,  output_sections[name])
            for (name, given) in input_sections.items()]
