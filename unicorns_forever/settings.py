class Settings:
    """Storing all settings used in game."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.unicorns_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        self.troll_bullet_width = 10
        self.troll_bullet_height = 30
        self.troll_bullet_color = (90, 160, 100)

        self.bomb_width = 20
        self.bomb_height = 20
        self.bomb_color = (60, 60, 60)
        self.bombs_allowed = 1
        self.bombs_limit = 1

        self.hord_drop_speed = 10
        self.trolls_starts_shoot = 20

        self.speed_up_scale = 1.1
        self.score_scale = 1.5
        self.new_bombs = 1

        self.filename = 'unicorns_forever/high_score.json'
        self.instructions_file = 'unicorns_forever/readme.txt'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """settings initialization."""
        self.unicorn_speed_left_right = 1
        self.unicorn_speed_up_down = 1
        self.bullet_speed = 3.0
        self.troll_bullet_speed = 1.0
        self.bomb_speed = 1.5
        self.troll_speed = 1.0

        self.troll_points = 50

        self.hord_direction = 1

        self.bombs_fired = 0

    def increase_speed(self):
        """change speed settings."""
        self.unicorn_speed_left_right *= self.speed_up_scale
        self.unicorn_speed_up_down *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.bomb_speed *= self.speed_up_scale
        self.troll_speed *= self.speed_up_scale
        self.troll_bullet_speed *= self.speed_up_scale
        self.troll_points = int(self.troll_points * self.score_scale)
        self.bombs_limit += self.new_bombs