#! /usr/bin/python
# -*- coding: utf-8 -*-
import setting as game_setting
import game_function as gf
import pygame
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    pygame.init()
    setting = game_setting.Setting()
    screen = pygame.display.set_mode(setting.screen_size)
    pygame.display.set_caption('飞船游戏')
    stats = GameStats(setting)
    alien = Alien(setting,screen)
    ship = Ship(setting,screen)
    aliens = Group()
    gf.creat_fleet(setting,screen,aliens,ship)
    bullets = Group()
    while True:
        gf.move_check(setting,screen,ship,bullets)
        if stats.game_active:
            ship.ship_move()
            gf.update_bullets(setting,stats,screen,ship,bullets,aliens)
            gf.update_alines(setting,aliens)
        else:
            aliens.empty()
            bullets.empty()

        gf.update_screen(setting,screen,ship,aliens,bullets)





run_game()