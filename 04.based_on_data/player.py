import numpy as np 
import time


from player_profile import PlayerProfile
from player_ability import PlayerAbility
from player_stat import PlayerStat
from player_form import PlayerForm



LOW_ABILITY = 20
HIGH_ABILITY = 70

def fillRandomAbility(low, high):
    t = int(time.time() % 65535)
    np.random.seed(t)
    list_rnd_technical = np.random.randint(low, high, size=14)
    list_rnd_mental = np.random.randint(low, high, size=14)
    list_rnd_physical = np.random.randint(low, high, size=8)
    list_rnd_goalkeeping = np.random.randint(low, high, size=9)
    rnd_potential = np.random.randint(low, high)


    list_rnd_ability = [ \
        list_rnd_technical, \
        list_rnd_mental, \
        list_rnd_physical, \
        list_rnd_goalkeeping, \
        rnd_potential, \
    ]
    return list_rnd_ability



class Player:
    def __init__(self, list_profile, list_ability=fillRandomAbility(LOW_ABILITY, HIGH_ABILITY), list_stat=[0,0,0,0,0,0,0,0], list_form=[0,0,0], startingLevel=1):
        self.profile = PlayerProfile(list_profile)
        self.ability = PlayerAbility(list_ability)
        self.stat = PlayerStat(list_stat)
        self.form = PlayerForm(list_form)
        self.startingLevel = startingLevel
        self.position = "FW"
