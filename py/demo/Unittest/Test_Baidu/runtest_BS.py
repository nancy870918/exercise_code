# 执行测试用例模块
import unittest
#报告模块
from BSTestRunner import BSTestRunner
import time
#发邮件模块



test_dir='./test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_mathfunc.py")

if __name__=='__main__':
    report_dir='./test_report'
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    report_name=report_dir+'/'+now+'result.html'

    with open(report_name,'wb') as f:
        runner=BSTestRunner(stream=f,title="TestReport",description="baidu search")
        runner.run(discover)
    f.close()