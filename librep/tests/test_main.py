#!/usr/bin/env python
"""Unit test script"""

import filecmp
import os
import unittest
from subprocess import run


class MainTestCase(unittest.TestCase):
    """Test class for puma.histogram_plot"""

    def setUp(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

    def test_librep(self):
        """Test simple example file."""
        input_filename = f"{self.dir_path}/fixtures/test_input.md"
        output_filename = f"{self.dir_path}/fixtures/output.md"
        exp_output_filename = f"{self.dir_path}/fixtures/expected_output.md"
        command = f"librep -i {input_filename} -o {output_filename}"
        print(command)
        self.assertEqual(
            run(command, shell=True, check=True).returncode,
            0,
        )
        self.assertTrue(filecmp.cmp(output_filename, exp_output_filename))
