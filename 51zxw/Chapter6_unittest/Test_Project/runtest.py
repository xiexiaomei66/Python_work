import unittest
#如果是其他路径就写绝对路径，注意路径的转译
#test_dir='D:\learning\Python_workspace\\51zxw\Chapter6_unittest'
test_dir='./'
discovery=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discovery)