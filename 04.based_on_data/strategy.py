from player import Player 
import random

class Formation:
	def __init__(self, players, formationType, isHome):
		self.players = players
		self.formationType = formationType
		self.isHome = isHome
		self.best = {}
		self.sub = {}
		self.reserve = {}
		self.setFormation()
	def bestEleven(self):
		best_names = random.sample(list(self.players.keys()), 11)
		for i in range(11):
			self.best[best_names[i]] = self.players[best_names[i]]
	def setFormation(self):
		i = 1
		for key, val in self.best.items():
			if self.isHome:
				if i == 1:
					self.best[key]['Pos'] = [10,50]
					self.best[key]['possession']= False
				elif i == 2:
					self.best[key]['Pos'] = [30,20]	
					self.best[key]['possession']= False
				elif i == 3:
					self.best[key]['Pos'] = [30,40]	
					self.best[key]['possession']= False
				elif i == 4:
					self.best[key]['Pos'] = [30,60]	
					self.best[key]['possession']= False
				elif i == 5:
					self.best[key]['Pos'] = [30,80]	
					self.best[key]['possession']= False
				elif i == 6:
					self.best[key]['Pos'] = [60,20]	
					self.best[key]['possession']= False
				elif i == 7:
					self.best[key]['Pos'] = [60,40]	
					self.best[key]['possession']= False
				elif i == 8:
					self.best[key]['Pos'] = [60,60]	
					self.best[key]['possession']= False
				elif i == 9:
					self.best[key]['Pos'] = [60,80]	
					self.best[key]['possession']= False
				elif i == 10:
					self.best[key]['Pos'] = [90,40]	
					self.best[key]['possession']= False
				elif i == 11:
					self.best[key]['Pos'] = [90,60]	
					self.best[key]['possession']= False
			else:
				if i == 1:
					self.best[key]['Pos'] = [200-10,50]
					self.best[key]['possession']= False
				elif i == 2:
					self.best[key]['Pos'] = [200-30,20]	
					self.best[key]['possession']= False
				elif i == 3:
					self.best[key]['Pos'] = [200-30,40]	
					self.best[key]['possession']= False
				elif i == 4:
					self.best[key]['Pos'] = [200-30,60]	
					self.best[key]['possession']= False
				elif i == 5:
					self.best[key]['Pos'] = [200-30,80]	
					self.best[key]['possession']= False
				elif i == 6:
					self.best[key]['Pos'] = [200-60,20]	
					self.best[key]['possession']= False
				elif i == 7:
					self.best[key]['Pos'] = [200-60,40]	
					self.best[key]['possession']= False
				elif i == 8:
					self.best[key]['Pos'] = [200-60,60]	
					self.best[key]['possession']= False
				elif i == 9:
					self.best[key]['Pos'] = [200-60,80]	
					self.best[key]['possession']= False
				elif i == 10:
					self.best[key]['Pos'] = [200-90,40]	
					self.best[key]['possession']= False
				elif i == 11:
					self.best[key]['Pos'] = [200-90,60]	
					self.best[key]['possession']= False
			i += 1
				


class Strategy:
	def __init__(self, formation):
		self.formation = formation
