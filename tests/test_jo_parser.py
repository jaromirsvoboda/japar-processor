import unittest

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from japar_processor.jo_parser import JoParser

class TestJoParser(unittest.TestCase):
    def test_parse(self):
        # Define a test string
        # test_string = """
        # NAPETI S[MPa]  <_LIMITY L[MPa]_>  ZATEZOVACI STAV 12 kSei
        # Some text here...
        # ________________________________________________________________________________________
        # """

        # Call the parse method
        with open("example_inputs/test_short.jo", 'r') as file:
            result = JoParser.parse(file.read())

        # Check the resulthow 
        # This will depend on what you expect the result to be
        # For this example, let's assume the parse method should return a list of tuples
        self.assertEqual(result, [("NAPETI S[MPa]  <_LIMITY L[MPa]_>  ZATEZOVACI STAV 12 kSei\nSome text here...\n________________________________________________________________________________________", "12")])

if __name__ == '__main__':
    unittest.main()