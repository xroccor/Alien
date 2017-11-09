#! /usr/bin/python
# -*- coding: utf-8 -*-
class Setting(object):
    def __init__(self):
        #窗口设置
        self.bg_color = (250,250,250)
        self.screen_size = (1200,700)

        #飞船移速设置
        self.ship_move_speed = 5

        #子弹设置
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60,100,60)
        self.bullet_max = 15

        #外星人设置
        self.alien_speed = 5
        self.alien_speed_drop = 50
        #外星人方向，为1则为右移，为-1则为左移
        self.alien_direction = 1

        #统计信息设置
        self.ship_limit = 1