import sys

import pygame

from settings import Settings
from ship import Ship

import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    # 生成保存游戏设置参数的 Setting 对象
    ai_settings = Settings()

    # Pygame 中原点位于左上角
    # 在 Pygame 中, surface 是屏幕的一部分, 用于显示游戏元素
    # screen 就是一个 surface. display.setmode() 返回的 surface 表示整个游戏窗口
    # 我们激活游戏的动画循环后, 每经过一次循环都将自动重绘这个 surface
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # 创建显示窗口 尺寸参数为元组
    pygame.display.set_caption("Alienware大战")

    # 设置背景颜色
    bg_color = (ai_settings.bg_color)

    # 创建飞船对象
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get(): # pygame.event.get() 用来访问检测事件
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship)

        # 根据按键进行相应的响应
        ship.update_position()

        # 每次循环时都重绘屏幕
        # screen.fill(bg_color) # 修改背景色
        # ship.blitme() # 绘制飞船
        #
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship)

run_game()