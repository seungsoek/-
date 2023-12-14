import numpy as np 
from team_stat import TeamStat
from player import Player
from match import Match

WIN = 2
DRAW = 1
LOSE = 0
HOME_GOALS_AVG = 1.53
AWAY_GOALS_AVG = 1.12
class Team:
	numPlayers = 23
	def __init__(self, name):
		self.__name = name
		# 스탯 입력
		self.__stat = TeamStat()
		self.__players = []
	def getPlayers(self):
		return self.__players
	def getTeamName(self):
		return self.__name
	def getStat(self):
		return self.__stat
	def match(self, opponent):
		home_goals = np.random.poisson(HOME_GOALS_AVG)
		away_goals = np.random.poisson(AWAY_GOALS_AVG)
		print(home_goals, away_goals)
		if home_goals > away_goals:
			res = WIN
		elif home_goals == away_goals:
			res = DRAW
		else:
			res = LOSE
		self.__stat.update(home_goals, away_goals, res)
		opponent.__stat.update(away_goals, home_goals, 2 - res)


	def prepMatch(self):
		best_eleven = self.getPlayers()[:11]
		self.__match = Match(1, best_eleven)
		return self.__match

	def getMatchObj(self):
		return self.__match 

	def addPlayer(self, playerObj):
		if len(self.__players) <= 22:
			self.__players.append(playerObj)
			return True
		else:
			return False
