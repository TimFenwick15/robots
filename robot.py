import rg
class Robot:
  def getNeighbourSquares(loc):
    return [
      (loc[0], loc[1]),

    ]
  def act(self, game):
    # If we're on a spawn square, get out
    if rg.loc_types(self.loc) != 'normal':
      return ['move', rg.toward(self.location, rg.CENTER_POINT)]

    # get list of allies and enemies
    allies = []
    enemies = []
    for loc, bot in game.robots.iteritems():
      if bot.player_id != self.player_id:
        if bot.robot_id:
          allies.append(bot.location)
        else:
          enemies.append(bot.location)

    # suicide condition
    allyNeighbours = 0 # work out
    enemyNeightbours = 0
    if self.hp < 10 && allyNeighbours == 0 && (enemyNeightbours > 1 || enemyNeightbours == 1 && their hp > 10)
      return ['suicide']

    # attack near by enemies
    for loc, bot in game.robots.iteritems():
      if bot.player_id != self.player_id:
        if rg.dist(loc, self.location) <= 1:
          return ['attack', loc]

    # move:
    # - don't move into a square an ally could move into
    # - move towards an ally
    # - move towards an enemy

    # guard
  