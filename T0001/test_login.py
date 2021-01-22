# -*- coding: UTF-8 -*-
#import unittest
from etcshop_login_testcase import EtcLoginTest
import pytest
class Testlogin:
    def test_login(self):
        EtcLoginTest().test_etclogin
if __name__ == '__main__':
    pytest.main(['Testlogin.py'])
