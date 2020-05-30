'''
Created on 11/10/2019

@author: Miguel
'''

import pygame


pygame.init()
win = pygame.display.set_mode((1350,735))
In_game = True
while In_game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            In_game = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                rect_pos = e.pos
                