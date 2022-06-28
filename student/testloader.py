import unittest

from HtmlTestRunner import HTMLTestRunner

# 用testloader对象的discover方法来自动查找.py文件
# ”./“是处于当前目录下查找   ”my*.py“是模糊my”*“通配符查找后面不确定的文件
suite = unittest.TestLoader().discover("./", "my*.py")
# runner=unittest.TextTestRunner()
# runner.run(suite)

# testSuite 需要手动添加测试用例，可以添加测试用例的类，也可以添加测试类中的某个方法
# testLoader 指定搜索目录文件'**.py'并且只能全部添加所有类和所有方法，不能指定添加类里面的方法
# 添加指定的  用suite  添加全部 用loader
# run是跑起来的

f = open("test01.html", "w", encoding="utf-8")
# runner=unittest.TextTestRunner(stream=f,verbosity=2)
runner = HTMLTestRunner(stream=f, verbosity=2, report_title='AAAA')
# runner=HTMLTestRunner(stream=f,verbosity=2,title="自动化测试")#有title报错。
# 无法生成html测试报告  只能生成txt文档进行基础查看，无法形成正规的html测试报告。
runner.run(suite)
f.close()
