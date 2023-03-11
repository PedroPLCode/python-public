import pygame.font

class Instructions():
    def __init__(self, uf_game, instructions_file):
        """Button initialization."""
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = 800, 400
        self.button_color = (0, 255, 0) # inne kolory
        self.text_color = (255, 255, 255) 
        self.font = pygame.font.SysFont(None, 22)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        instructions_file = 'readme.txt'
        self._prep_info(instructions_file)

    def _prep_info(self, instructions_file):
        """Instructions from txt file preparation."""
        with open(instructions_file) as instr_file_object:
            lines = instr_file_object.readlines()
            for n, line in enumerate(lines):
                self.instructions_image = self.font.render(line, True, self.text_color, self.button_color)
                self.instructions_image_rect = self.instructions_image.get_rect()
                self.instructions_image_rect.centerx = self.rect.centerx
                self.instructions_image_rect.centery = n*25 + 50


    def draw_instructions(self):
        """Draws instructions on the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.instructions_image, self.instructions_image_rect)