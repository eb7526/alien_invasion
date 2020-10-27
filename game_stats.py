class GameStats:
  """Track statistics for alien invasion."""

  def __init__(self, ai_game):
    """Initialise statitics"""
    self.settings = ai_game.settings
    self.reset_stats()
    # Start alien invasion in an active state
    self.game_active = True

  def reset_stats(self):
    """Initialise statistics that can change during the game."""
    self.ships_left = self.settings.ship_limit