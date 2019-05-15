from calculator import Math
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start!")
    def test1(self):
        j=Math(5,10)
        #添加断言
        self.assertEqual(j.add(),15)
        #会失败的断言
        #self.assertEqual(j.add(),12)
        print(j.add())
    def assertNotEqual_test(self):
         j=Math(3,6)
         self.assertNotEqual(j.add(),12)
    def assertTrue_test(self):
        j=Math(5,10)
        self.assertTrue(j.add()<10)
    def assertIn_test(self):
        self.assertIn("51zxw","Hello,51zxw")
    def assertIs_test(self):
        self.assertIs("51zxw","51zxw")
        self.assertIs("51","51zxw")
    def tearDown(self):
        print("test end!")
#运行的时候要选中下面代码运行不然会报错
if __name__=='__main__':
    suite=unittest.TestSuite()
    #将方法装载到TestSuite中
    suite.addTest(TestMath('assertIs_test'))
    runner=unittest.TextTestRunner()
    runner.run(suite)