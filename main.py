"""Main program for the Superman Game"""
import sys
import pygame
from pygame.sprite import Group

from superman_class import Superman
import game_functions as gf
from settings import Settings
from kryptonite import Kryptonite
from gamestats import Gamestats
from button import Button
from random import randint



def run_game():
    pygame.init()
    pygame.display.set_caption("Superman Game")

    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.screen_dimensions)

    # Create button
    play_button = Button(screen, "Start")

    # Create Superman
    superman = Superman(screen, game_settings)

    # Create Laser group
    lasers = Group()

    # create kryptonite group
    kryptonites = Group()

    #game stats
    gamestats = Gamestats(game_settings)

    while True:
        gf.check_events(superman, screen, game_settings, lasers, play_button, gamestats, kryptonites)
        pygame.mouse.set_visible(True)

        if gamestats.game_active:
            pygame.mouse.set_visible(False)
            superman.movement()
            gf.update_laser(lasers)
            gf.update_kryptonite(screen, game_settings, kryptonites, lasers, superman, gamestats)
        gf.update_screen(screen, game_settings, superman, lasers, kryptonites, play_button, gamestats)


run_game()