import pygame
from pygame.sprite import Sprite

class Troll(Sprite):
    """Single Troll."""

    def __init__(self, uf_game):
        """Troll initialization and location."""
        super().__init__()
        self.screen = uf_game.screen
        self.settings = uf_game.settings

        self.image = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/troll.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def update(self):
        """Troll moving left or right."""
        self.x += (self.settings.troll_speed * self.settings.hord_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if Troll on edge."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)