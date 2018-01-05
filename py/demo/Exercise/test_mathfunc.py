# -*- coding: utf-8 -*-

import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfunc.py"""
    @classmethod
    def setUp(self):
        print("do something before test.Prepare environment.")
    def tearDown(self):
        print("do something after test.Clean up.")

    def test_add(self):
        """Test method add(a,b)"""
        print("add")
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2))

    def test_minus(self):
        """Test method miuns(a,b)"""
        print("minus")
        self.assertEqual(1,minus(3,2))

    def test_multi(self):
        """Test method multi(a,b)"""
        print("multi")
        self.assertEqual(6,multi(2,3))

    def test_divide(self):
        """Test method divide(a,b)"""
        print("divide")
        self.assertEqual(2,divide(6,3))
        self.assertEqual(2,divide(5,2))

if __name__=='__main__':
    unittest.main(verbosity=2)