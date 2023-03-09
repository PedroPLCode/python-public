class GameStats:
    """Statistic data in game."""

    def __init__(self, uf_game):
        """Statistic data initialization."""
        self.settings = uf_game.settings
        self._reset_stats()
        self.game_active = True

    def _reset_stats(self):
        """Reset of statistic data."""
        self.unicorn_left = self.settings.unicorns_limit