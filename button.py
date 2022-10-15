"""Module for button Class"""
import pygame

class Button():
    """button class"""
    def __init__(self, screen, msg):
        """atributes of buttons"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Dimensions and colors
        self.height = 1
        self.width = 1
        self.bg_color = (255, 255, 0) # yellow
        self.txt_color = (255, 0, 0) # red


        # Rendering image
        font = pygame.font.SysFont(None, 48)
        self.msg_image = font.render(msg, True, self.txt_color, self.bg_color)

        self.rect = self.msg_image.get_rect()
        self.rect.center = self.screen_rect.center
    def display_button(self):
        """Display the button on the screen"""
        self.screen.blit(self.msg_image, self.rect)

