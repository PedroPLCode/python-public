import pygame.font

class HelpButton():
    def __init__(self, uf_game, help_msg):
        """Button initialization."""
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = 200, 55
        self.button_color = (0, 255, 0) # inne kolory
        self.text_color = (255, 255, 255) 
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = self.screen_rect.topleft

        self._prep_help_msg(help_msg)

    help_msg = "Help"

    def _prep_help_msg(self, help_msg):
        """Message into the button."""
        self.help_msg_image = self.font.render(help_msg, True, self.text_color, self.button_color)
        self.help_msg_image_rect = self.help_msg_image.get_rect()
        self.help_msg_image_rect.center = self.rect.center

    def draw_help_button(self):
        """Draws a button with message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.help_msg_image, self.help_msg_image_rect)

    