import unittest

from tutorial.solutions.pandas.read_excel_file import read_file_return_dict, read_documentation_for_pandas


class ReadExcelFileTestCase(unittest.TestCase):

    def test_read_documentation_for_pandas(self):
        self.assertTrue(read_documentation_for_pandas())

    def test_read_excel_file_to_dict(self):
        res = read_file_return_dict("../resources/sample.xlsx")
        self.assertEqual({0: 95110, 1: 95120, 2: 95130}, res['zipcode'])


if __name__ == '__main__':
    unittest.main()
