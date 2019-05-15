import unittest
from function import *
from HTMLTestRunner import HTMLTestRunner
import time


report_dir='D:\learning\Python_workspace\Sunfobank_test\AutoTest\Website\\test_report'
test_dir='D:\learning\Python_workspace\Sunfobank_test\AutoTest\Website\\test_case'

print('start run test case...')
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+'result.html'

print("start write report...")
with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title='Test Report',description='Sunfobank login test')
    runner.run(discover)
    f.close()
print('find latest report')
latest_report=latest_report(report_dir)

print('send email report...')
send_email(latest_report)
print('Test end!')

