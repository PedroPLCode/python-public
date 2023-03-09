import pygame
from pygame.sprite import Sprite

class Troll(Sprite):
    """Single Troll."""

    def __init__(self, uf_game):
        """Troll initialization and location."""
        super().__init__()
        self.screen = uf_game.screen

        self.image = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/troll.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)