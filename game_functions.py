"""Module for game function"""
import pygame
import sys

from laser_class import Laser
from kryptonite import Kryptonite

def check_events(superman, screen, Settings, lasers, button, gamestats, kryptonites):
    for events in pygame.event.get():
        #Exit game
        if events.type == pygame.QUIT:
            sys.exit()

        elif events.type == pygame.KEYDOWN:
        #Keydown events
            check_keydown_events(events, superman, screen, lasers, Settings)

        elif events.type == pygame.KEYUP:
        # Keyup events
            check_keyup_events(events, superman)

        elif events.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_events(button, gamestats, Settings, kryptonites, lasers, superman)

def check_mouse_events(button, gamestats, Settings, kryptonites, lasers, superman):
    mouse_position = pygame.mouse.get_pos()

    # Setting up game when Start is clicked
    if button.rect.collidepoint(mouse_position):
        Settings.setup_dynamic_settings()
        gamestats.reset_stats()

        # empty laser and kryptonites
        kryptonites.empty()
        lasers.empty()

        # re-center superman
        superman.center_superman()

        gamestats.game_active = True

def check_keydown_events(events, superman, screen, lasers, Settings):
    # Setting movement flags
    if events.key == pygame.K_UP:
        superman.moving_up = True
    elif events.key == pygame.K_DOWN:
        superman.moving_down = True
    elif events.key == pygame.K_RIGHT:
        superman.moving_right = True
    elif events.key == pygame.K_LEFT:
        superman.moving_left = True

    # Adding laser to Group when space is pressed
    elif events.key == pygame.K_SPACE:
        if len(lasers) < 3:
            new_laser = Laser(screen, superman, Settings)
            lasers.add(new_laser)


def check_keyup_events(events, superman):
    # Setting movement flags
    if events.key == pygame.K_UP:
        superman.moving_up = False
    elif events.key == pygame.K_DOWN:
        superman.moving_down = False
    elif events.key == pygame.K_RIGHT:
        superman.moving_right = False
    elif events.key == pygame.K_LEFT:
        superman.moving_left = False

def create_kryptonite(screen, ai_settings, kryptonites):
    """create kryptonites"""
    if len(kryptonites) == 0:
        for kryptonite in range(30):
            kryptonite = Kryptonite(screen, ai_settings)
            kryptonites.add(kryptonite)

        # speed up the game
        ai_settings.increase_speed()

def update_screen(screen, game_settings, superman, lasers, kryptonites, play_button, gamestats):
    screen.fill(game_settings.background_color)
    # Show superman
    superman.blitme()

    # display and move lasers
    for laser in lasers:
        laser.update()
        laser.show_laser()


    # move and display the kryptonites
    for kryptonite in kryptonites:
        kryptonite.blitme()

    # show play button
    if not gamestats.game_active:
        play_button.display_button()

    pygame.display.flip()

def move_kryptonite(kryptonites):
    for item in kryptonites:
        item.movement()

def update_laser(lasers):
    # delete laser once it exits screen
    for laser in lasers:
        if laser.rect.left >= 1200:
            lasers.remove(laser)

def remove_and_create_kryptonite(kryptonites, lasers):
    """when kryptonite reaches the end of screen, remove it and create a new one"""
    for kryptonite in kryptonites:
        if kryptonite.rect.right <= 0:
            kryptonites.remove(kryptonite)

    check_laser_kryptonite_collision(lasers, kryptonites)

def check_laser_kryptonite_collision(lasers, kryptonites):
    """when laser collides with a kryptonite, remove it"""
    collisions = pygame.sprite.groupcollide(lasers, kryptonites, True, True)

def kryptonite_hit(kryptonites, screen, superman, gamestats, lasers):
    """whenever kryptonite hits superman or the edge"""
    if kryptonite_at_edge(kryptonites, screen) or check_superman_kryptonite_collision(superman, kryptonites):
        if gamestats.livesleft > 1:
            # remove 1 life whenever hit
            gamestats.livesleft -= 1

        else:
            # end game when all lives depleted
            gamestats.game_active = False


def check_superman_kryptonite_collision(superman, kryptonites):
    """when a kryptonite hits superman"""
    if pygame.sprite.spritecollide(superman, kryptonites, True):
        return True

def kryptonite_at_edge(kryptonites, screen):
    """when kryptonite reaches edge"""
    screen_rect = screen.get_rect()
    for kryptonite in kryptonites:
        if kryptonite.rect.left <= screen_rect.left:
            kryptonites.remove(kryptonite)
            return True


def update_kryptonite(screen, ai_settings, kryptonites, lasers, superman, gamestats):

    create_kryptonite(screen, ai_settings, kryptonites)

    move_kryptonite(kryptonites)

    remove_and_create_kryptonite(kryptonites, lasers)

    kryptonite_hit(kryptonites, screen, superman, gamestats, lasers)
