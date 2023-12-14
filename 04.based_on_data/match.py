OFF_GAME = 0
ON_GAME = 1

import numpy as np
from strategy import Formation
import random
import math
class Match:
	def __init__(self, gameStatus, homeTeam, awayTeam):
		self.gameStatus = gameStatus
		self.homeTeam = homeTeam
		self.awayTeam = awayTeam
		self.best_eleven = best_eleven
		self.isHomeTeam = isHomeTeam
		self.ball_pos = [100, 50]
		self.dribbler = ""
		self.passer = ""
		self.passed = False
		self.passDest = [0,0]
		self.receiver = ""
		self.chase = True
	def getGameStatus(self):
		return self.gameStatus

	def getBestEleven(self):
		return self.best_eleven

	def getFormationObj(self):
		return self.formation

	def setFormation(self, numFormation):
		self.formation = Formation(self.best_eleven, numFormation, self.isHomeTeam)
		self.best_eleven = self.formation.eleven
		# print(self.best_eleven.items())

	def chaseBall(self):
		for key, player in self.best_eleven.items():
			if player['possession'] == False and \
				self.chase and \
				key != self.passer and \
					key != self.receiver:
				player_pos = player['Pos']
				xdiff = self.ball_pos[0] - player_pos[0] 
				ydiff = self.ball_pos[1] - player_pos[1] 
				dist = math.sqrt(xdiff ** 2 + ydiff ** 2)

				if dist < 0.6:
					self.dribbler = key
					self.best_eleven[self.dribbler]['possession'] = True
					print(self.dribbler + " possed the ball")
					# self.chase = False
				elif dist < 30:
					print(key, "chase the ball")
					x_or_y = random.randint(0,1)
					if x_or_y == 0:
						self.best_eleven[key]['Pos'][x_or_y] += np.sign(xdiff)
					else:
						self.best_eleven[key]['Pos'][x_or_y] += np.sign(ydiff)
							

	def dribble(self):
		if self.passed == False and \
			 self.dribbler != "" and \
				 self.dribbler != self.passer: 
			# print(self.dribbler + " trying to dribble")
			if self.best_eleven[self.dribbler]['possession'] == True:
				# print(self.dribbler + " trying to dribble")
				x_or_y = random.randint(0,1)
				f_or_b = 1
				if random.randint(0,1) == 0:
					f_or_b = 1
				else:
					f_or_b = -1
				dribbler_x = self.best_eleven[self.dribbler]['Pos'][0]
				dribbler_y = self.best_eleven[self.dribbler]['Pos'][1]
				self.best_eleven[self.dribbler]['Pos'][x_or_y] += f_or_b
				self.ball_pos = [dribbler_x, dribbler_y]
				print(self.dribbler + " dribbles")
				if random.randint(0,100) > 95:
					self.passer = str(self.dribbler)
					self.best_eleven[self.dribbler]['possession'] = False
					self.dribbler =""
					self.passed = False
					
					

	def ballPass(self):
		ok_to_pass = False
		if self.passer !="" and self.passed == False:
			print(self.passer, "trying to pass the ball")
			print("passing status: ", self.passed)
			while True: 
				self.receiver = random.choice(list(self.best_eleven.keys()))
				print("receiver is ", self.receiver)
				if self.receiver != self.passer:
					ok_to_pass = True
					break
			if ok_to_pass:
				print(self.passer, "pass the ball to ",self.receiver)
				recv_x = self.best_eleven[self.receiver]['Pos'][0]
				recv_y = self.best_eleven[self.receiver]['Pos'][1] 
				self.passDest = [recv_x,recv_y]
				self.best_eleven[self.passer]['possession'] = False
				self.passed = True
	def ballMove(self):
		if self.passer !="" and self.passed == True:
			diff = [0,0]
			print(self.passDest)
			print("ball move dest:", self.passDest[0], self.passDest[1])
			xdiff = (self.passDest[0] - self.ball_pos[0])
			ydiff = (self.passDest[1] - self.ball_pos[1])
			
			dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
			cos_theta = abs(xdiff) / dist
			sin_theta = abs(ydiff) / dist
			# print("distance: ", dist)
			if dist > 0.6:
				self.ball_pos[0] += np.sign(xdiff) * cos_theta
				self.ball_pos[1] += np.sign(ydiff) * sin_theta
			else:
				self.passed = False
				self.dribbler = str(self.receiver)
				self.best_eleven[self.dribbler]['possession'] = True
				self.passer=""
				print(self.dribbler, " received the ball")
