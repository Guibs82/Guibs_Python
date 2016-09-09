class Settings():
    """存储 Alienware 大战的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (21, 154, 237) # RGB 此处为一种蓝色

        # 飞船的设置
        self.ship_speed_factor = 1.5