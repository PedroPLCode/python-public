import pygame

class Unicorn:
    """Unicorn managment."""

    def __init__(self, uf_game):
        """Unicorn initialization."""

        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.image = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/unicorn.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Shows unicorn in current location."""

        self.screen.blit(self.image, self.rect)