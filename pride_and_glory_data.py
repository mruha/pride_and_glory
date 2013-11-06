__author__ = 'mruha'

# monster data
from pride_and_glory_monster_data import *

# game data class
class pride_and_glore_game_data:

    def __init__(self, attacker, defender):
        self.fight_finished = False

        # set armies
        self.attacker_stack = self.set_monsters(attacker)

    def set_monsters(self,hero_info):

        print "hero: ", hero_info['hero name']
        print "stack monsters: ", hero_info['army']

        # monster totals

        return 0

    def update_stack(self):
        pass