import pygal

wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

wm.add('China', {'中国': 66666}) # 鼠标悬浮提示

wm.render_to_file('china.svg')