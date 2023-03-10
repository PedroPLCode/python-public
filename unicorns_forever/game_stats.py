class GameStats:
    """Statistic data in game."""

    def __init__(self, uf_game):
        """Statistic data initialization."""
        self.settings = uf_game.settings
        self._reset_stats()
        self.game_active = False
        self.high_score = 0

    def _reset_stats(self):
        """Reset of statistic data."""
        self.unicorn_left = self.settings.unicorns_limit
        self.score = 0
        self.level = 1