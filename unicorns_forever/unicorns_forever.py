import sys
import pygame

from settings import Settings
from unicorn import Unicorn

class UnicornsForever:
    """Main class for game menagment."""

    def __init__(self):
        """Game initialization."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Unicorns Forever")
        self.unicorn = Unicorn(self)

    def run_game(self):
        """Game main loop."""
        while True:
            self._check_events()
            self.unicorn.update()
            self._update_screen()

    def _check_events(self):
        """Keyboard and mouce reactions."""
        for event in pygame.event.get(): # naciśnięcie klawisza lub myszy
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)     

    def _check_keydown_events(self, event):
        """Key down reaction."""
        if event.key == pygame.K_RIGHT:
            self.unicorn.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.unicorn.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Key up reaction."""
        if event.key == pygame.K_RIGHT:
            self.unicorn.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.unicorn.moving_left = False


    def _update_screen(self):
        """Updating screen view."""
        self.screen.fill(self.settings.bg_color) # kolor tła , zrobic inny
        self.unicorn.blitme()
        pygame.display.flip() # ostatni ekran

if __name__=='__main__':
    uf = UnicornsForever()
    uf.run_game()