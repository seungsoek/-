import numpy as np 
from team_stat import TeamStat
from player import Player
from strategy import *
import random

WIN = 2
DRAW = 1
LOSE = 0
HOME_GOALS_AVG = 1.53
AWAY_GOALS_AVG = 1.12
class Team:
	numPlayers = 23
	def __init__(self, name):
		self.name = name
		# 스탯 입력
		self.stat = TeamStat()
		self.players = {}
		self.match = []
	def getPlayers(self):
		return self.players
	def getTeamName(self):
		return self.name
	def getStat(self):
		return self.stat
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
		self.stat.update(home_goals, away_goals, res)
		opponent.__stat.update(away_goals, home_goals, 2 - res)


	def prepMatch(self, isHome):
		formation = Formation(self.players, 442, isHome)
		self.strategy = Strategy(formation)
		
		

	def getMatchObj(self):
		return self.match 

	def addPlayer(self, playerObj):
		# print(playerObj)
		if len(self.players) <= 22:
			self.players[playerObj['full_name']] = playerObj
			return True
		else:
			return False
