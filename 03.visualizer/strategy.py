from player import Player 

class Formation:
	def __init__(self, eleven, formationType):
		self.__eleven = eleven
		self.__formationType = formationType
		if formationType == 442:
			self.setFormation()

	
	def getFormation(self):
		return self.__formation
	def getFormationType(self):
		return self.__formationType
	def setFormation(self):
		self.setPlayerPosition(0, ["GK", [0,50]])
		self.setPlayerPosition(1, ["LB", [30,10]])
		self.setPlayerPosition(2, ["LCB", [30,37]])
		self.setPlayerPosition(3, ["RCB", [30,64]])
		self.setPlayerPosition(4, ["RB", [30,90]])
		self.setPlayerPosition(5, ["LM", [60,10]])
		self.setPlayerPosition(6, ["LCM", [60,37]])
		self.setPlayerPosition(7, ["RCM", [60,64]])
		self.setPlayerPosition(8, ["RM", [60,90]])
		self.setPlayerPosition(9, ["LF", [90,40]])
		self.setPlayerPosition(10, ["RF", [90,60]])

	def setPlayerPosition(self, num, position):
		self.__eleven[num].setPosition(position)

	def getBestEleven(self):
		return self.__eleven
