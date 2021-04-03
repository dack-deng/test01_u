# 导包
# import unittest
# # 参数化；导包：
# from parameterized i
import unittest

def add(x, y):
    z = x + y
    return z


# 使用TestCase类

class Test_add(unittest.TestCase):

    def testadd01(self):
        self.assertEqual(7, add(3, 4))
        print('执行第一条测试用例')

    def testadd02(self):
        self.assertEqual(None, add(2, 4))
        print('执行第二条测试用例')

    def testadd03(self):
        self.assertEqual(6.5, add(2.1, 4.4))
        print('执行第三条测试用例')

    # 一下是参数化的方法
    # def build_data():
    #     return [(6, 2, 4), (-1, 3, -4), (5.5, 2.3, 3.2)]
    #
    # @parameterized.expand(build_data)
    # def testadd(self, c, a, b):
    #     res = add(a, b)
    #     self.assertEqual(c, res)


"""
使用TestSuite类
1.addtest(test)
2.addtests(tests)
"""

if __name__ == '__main__':
    suite = unittest.TestSuite()  # 类名要加（）
    suite.addTest(Test_add('test01'))
    runner = unittest.TextTestRunner
    runner.run(suite)
