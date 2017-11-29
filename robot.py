import rg


class Robot:
    def act(self, game):
        # If we're on a spawn square, get out
        if rg.loc_types(self.loc) != 'normal':
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]
  
        d1_us = {}
        d1_them = {}
        d2_us = {}
        d2_them = {}
        for loc, bot in game.robots.iteritems():
            if rg.wdist(self.loc, loc) == 1:
                if bot.robot_id:
                    d1_us[loc] = bot
                else:
                    d1_them[loc] = bot
            elif rg.wdist(self.loc, loc) == 2:
                if bot.robot_id:
                    d2_us[loc] = bot
                else:
                    d2_them[loc] = bot
        
        if d1_them:
            return ['attack', d1_them.keys()[0]]
        elif d2_them:
            return ['attack', rg.toward(self.loc, d2_them.keys()[0])]
  
        # move:
        # - don't move into a square an ally could move into
        # - move towards an ally
        # - move towards an enemy
  
        # suicide condition
        #allyNeighbours = 0 # work out
        #enemyNeightbours = 0
        #if self.hp < 10 and allyNeighbours == 0 and (enemyNeightbours > 1 or enemyNeightbours == 1 and their hp > 10)
        #  return ['suicide']
  
        # Default action
        #return ['guard']
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
      
