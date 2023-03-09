import sys
import pygame

from settings import Settings
from unicorn import Unicorn
from bullet import Bullet
from troll import Troll

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
        self.bullets = pygame.sprite.Group()
        self.trolls = pygame.sprite.Group()

        self._create_hord()

    def run_game(self):
        """Game main loop."""
        while True:
            self._check_events()
            self.unicorn.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Keyboard and mouce reactions."""
        for event in pygame.event.get(): # naciśnięcie klawisza lub myszy
            if event.type == pygame.QUIT: # teraz niepotrzebne
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
        elif event.key == pygame.K_UP:
            self.unicorn.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.unicorn.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Key up reaction."""
        if event.key == pygame.K_RIGHT:
            self.unicorn.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.unicorn.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.unicorn.moving_down = False
        elif event.key == pygame.K_UP:
            self.unicorn.moving_up = False

    def _fire_bullet(self):
        """Creating new bullet and adding to bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Bullets actualization and old bullets removing."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_hord(self):
        """Creating Trolls Hord."""
        troll = Troll(self)
        troll_width, troll_height = troll.rect.size
        available_space_x = self.settings.screen_width - (2 * troll_width)
        number_trolls_x = available_space_x // (2 * troll_width)

        unicorn_height = self.unicorn.rect.height
        available_space_y = (self.settings.screen_height - (3 * troll_height) - unicorn_height)
        number_rows = available_space_y // (2 * troll_height)

        for row_number in range(number_rows):
            for troll_number in range(number_trolls_x):
                self._create_troll(troll_number, row_number)

    def _create_troll(self, troll_number, row_number):
        """Creating troll and location in a row."""
        troll = Troll(self)
        troll_width, troll_height = troll.rect.size
        troll.x = troll_width + 2 * troll_width * troll_number
        troll.rect.x = troll.x
        troll.rect.y = troll.rect.height + 2 * troll.rect.height * row_number
        self.trolls.add(troll)

    def _update_screen(self):
        """Updating screen view."""
        self.screen.fill(self.settings.bg_color) # kolor tła , zrobic inny
        self.unicorn.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.trolls.draw(self.screen)

        pygame.display.flip() # ostatni ekran

if __name__=='__main__':
    uf = UnicornsForever()
    uf.run_game()