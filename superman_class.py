"""Module for classes"""
import pygame

class Superman():
    def __init__(self, screen, settings):
        """Initialize Superman and its starting position"""
        self.screen = screen

        # Load the superman image and its starting position and settings
        self.image = pygame.image.load('images/superman_character.bmp')
        self.image = pygame.transform.scale(self.image, (220,74))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.superman_settings = settings

        # Start each new superman at left and center of the screen
        self.center_superman()

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def movement(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y_position -= self.superman_settings.superman_speed
            self.rect.centery = self.y_position
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y_position += self.superman_settings.superman_speed
            self.rect.centery = self.y_position

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x_position += self.superman_settings.superman_speed
            self.rect.centerx = self.x_position
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x_position -= self.superman_settings.superman_speed
            self.rect.centerx = self.x_position

    def center_superman(self):
        # Start each new superman at left and center of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.x_position = float(self.rect.centerx)
        self.y_position = float(self.rect.centery)
