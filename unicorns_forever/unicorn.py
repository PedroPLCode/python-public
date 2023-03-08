import pygame

class Unicorn:
    """Unicorn managment."""

    def __init__(self, uf_game):
        """Unicorn initialization."""

        self.screen = uf_game.screen
        self.settings = uf_game.settings
        self.screen_rect = uf_game.screen.get_rect()

        self.image = pygame.image.load('/home/pedro/Dokumenty/python-public/unicorns_forever/images/unicorn.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Unicorn location updating."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.unicorn_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.unicorn_speed

        self.rect.x = self.x

    def blitme(self):
        """Shows unicorn in current location."""

        self.screen.blit(self.image, self.rect)