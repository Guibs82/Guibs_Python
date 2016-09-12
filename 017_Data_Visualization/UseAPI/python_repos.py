import requests
import pygal

# 执行 API 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url=url)
print('Status code: ', r.status_code) # 200: 请求成功

# 将 API响应 存储在一个变量中
response_dict = r.json() # 使用 [.json] 将结果转换为 Python 字典
# 打印字典中的所有键
print(response_dict.keys())

# 仓库总数
print("共有仓库:", response_dict['total_count'], "个")

# 探索有关仓库信息
repo_dicts = response_dict['items']
print("返回仓库信息:", len(repo_dicts), "个")

# 研究第一个仓库
# repo_dict = repo_dicts[0]

# 打印该仓库的字典对象的键数目和名称
# print("\nKeys:", len(repo_dict))
# for  key in sorted(repo_dict.keys()):
#     print(key)

# 打印所有仓库信息
# for repo_dict in repo_dicts:
#     print("\n这个仓库的大致信息如下:")
#     print("项目名称:", repo_dict['name'])
#     print("所有人:", repo_dict['owner']['login'])
#     print("Stars:", repo_dict['stargazers_count'])
#     print("仓库地址:", repo_dict['html_url'])
#     print("创建日期:", repo_dict['created_at'])
#     print("更新日期:", repo_dict['updated_at'])
#     print("描述:", repo_dict['description'])

# 可视化
names, stars, urls = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

chart = pygal.Bar(x_label_rotation=45, show_legend=False) # 使用 Bar() 创建简单的条形图
chart.title = "最受欢迎的 Python Project on GitHub"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
