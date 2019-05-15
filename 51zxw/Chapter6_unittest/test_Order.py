import unittest

#执行循序：数字从小到大（0-9），英文从a-z(A-Z)
class Test2(unittest.TestCase):
    def setUp(self):
        print('Test2 start')
    def test_c(self):
        print('test_c')
    def test_b(self):
        print('test_b')
    def tearDown(self):
        print('Test1 end!')
class Test1(unittest.TestCase):
    def setUp(self):
        print('Test1 start')
    def test_d(self):
        print('test_d')
    def test_a(self):
        print('test_a')
    def tearDown(self):
        print('Test1 end!')
# if __name__ == '__main__':
#     unittest.main()
#如果不想让他默认的排序，则手动装载方法
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Test2('test_c'))
    suite.addTest(Test2('test_b'))
    suite.addTest(Test1('test_a'))
    suite.addTest(Test1('test_d'))
    runner=unittest.TextTestRunner()
    runner.run(suite)