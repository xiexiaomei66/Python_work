from calculator import *
import unittest
#setUp()\tearDown()里面的内容是一样的话才能这样合并，如不一样的话不能这么合并
class Test_startEnd(unittest.TestCase):
    def setUp(self):
        print('test start!')
    def tearDown(self):
        print('test end!')
class Testadd(Test_startEnd):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)
class Testsub(Test_startEnd):
    def test_sub(self):
        i=Math(7,8)
        self.assertEqual(i.sub(),-1)


if __name__ == '__main__':
    unittest.main()
