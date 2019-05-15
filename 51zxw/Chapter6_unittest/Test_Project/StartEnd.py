import unittest
class Setup_tearDown(unittest.TestCase):
    def setUp(self):
        print('Test start!')
    def tearDown(self):
        print('Test End!')