import unittest  # 导入unittest模块包

from parameterized import parameterized  # 导入parameterized包


# 以下的setUp Module、tearDown Module是模块级
# def setUpModule():
#     print("模块级setUpModule被调用了")
# def tearDownModule():
#     print("模块级tearDownModule被调用了")

def my_sum(a, b):  # 创建方法
    return a + b


# def my_rand():#定义一个 返回1-5之间的一个随机数
#     return random.randint(1,5)


# 创建类，继承unittest模块里面的testcase
# testcase是测试用例，指单条  suite是多个case打包一起运行，
# 类中的每个方法名必须以test开头，
class my_test(unittest.TestCase):
    # 以下的setUp、tearDown都是属于方法级
    # 类级是：@classmethod def setUpClass(cls)和@classmethod def tearDownClass(cls)
    # def setUp(self) :#fixture的每条测试用例开始前调用了
    #     print("方法级setup调用了")
    # def tearDown(self):#fixture的每条测试用例结束后调用了
    #     print("方法级teardown被调用了")
    # 以下的setUpClass、tearDownClass都是属于类级
    # 类级别只会在每个类中开始跟结束均执行一次
    # 类级的fixture一定要使用类方法
    # @classmethod
    # def setUpClass(cls):
    #     print("类级setUpClass被调用了")
    # @classmethod
    # def tearDownClass(cls):
    #     print("类级tearDownClass被调用了")

    # 场景一：@parameterized.expan的用法
    @parameterized.expand([(1, 2, 3), (5, 6, 11), (1, 4, 5), (5, 6, 11)])
    # 场景2
    # list1=[(1, 2, 3), (5, 6, 11), (1, 4, 5),(5,6,11)]
    # #定义@parameterized.expand的数组化
    # @parameterized.expand(list1)

    # 场景3
    # def get_data():
    #     return  [(1, 2, 3), (5, 6, 11), (1, 4, 5), (5, 6, 11)]
    # @parameterized.expand(get_data())
    # assert=断言  Equal=相等   assertEqual是属于unittest.TestCase的子类，
    # 可以直接通过unittest.TestCase调用assertEqual
    def test_001(self, a, b, c):  # 编写测试用例
        # a是调用my_sum的第一个参数
        # b是调用my_sum的第2个参数
        # c是预期结果
        num = my_sum(a, b)
        self.assertEqual(num, c)

    # def test_003(self):
    #     num=my_rand()
    #     self.assertIn(num,[1,2,3,4,5])

# 跳过测试用例
# @unittest.skip
# def test_002(self):
#      pass;
