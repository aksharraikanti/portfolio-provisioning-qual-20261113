import subprocess
import sys
import unittest


class CommandLineTests(unittest.TestCase):
    def test_version(self):
        result = subprocess.run(
            [sys.executable, "-B", "-m", "portfolio_provisioning_qual_20261113", "--version"],
            check=True, capture_output=True, text=True,
        )
        self.assertRegex(result.stdout, r"^\d+\.\d+\.\d+\n$")
