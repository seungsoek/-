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
        self.__profile = PlayerProfile(list_profile)
        self.__ability = PlayerAbility(list_ability)
        self.__stat = PlayerStat(list_stat)
        self.__form = PlayerForm(list_form)
        self.__startingLevel = startingLevel


    def getProfileObj(self):
        return self.__profile
    def getAbilityObj(self):
        return self.__ability
    def getStatObj(self):
        return self.__stat
    def getFormObj(self):
        return self.__form
    def getStartingLevel(self):
        return self.__startingLevel
