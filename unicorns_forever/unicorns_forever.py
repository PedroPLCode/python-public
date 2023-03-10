import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from unicorn import Unicorn
from bullet import Bullet
from bomb import Bomb
from troll import Troll
from button import Button
from scoreboard import ScoreBoard

class UnicornsForever:
    """Main class for game menagment."""

    def __init__(self):
        """Game initialization."""
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Unicorns Forever")

        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)
        
        self.unicorn = Unicorn(self)
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.trolls = pygame.sprite.Group()

        self._create_hord()

        self.game_active = False
        self.play_button = Button(self, msg="Play") # info


    def run_game(self):
        """Game main loop."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.unicorn.update()
                self._update_bullets()
                self._update_bombs()
                self._update_trolls()
            self._update_screen()

    def _check_events(self):
        """Keyboard and mouce reactions."""
        for event in pygame.event.get(): # naciśnięcie klawisza lub myszy
            if event.type == pygame.QUIT: # teraz niepotrzebne
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  

    def _check_g_key(self):
        """New game starts after key G press"""
        if True and not self.stats.game_active:
            self.start_new_round()

    def _check_play_button(self, mouse_pos):
        """New game starts after Play button."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.start_new_round()

    def start_new_round(self):
            """Starting new round."""
            self.settings.initialize_dynamic_settings()
            self.stats._reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_unicorns()

            self.trolls.empty()
            self.bullets.empty()

            self._create_hord()
            self.unicorn.center_unicorn()  

            pygame.mouse.set_visible(False) 

    def _check_keydown_events(self, event):
        """Key down reaction."""
        if event.key == pygame.K_g:
            self._check_g_key()
        elif event.key == pygame.K_RIGHT:
            self.unicorn.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.unicorn.moving_left = True
        elif event.key == pygame.K_UP:
            self.unicorn.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.unicorn.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_b:
            self._fire_bomb()
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

    def _fire_bomb(self):
        """Creating new Bomb and adding to bombs group."""
        if len(self.bombs) < self.settings.bombs_allowed and self.settings.bombs_fired < self.settings.bombs_limit:
            new_bomb = Bomb(self)
            self.bombs.add(new_bomb)
            self.settings.bombs_fired += 1


    def _update_bullets(self):
        """Bullets actualization and old bullets removing."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_troll_colisions()

    def _update_bombs(self):
        """Bombs actualization and old bombs removing."""
        self.bombs.update()

        for bomb in self.bombs.copy():
            if bomb.rect.bottom <= 0:
                self.bombs.remove(bomb)

        self._check_bombs_troll_colisions()

    def _check_bullet_troll_colisions(self):
        """Reaction for collision of bullet and troll."""
        colisions = pygame.sprite.groupcollide(self.bullets, self.trolls, True, True)

        if colisions:
            for trolls in colisions.values():
                self.stats.score += self.settings.troll_points * len(trolls)
            self.sb.prep_score()
            self.sb.check_high_score()

        self.next_level()

    def _check_bombs_troll_colisions(self):
        """Reaction for collision of bomb and troll."""
        bomb_colisions = pygame.sprite.groupcollide(self.bombs, self.trolls, True, True)

        if bomb_colisions:
            for trolls in bomb_colisions.values():
                self.stats.score += self.settings.troll_points * len(trolls)
            self.sb.prep_score()
            self.sb.check_high_score()

        self.next_level()

    def next_level(self):
        """Next level."""
        if not self.trolls:
            self.bullets.empty()
            self.bombs.empty()
            self._create_hord()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _update_trolls(self):
        """Checking if hord is on the edge and location of all trolls actualization."""
        self._check_hord_egdes()
        self.trolls.update()
        if pygame.sprite.spritecollideany(self.unicorn, self.trolls):
            self._unicorn_hit()
        self._check_trolls_bottom()

    def _check_hord_egdes(self):
        """Reaction for Troll on the screen edge."""
        for troll in self.trolls.sprites():
            if troll.check_edges():
                self._change_hord_direction()
                break

    def _change_hord_direction(self):
        """Hord moving down and charne direction."""
        for troll in self.trolls.sprites():
            troll.rect.y += self.settings.hord_drop_speed
        self.settings.hord_direction *= -1

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

    def _unicorn_hit(self):
        """Unicorn hit by Troll reaction."""

        if self.stats.unicorns_left > 0:

            self.stats.unicorns_left -= 1

            self.sb.prep_unicorns()

            self.trolls.empty()
            self.bullets.empty()
            self.bombs.empty()

            self._create_hord()
            self.unicorn.center_unicorn()

            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_trolls_bottom(self):
        """checking if any Troll gets to the bottonm of the screen."""
        screen_rect = self.screen.get_rect()
        for troll in self.trolls.sprites():
            if troll.rect.bottom >= screen_rect.bottom:
                self._unicorn_hit()
                break

    def _update_screen(self):
        """Updating screen view."""
        self.screen.fill(self.settings.bg_color) # kolor tła , zrobic inny
        self.unicorn.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for bomb in self.bombs.sprites():
            bomb.draw_bomb()
        
        self.trolls.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip() # ostatni ekran

if __name__=='__main__':
    uf = UnicornsForever()
    uf.run_game()