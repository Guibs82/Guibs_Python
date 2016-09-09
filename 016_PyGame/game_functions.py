# 游戏中运用到的函数

import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            """向下按键"""
            if event.key == pygame.K_RIGHT:
                print("11")
                # 向右移动飞船
                # ship.rect.centerx += 1
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                # 向左移动飞船
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            """松开按键"""
            if event.key == pygame.K_RIGHT:
                # 停止向右移动
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                # 停止向左移动
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像, 切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()