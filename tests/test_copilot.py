import unittest

from copilot.date_utils import calculate_date_difference
from copilot.file_utils import open_pdf_file


class TestCopilot(unittest.TestCase):
    def test_1(self):
        print('test')
        text = "Python is a great programming language"
        print(text)

    def test_2(self):
        diff = calculate_date_difference(1, 2)
        print(diff)

    def test_open_pdf_file(self):
        # print('test')
        # text = "Python is a great programming language"
        # print(text)
        # open_pdf_file('tests/test.pdf')
        result = open_pdf_file('../test_data/Table Example - Starting.pdf')
        print(result)
        print(type(result))
        print("\n\n".join(result))