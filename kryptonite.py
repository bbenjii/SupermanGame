"""Module for Kryptonite class"""
import pygame
from pygame.sprite import Sprite
from random import randint


class Kryptonite(Sprite):
    def __init__(self, screen, ai_settings):
        """Initialize Kryptonite Attributes"""
        super(Kryptonite, self).__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        # create Kryptonite rect
        self.image = pygame.image.load('images/kryptonite.bmp')
        self.rect = self.image.get_rect()

        # position kryptonite at a random location on screen
        self.rect.y = randint(0, ai_settings.screen_height)
        self.rect.centery = self.rect.y
        self.xposition = randint(ai_settings.screen_width, ai_settings.screen_width * 5)
        self.rect.centerx = self.xposition

    def movement(self):
        # move kryptonite along the screen
        self.xposition -= self.ai_settings.kryptonite_speed
        self.rect.centerx = self.xposition

    def blitme(self):
        self.screen.blit(self.image, self.rect)

