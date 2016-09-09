# 测试 AnonymousSurvey 类
import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """针对 AnonmyousSurvey 类的测试"""

    # setUp() 方法, 让我们只需创建某些对象一次, 并在每个测试方法中都可以使用它们
    # 如果在 TestCase 类中包含了 setUp(), Python 将先运行它, 再运行各个以 test_ 打头的方法
    def setUp(self):
        """创建一个调查对象和一组答案, 供使用的测试方法使用"""
        question = "你会什么语言?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Swift', 'Python', 'JS']

    def test_sotre_single_response(self):
        """测试单个答案会被妥善地存储"""
        # question = "你会什么语言?" # 由于 setUp(), 进行修改
        # my_survey = AnonymousSurvey(question) # 由于 setUp(), 进行修改
        # my_survey.store_response('Python') # 由于 setUp(), 进行修改
        self.my_survey.store_response(self.responses[0])

        # 测试 my_survey.responses 中是否含有 'Python'
        # self.assertIn('Python', my_survey.responses) # 由于 setUp(), 进行修改
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """测试单个答案会被妥善存储"""
        # question = "你会什么语言?" # 由于 setUp(), 进行修改
        # my_survey = AnonymousSurvey(question) # 由于 setUp(), 进行修改
        # responses = ['Swift', 'Python', 'JS'] # 由于 setUp(), 进行修改
        # for response in responses: # 由于 setUp(), 进行修改
        #     my_survey.store_response(response) # 由于 setUp(), 进行修改
        for response in self.responses:
            self.my_survey.store_response(response)

        # 测试 my_survey.responses 中是否含有 'Swift', 'Python', 'JS'
        # for response in responses: # 由于 setUp(), 进行修改
        #     self.assertIn(response, my_survey.responses) # 由于 setUp(), 进行修改
        for  response in self.responses:
            self.assertIn(response, self.my_survey.responses)

# 注意:
#   在 Python 原始环境中(例如: 终端下)
#       每完成一个单元测试, Python 都打印一个字符:
#             测试通过时打印一个[ . ]
#             测试引发错误时打印一个[ E ]
#             测试导致断言失败时打印一个[ F ]
