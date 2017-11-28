import rg
class Robot:
  def act(self, game):
    if rg.loc_types(self.loc) != 'normal':
      return ['move', rg.toward(self.location, rg.CENTER_POINT)]

    # if there are enemies around, attack them
    allies = []
    enemies = []
    for loc, bot in game.robots.iteritems():
      if bot.player_id != self.player_id:
        if bot.robot_id:
          allies.append(bot.location)
        else:
          enemies.append(bot.location)
  

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]