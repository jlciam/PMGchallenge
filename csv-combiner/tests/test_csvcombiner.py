import unittest
import pytest

from csvcombiner import correct_arguments
from csvcombiner import grab_headers
from csvcombiner import csv_combine
from csvcombiner import main as csv_main

accessories = 'accessories.csv'
clothing = 'clothing.csv'
household_cleaners = 'household_cleaners.csv'
combined_all = 'email_hash,category,file_name\r\n' \
 'b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Satchels,accessories.csv\r\n' \
 'c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Purses,accessories.csv\r\n' \
 'b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Blouses,clothing.csv\r\n' \
 'c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Shirts,clothing.csv\r\n' \
 'b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Kitchen ' \
 'Cleaner,household_cleaners.csv\r\n' \
 'c2b5fa9e09ef2464a2b9ed7e351a5e1499823083c057913c6995fdf4335c73e7,Kitchen ' \
 'Cleaner,household_cleaners.csv\r\n'

main_args = accessories + " " + clothing + " " + household_cleaners
command = ["python", "csvcombiner.py", accessories, clothing, household_cleaners]
test_wrong_file = 'incorrect.txt'
test_wrong_path = './wrong/incorrect.txt'
expected_headers = ["email_hash", "category", "file_name"]


class CsvCombinerTest(unittest.TestCase):

    def test_input_errors(self):
        # Test valueError is thrown for path not existing
        self.assertRaises(FileNotFoundError, correct_arguments, [accessories, test_wrong_path])
        # Test valueError is thrown for non-csv file
        self.assertRaises(TypeError, correct_arguments, [accessories, test_wrong_file])

    def test_grab_headers(self):
        # Test the expected headers are returned
        self.assertEqual(grab_headers(accessories), expected_headers)

    # This helps to capture the stdout of tests
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_combine(self):
        # Test combine function works
        csv_combine([accessories, clothing, household_cleaners])
        captured = self.capsys.readouterr()
        self.assertEqual(combined_all, captured.out)

    def test_all_happy_path(self):
        # Test that all the units work together for unit test completeness
        csv_main([accessories, clothing, household_cleaners])
        captured = self.capsys.readouterr()
        self.assertEqual(combined_all, captured.out)


if __name__ == '__main__':
    unittest.main()
