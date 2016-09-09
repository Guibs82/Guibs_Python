import pygame

class Ship():
    """飞船类"""

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') # 返回一个表示飞船的 surface 保存到 image变量 中
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 设置 center 为小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center # rect.centerx 只存储 center 的整数部分

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)