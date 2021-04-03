print('hello werld')
print('hhhhhhh')
# unittest.skip方法
import unittest
version = 30

def add(x, y):
    z = x + y
    return z
class Test_add(unittest.TestCase):

    @unittest.skip('此条测试用例未修改完成，暂时不测试')
    def testadd01(self):
        print('=======执行测试用例01==========')
        self.assertEqual(6, add(2, 4))

    def testadd02(self):
        print('=======执行测试用例02==========')
        self.assertEqual(-2, add(-4, 2))

    @unittest.skipIf(version <= 30, '此次版本不是最新版本暂时不测试')
    def testadd03(self):
        print('=======执行测试用例03==========')
        self.assertEqual(6.4, add(3.3, 3.1))

if __name__ == '__main__':
    suite = unittest.TestSuite
    suite.addTest(Test_add('testadd01'))
    runner = unittest.TextTestRunner
    runner.run(suite)
