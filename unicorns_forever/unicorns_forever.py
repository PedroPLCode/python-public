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
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Unicorns Forever")
        self.unicorn = Unicorn(self)

    def run_game(self):
        """Game main loop."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Keyboard and mouce reactions."""
        for event in pygame.event.get(): # naciśnięcie klawisza lub myszy
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
         """Updating screen view."""
         self.screen.fill(self.settings.bg_color) # kolor tła , zrobic inny
         self.unicorn.blitme()
         pygame.display.flip() # ostatni ekran

if __name__=='__main__':
    uf = UnicornsForever()
    uf.run_game()