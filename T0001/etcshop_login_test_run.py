# -*- coding: UTF-8 -*-
import unittest
from etcshop_login_testcase import EtcLoginTest
from tools.HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
#suite.addTest(unittest.makeSuite(EtcLoginTest))
suite.addTest(unittest.makeSuite(EtcLoginTest))

with open("./reports/etcshop_login_test_report.html","wb") as f:
    h=HTMLTestRunner(stream=f,title="etc登录模块自动化测试报告",description="windows10 chrome")
    h.run(suite)
