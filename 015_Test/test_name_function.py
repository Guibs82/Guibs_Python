# 单元测试: 用于合适函数的某个方面没有问题
# 测试用例: 是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求
# 要为函数写测试用例, 可先导入模块 unittest 以及要测试的函数
#   再创建一个集成 unittest.TestCase 的类
#       并编写一系列方法对函数行为的不同方面进行测试

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试 name_function"""

    def test_first_last_name(self):
        """能够正确拼写么"""
        formatted_name = get_formatted_name('Guibs','G')
        self.assertEqual(formatted_name, 'Guibs G')# 使用断言对结果进行检测

    def test_first_last_middle_name(self):
        """能够正确拼写么"""
        formatted_name = get_formatted_name('Guibs', 'G', 'Joker')
        self.assertEqual(formatted_name, 'Guibs Joker G')  # 使用断言对结果进行检测

# unittest.main()
# 由于 PyCharm 中自带了一个 utrunner.py 的脚本负责调用测试用例进行测试
    # 因而不需写unittest.main
