import pygame.font

class QuitButton():
    def __init__(self, uf_game, quit_msg):
        """Button initialization."""
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = 200, 55
        self.button_color = (0, 255, 0) # inne kolory
        self.text_color = (255, 255, 255) 
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = self.screen_rect.top

        self._prep_quit_msg(quit_msg)

    quit_msg = "Quit"

    def _prep_quit_msg(self, quit_msg):
        """Message into the button."""
        self.quit_msg_image = self.font.render(quit_msg, True, self.text_color, self.button_color)
        self.quit_msg_image_rect = self.quit_msg_image.get_rect()
        self.quit_msg_image_rect.center = self.rect.center

    def draw_quit_button(self):
        """Draws a button with message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.quit_msg_image, self.quit_msg_image_rect)