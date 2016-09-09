from survey import AnonymousSurvey

# 定义一个问题, 并创建一个表示调查的AnonymousSurvey对象
question = "你会什么语言?\n"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("输入q退出程序\n")
while True:
    response = input("会的语言是: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("谢谢参与调查")
my_survey.show_results()