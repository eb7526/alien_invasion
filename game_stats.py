import json
import scoreboard as sb

class GameStats:
  """Track statistics for alien invasion."""

  def __init__(self, ai_game):
    """Initialise statitics"""
    self.settings = ai_game.settings
    self.reset_stats()
    # Start alien invasion in an inactive state
    self.game_active = False
    self.retrieve_high_score()
    self.high_score = self.all_time_high_score

  def reset_stats(self):
    """Initialise statistics that can change during the game."""
    self.ships_left = self.settings.ship_limit
    self.score = 0
    self.level = 1# High score should never be reset

  def retrieve_high_score(self):
    try:  
        with open('high_score.json', 'r') as f:
            self.all_time_high_score = json.load(f)
    except FileNotFoundError:
        self.all_time_high_score = 0
