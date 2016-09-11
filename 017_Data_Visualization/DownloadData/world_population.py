import json

import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

from country_codes import get_country_code

# 加载数据
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个人口数量的字典
cc_populations = {}

# 打印每个国家2010人口
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print("无代码国家" + country_name)

# 根据人口将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 每组包含的国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 设置样式
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

wm = pygal.Worldmap(style=wm_style)

wm.tilte = "世界人口"
# vm.add('2010', cc_populations) # 悬浮提示: [2010] cc_populations[key]: cc_populations[value]
wm.add('0-10m', cc_pops_1)
wm.add('10-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)


wm.render_to_file('world_population.svg')
