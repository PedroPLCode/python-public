import pygame
from pygame.sprite import Sprite

class TrollBullet(Sprite):
    """Troll bullets management."""

    def __init__(self, uf_game):
        """Create bullet in current Troll position."""

        super().__init__()
        self.screen = uf_game.screen
        self.settings = uf_game.settings
        self.color = self.settings.troll_bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.troll_bullet_width, self.settings.troll_bullet_height)
        #for troll in uf_game.trolls.sprites():
        for troll in uf_game.trolls:
            self.rect.midtop = troll.rect.midbottom
            self.y = float(self.rect.y)


    def update(self):
        """Trolls bullet moving down."""

        self.y += self.settings.troll_bullet_speed
        self.rect.y = self.y

    def draw_troll_bullet(self):
        """Shows troll bullet."""

        pygame.draw.ellipse(self.screen, self.color, self.rect)