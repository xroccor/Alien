#! /usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,setting,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # #设置外星人的初始位置
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        # #储存外星人的精确X的位置
        # self.x = float(self.rect.x)
        #储存外星人移动速度
        self.speed = setting.alien_speed
        #储存外星人移动方向
        self.alien_direction = setting.alien_direction

    # def blitme(self):
    #     #显示外星人
    #     print self.rect
    #     self.screen.blit(self.image,self.rect)
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        #更新外星人位置
        self.rect.x += (self.setting.alien_direction * self.speed)

    def check_edges(self):
        #检测外星人群是否到达边缘，如果到达，则回头
        if self.rect.right >= self.screen.get_rect().right \
                or self.rect.left <= 0:
            return True

