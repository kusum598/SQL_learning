# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:10:32 2024

@author: kusum
"""

import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

width, height = 800, 600

# Creating pygame window
screen = pygame.display.set_mode((width, height))

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)


# Initialize pygame
pygame.init()

width, height = 800, 600

# Creating pygame window
screen = pygame.display.set_mode((width, height))

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)



# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.py.png')
pygame.display.set_icon(icon)
# Title and Icon
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.py.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
