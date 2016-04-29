import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(__file__) + '/../')
from qgreports.scripts.add_scans import main

class TestAddScans(unittest.TestCase):

    def setUp(self):
        self.p = sys.path[:]

    def tearDown(self):
        sys.path = self.p[:]

    def test_main(self):
        main(os.path.dirname(__file__) + '/test_add_scans.json')