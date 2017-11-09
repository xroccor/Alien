#! /usr/bin/python
# -*- coding: utf-8 -*-
import pygame,sys
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,setting,screen,ship,bullets):
    '''按键按下的时候'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right_mark = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left_mark = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,setting,screen,ship,bullets):
    '''按键松开的时候'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right_mark = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left_mark = False

def move_check(setting,screen,ship,bullets):
    '''检测鼠标键盘事件，并作出反馈'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,setting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,setting,screen,ship,bullets)

def update_bullets(setting,stats,screen,ship,bullets,aliens):
    '''更新子弹位置，并清除飞出屏幕的子弹;如果有子弹和外星人碰撞或外星人到达低端，则清除二者'''
    bullets.update()
    check_bullet_alien_collisions(setting, screen, bullets, aliens, ship)
    check_aliens_bottom(setting, stats, screen, ship, bullets, aliens)
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(setting,stats,screen,ship,bullets,aliens)
    # print len(bullets.copy())

def ship_hit(setting,stats,screen,ship,bullets,aliens):
    '''检测飞船是否与外星人相撞'''
    if stats.ships_left > 1:
        stats.ships_left -= 1
        print stats.ships_left
        aliens.empty()
        bullets.empty()
        sleep(0.5)
    else:
        stats.game_active = False

    creat_fleet(setting,screen,aliens,ship)
    ship.center_ship()

def check_aliens_bottom(setting,stats,screen,ship,bullets,aliens):
    '''检测外星人是否到达低端'''
    for alien in aliens:
        if alien.rect.bottom >= screen.get_rect().bottom:
            ship_hit(setting,stats,screen,ship,bullets,aliens)
            break

def check_bullet_alien_collisions(setting,screen,bullets,aliens,ship):
    '''检测子弹和外星人是否碰撞，碰撞了则清除二者。若全部外星人被击杀，则生成一组新的'''
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #子弹碰到飞船
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(setting,screen,aliens,ship)

def fire_bullet(setting,screen,ship,bullets):
    '''发射子弹'''
    if len(bullets) <= setting.bullet_max - 1:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

def update_screen(setting,screen,ship,aliens,bullets):
    '''更新屏幕上的内容'''
    screen.fill(setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # aliens.draw(screen)
    for alien in aliens:
        alien.blitme()
    pygame.display.flip()

def creat_fleet(setting,screen,aliens,ship):
    '''创建外星人群'''
    alien = Alien(setting,screen)
    number_aliens_x = get_number_alien_x(setting,screen)
    number_aliens_y = get_number_alien_y(setting,screen,ship)
    for y in range(number_aliens_y):
        for x in range(number_aliens_x):
            creat_alien(x,y,setting,screen,aliens)

def get_number_alien_x(setting,screen):
    '''计算一行可以容纳多少外星人'''
    alien = Alien(setting, screen)
    # print alien.rect.width
    available_space_x = setting.screen_size[0] - 2 * alien.rect.width
    number_aliens_x = int(available_space_x / (2 * alien.rect.width))
    return number_aliens_x

def get_number_alien_y(setting,screen,ship):
    '''计算总共可以容纳多少行外星人'''
    alien = Alien(setting,screen)
    available_space_y = setting.screen_size[1] - 5 * alien.rect.height - ship.rect.height
    number_aliens_y = int(available_space_y / (2 * alien.rect.height))
    return number_aliens_y

def creat_alien(x,y,setting,screen,aliens):
    '''创建外星人'''
    alien = Alien(setting, screen)
    # for y in range(number_alien_y):
    #     for x in range(number_aliens_x+1):
    alien.rect.x = alien.rect.width + 2*alien.rect.width*x
    alien.rect.y = alien.rect.height + 2*alien.rect.width*y
    aliens.add(alien)

def update_alines(setting,aliens):
    '''使外星人群向右移动'''
    check_aliens_edges(setting,aliens)
    # aliens.update(setting)
    for a in aliens:
        a.update()

def check_aliens_edges(setting,aliens):
    '''查看是否到达边界，并改变方向'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_aliens_direction(setting,aliens)
            break

def change_aliens_direction(setting,aliens):
    '''改变飞船方向，并下移'''
    for alien in aliens.sprites():
        alien.rect.y += setting.alien_speed_drop
    setting.alien_direction *= -1
    # print setting.alien_direction
