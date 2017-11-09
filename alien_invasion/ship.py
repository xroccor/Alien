#! /usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Ship():
    def __init__(self,setting,screen):

        self.screen = screen

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #设置移动标志
        self.moving_right_mark = False
        self.moving_left_mark = False

        #设置飞船移动速度
        self.ship_move_speed = setting.ship_move_speed

    def ship_move(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right_mark and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ship_move_speed
        if self.moving_left_mark and self.rect.left > 0:
            self.rect.centerx -= self.ship_move_speed

    def center_ship(self):
        '''将飞船放在中间'''
        self.rect.x = self.screen_rect.centerx

    def blitme(self):
        '''将飞船显示在桌面上'''
        self.screen.blit(self.image,self.rect)