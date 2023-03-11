import pygame.font

class HelpButton():
    def __init__(self, uf_game, help_msg):
        """Button initialization."""
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_help_msg(help_msg)

    help_msg = ("Unicorn Forever Game\n\n"
               "arrows up, down, left and right - moving unicorn\n\n"
               "space - shooting normal bullets.\n"
               "max 3 bullets allowed at one time on the screen.\n"
               "bullets unlimited.\n\n"
               "b - bomb - super bullet.\n"
               "max 1 bomb allowed at one time on the screen.\n"
               "you have one bomb at the beginning. every level gives you an extra bomb.")

    def _prep_help_msg(self, help_msg):
        """Message into the button."""
        self.help_msg_image = self.font.render(help_msg, True, self.text_color, self.button_color)
        self.help_msg_image_rect = self.msg_image.get_rect()
        self.help_msg_image_rect.center = self.rect.center

    def draw_help_button(self):
        """Draws a button with message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.help_msg_image, self.help_msg_image_rect)
        