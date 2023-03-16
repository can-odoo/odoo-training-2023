import unittest
from Calculator import *

class TestCase1(unittest.TestCase) :
    
    def setUp(self):
        self.calc = Calculator()
        # print("setup caled")

    def test_method(self):
        sum = self.calc.add(2,4)
        print("Sum : ", sum)
        self.assertEqual(sum,6,'answer should be 6')
        listitem = [1,2,3,4,5,6,7,8,9]
        # self.assertIn(sum, listitem)
        # self.assertNotIn(9,listitem)

    # def test_method2(self):
    #     print("test method2 called")

    # def tearDown(self):
    #     print("tear down called")

unittest.main()                  
    