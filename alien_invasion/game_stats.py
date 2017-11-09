#! /usr/bin/python
# -*- coding: utf-8 -*-
class GameStats():
    '''记录游戏统计信息'''

    def __init__(self,setting):
        '''初始化'''
        self.setting = setting
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        '''初始化记录信息'''
        self.ships_left = self.setting.ship_limit