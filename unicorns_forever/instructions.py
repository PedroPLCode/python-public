import pygame.font

class Instructions():
    def __init__(self, uf_game, instructions_file):
        """Button initialization."""
        self.settings = uf_game.settings
        self.screen = uf_game.screen
        self.screen_rect = uf_game.screen.get_rect()

        self.width, self.height = 600, 700
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255) 
        self.font = pygame.font.SysFont(None, 22)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop

        self._prep_info(instructions_file)

    def _prep_info(self, instructions_file):
        """Instructions from txt file preparation."""
        instructions_file = self.settings.instructions_file
        with open(instructions_file) as instr_file_object:
            lines = instr_file_object.readlines()
            for n, line in enumerate(lines):
                self.instructions_image = self.font.render(line.strip(), True, self.text_color, self.button_color)
                self.instructions_image_rect = self.instructions_image.get_rect()
                self.instructions_image_rect.centerx = self.rect.centerx
                self.instructions_image_rect.centery = n*25 + 50
                self.screen.blit(self.instructions_image, self.instructions_image_rect)


    def draw_instructions(self, instructions_file):
        """Draws instructions on the screen with instructions inside."""
        self.screen.fill(self.button_color, self.rect)
        with open(instructions_file) as instr_file_object:
            lines = instr_file_object.readlines()
            for n, line in enumerate(lines):
                self.instructions_image = self.font.render(line.strip(), True, self.text_color, self.button_color)
                self.instructions_image_rect = self.instructions_image.get_rect()
                self.instructions_image_rect.centerx = self.rect.centerx
                self.instructions_image_rect.centery = n*25 + 50
                self.screen.blit(self.instructions_image, self.instructions_image_rect)
