import pygame
from pygame.sprite import Sprite

class Unicorn(Sprite):
    """Unicorn managment."""

    def __init__(self, uf_game):
        """Unicorn initialization."""
        super().__init__()

        self.screen = uf_game.screen
        self.settings = uf_game.settings
        self.screen_rect = uf_game.screen.get_rect()

        self.image_up = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/unicornUP.bmp')
        self.imageup_down = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/unicornDOWN.bmp')
        self.imageup_left = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/unicornL.bmp')
        self.image_right = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/unicornR.bmp')
        self.image = self.image_up
        
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Unicorn location updating."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.unicorn_speed_left_right
            self.image = self.image_right
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.unicorn_speed_left_right
            self.image = self.imageup_left
        if self.moving_up: # and self.rect.top < self.screen_rect.top:
            self.rect.y -= self.settings.unicorn_speed_up_down
            self.image = self.image_up
        if self.moving_down: # and self.rect.bottom > 0:
            self.rect.y += self.settings.unicorn_speed_up_down
            self.image = self.imageup_down

        self.rect_x = self.x
        self.rect_y = self.y

    def blitme(self):
        """Shows unicorn in current location."""

        self.screen.blit(self.image, self.rect)

    def center_unicorn(self):
        """New unicorn in the center bottom of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)