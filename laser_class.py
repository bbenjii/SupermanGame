"""Module for the Lasers class"""
import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """Class for Lasers shot"""
    def __init__(self, screen, superman, Settings):
        """Initialize laser attributes"""
        super().__init__()

        self.screen = screen
        self.laser_speed = Settings.laser_speed

        # load image and create laser rect
        self.laser_image = pygame.image.load("images/laser.bmp")
        self.laser_image = pygame.transform.scale(self.laser_image, (56, 56))
        self.rect = self.laser_image.get_rect()

        # position laser rect
        self.rect.centery = superman.rect.centery + -15
        self.rect.centerx = superman.rect.centerx + 75

        self.position = float(self.rect.centerx)

    def update(self):
        # move laser along the screen
        self.position += self.laser_speed
        self.rect.centerx = self.position

    def show_laser(self):
        # display the laser
        self.screen.blit(self.laser_image, self.rect)



