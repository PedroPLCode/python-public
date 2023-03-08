class Settings:
    """Storing all settings used in game."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.unicorn_speed_left_right = 1.5
        self.unicorn_speed_up_down = 1

        self.bullet_speed = 1
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5