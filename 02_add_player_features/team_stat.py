class TeamStat:
	def __init__(self):
		self.__wdl = [0, 0, 0]
		self.__nGamePlayed = 0
		self.__point = 0
		self.__nTotalGainedGoals = 0
		self.__nTotalTakenGoals = 0
		self.__netGoalDiff = 0
		self.__rank = 20
	def update(self, ourGoals, theirGoals, matchRes):
		self.__nGamePlayed += 1
		self.__nTotalGainedGoals += ourGoals
		self.__nTotalTakenGoals += theirGoals
		self.__netGoalDiff += (ourGoals - theirGoals)
		if matchRes == 2:
			self.__wdl[0] += 1
			self.__point += 3
		elif matchRes == 1:
			self.__wdl[1] += 1
			self.__point += 1
		else:
			self.__wdl[2] += 1
			self.__point += 0

	def getWDL(self):
		return self.__wdl
	def getPoint(self):
		return self.__point
	def getTotalGainedGoals(self):
		return self.__nTotalGainedGoals
	def getTotalTakenGoals(self):
		return self.__nTotalTakenGoals
	def getTotalNetGoals(self):
		return self.__netGoalDiff
	def getRank(self):
		return self.__rank
	def getNumPlayed(self):
		return self.__nGamePlayed
	def setRank(self, r):
		self.__rank = r
