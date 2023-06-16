#!/usr/bin/python3

"""Testing the console module for pep8 compliance."""

import unittest
import pep8


class test_Console(unittest.TestCase):
    """ This class tests the compliance of the console module."""

    def test_pep8_compliance(self):
        """Runs styleguide against the module to ensure no errors exist"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
