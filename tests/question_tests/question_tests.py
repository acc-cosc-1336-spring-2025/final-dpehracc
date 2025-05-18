import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

from src.question_a.question_a import get_most_likely_ancestor_consensus

class TestDNAConsensus(unittest.TestCase):
    def test_dna_substring(self):
        a, b, c = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        self.assertEqual(a, 2)
        self.assertEqual(b, 4)
        self.assertEqual(c, 10)

if __name__ == "__main__":
    unittest.main()

