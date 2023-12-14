OFF_GAME = 0
ON_GAME = 1

from strategy import Formation

class Match:
	def __init__(self, gameStatus, best_eleven):
		self.__gameStatus = gameStatus
		self.__best_eleven = best_eleven

	def getGameStatus(self):
		return self.__gameStatus

	def getBestEleven(self):
		return self.__best_eleven

	def getFormationObj(self):
		return self.__formation

	def setFormation(self, numFormation):
		self.__formation = Formation(self.__best_eleven, numFormation)
