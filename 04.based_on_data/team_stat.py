class TeamStat:
	def __init__(self):
		self.wdl = [0, 0, 0]
		self.nGamePlayed = 0
		self.point = 0
		self.nTotalGainedGoals = 0
		self.nTotalTakenGoals = 0
		self.netGoalDiff = 0
		self.rank = 20
	def update(self, ourGoals, theirGoals, matchRes):
		self.nGamePlayed += 1
		self.nTotalGainedGoals += ourGoals
		self.nTotalTakenGoals += theirGoals
		self.netGoalDiff += (ourGoals - theirGoals)
		if matchRes == 2:
			self.wdl[0] += 1
			self.point += 3
		elif matchRes == 1:
			self.wdl[1] += 1
			self.point += 1
		else:
			self.wdl[2] += 1
			self.point += 0

	def getWDL(self):
		return self.wdl
	def getPoint(self):
		return self.point
	def getTotalGainedGoals(self):
		return self.nTotalGainedGoals
	def getTotalTakenGoals(self):
		return self.nTotalTakenGoals
	def getTotalNetGoals(self):
		return self.netGoalDiff
	def getRank(self):
		return self.rank
	def getNumPlayed(self):
		return self.nGamePlayed
	def setRank(self, r):
		self.rank = r
