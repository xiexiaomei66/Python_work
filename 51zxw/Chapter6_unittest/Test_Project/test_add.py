from calculator import *
import unittest
from  StartEnd import *
class Test_add(Setup_tearDown):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)
    def test_add1(self):
        i=Math(8,8)
        self.assertEqual(i.add(),16)