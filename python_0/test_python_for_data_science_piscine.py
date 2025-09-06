# test_format_ft_time.py
import unittest
import subprocess
import re
from datetime import datetime

class TestEx00(unittest.TestCase):
    def test_ex00_output(self):
        result = subprocess.run(['python3', 'ex00/Hello.py'], 
                                capture_output=True, text=True)
        
        # Check that the script ran successfully
        self.assertEqual(result.returncode, 0)

        # Split output into lines
        lines = result.stdout.strip().split('\n')

        # Test if we have 4 lines
        self.assertEqual(len(lines), 4)

        # Test if the result matches the expected
        self.assertEqual(lines[0], "['Hello', 'World!']")
        self.assertEqual(lines[1], "('Hello', 'Brazil!')")
        self.assertEqual(lines[2], "{'Hello', 'São Paulo!'}")
        self.assertEqual(lines[3], "{'Hello': '42SãoPaulo!'}")

class TestEx01(unittest.TestCase):
    
    def test_ex01_output(self):
        # Run the script and capture output
        result = subprocess.run(['python3', 'ex01/format_ft_time.py'], 
                              capture_output=True, text=True)
        
        # Check that the script ran successfully
        self.assertEqual(result.returncode, 0)
        
        # Split output into lines
        lines = result.stdout.strip().split('\n')
        
        # Test that we have exactly 2 lines
        self.assertEqual(len(lines), 2)
        
        # Test first line (epoch time format)
        first_line = lines[0]
        epoch_pattern = r"Seconds since January 1, 1970: [\d,]+\.\d{4} or \d\.\d{2}e\+\d{2} in scientific notation"
        self.assertRegex(first_line, epoch_pattern)
        
        # Test second line (date format)
        second_line = lines[1]
        date_pattern = r"[A-Za-z]{3} \d{2} \d{4}"
        self.assertRegex(second_line, date_pattern)
        
        # Additional checks to ensure the values make sense
        # Extract the epoch time from first line
        epoch_match = re.search(r"1,[\d,]+\.\d{4}", first_line)
        self.assertIsNotNone(epoch_match, "Should contain epoch time starting with 1,")
        
        # Extract scientific notation
        scientific_match = re.search(r"\d\.\d{2}e\+\d{2}", first_line)
        self.assertIsNotNone(scientific_match, "Should contain scientific notation")
        
        # Verify the date is reasonable (not too far in past/future)
        current_year = datetime.now().year
        year_match = re.search(r"\d{4}", second_line)
        if year_match:
            output_year = int(year_match.group())
            # Allow some flexibility (within 1 year of current)
            self.assertGreaterEqual(output_year, current_year - 1)
            self.assertLessEqual(output_year, current_year + 1)

    def test_ex01_specific_format_structure(self):
        # Run the script
        result = subprocess.run(['python3', 'ex01/format_ft_time.py'], 
                              capture_output=True, text=True)
        
        lines = result.stdout.strip().split('\n')
        
        # More specific tests for format structure
        first_line = lines[0]
        
        # Check that comma separators are present in epoch time
        self.assertIn(',', first_line)
        
        # Check that scientific notation follows the pattern X.XXe+XX
        scientific_pattern = r"\d\.\d{2}e\+\d{2}"
        self.assertTrue(re.search(scientific_pattern, first_line))
        
        # Check date format is "Mon DD YYYY"
        second_line = lines[1]
        date_parts = second_line.split()
        self.assertEqual(len(date_parts), 3)  # Month Day Year
        
        # Month should be 3 letters
        self.assertEqual(len(date_parts[0]), 3)
        
        # Day should be 2 digits
        self.assertEqual(len(date_parts[1]), 2)
        self.assertTrue(date_parts[1].isdigit())
        
        # Year should be 4 digits
        self.assertEqual(len(date_parts[2]), 4)
        self.assertTrue(date_parts[2].isdigit())

if __name__ == '__main__':
    unittest.main()
