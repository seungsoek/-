import itertools
import random
import numpy as np 

class League:
	def __init__(self, allTeams):
		self.__currRound = 0
		self.__allTeams = allTeams
		self.__numTeams = len(self.__allTeams)
		self.__totalRound = self.__numTeams
		self.__teamNames = {}
		self.__pointTable = np.array(list([int]*self.__numTeams))
		self.__schedule = [] * self.__numTeams * (self.__numTeams - 1)

	def begin(self):
		for i, team in enumerate(self.__allTeams):
			self.__teamNames[team.getTeamName()] = i
		perm = itertools.permutations(self.__teamNames, 2)
		perm = list(perm)
		n = len(perm)
		half = n // 2
		perm1 = perm[:half]
		perm2 = perm[half:]
		random.shuffle(perm1)
		random.shuffle(perm2)
		perm = perm1 + perm2
		self.__schedule = list(perm)

	def nextRound(self):
		self.__currRound += 1
		for i in range(self.__numTeams - 1):
			match = self.__schedule.pop(0)
			home_team = match[0]
			away_team = match[1]
			self.__allTeams[self.__teamNames[home_team]].match(self.__allTeams[self.__teamNames[away_team]])

		for i in range(self.__numTeams):
			self.__pointTable[i] = self.__allTeams[i].getStat().getPoint()

		d = {n:i for i, n in list(enumerate(sorted(set(self.__pointTable), reverse=True), 1))}
		rank = []
		for pt in self.__pointTable:
			rank.append(d[pt])

		# print(rank)

		for i in range(self.__numTeams):
			self.__allTeams[i].getStat().setRank(rank[i])


		self.__allTeams.sort(key=lambda x:x.getStat().getRank())



	def showTable(self):
		print()
		print("===================================================================================================")
		print("       프리미어리그 {}번째 라운드".format(self.getCurrRound()))
		print("===================================================================================================")
		print(f'{"순위":>5}', end="\t")
		print(f'{"팀명":>15}', end="\t")
		print(f'{"승":>5}', end="\t")
		print(f'{"무":>5}', end="\t")
		print(f'{"패":>5}', end="\t")
		print(f'{"총득점":>4}', end="\t")
		print(f'{"총실점":>4}', end="\t")
		print(f'{"골득실":>4}', end="\t")
		print(f'{"경기수":>4}', end="\t")
		print(f'{"승점":>4}')
		for i in range(self.__numTeams):
			st = self.__allTeams[i].getStat()
			print(f'{st.getRank():>5d}', end='\t')
			print(f'{self.__allTeams[i].getTeamName():>15}', end='\t')
			print(f'{st.getWDL()[0]:>5d}', end='\t')
			print(f'{st.getWDL()[1]:>5d}', end='\t')
			print(f'{st.getWDL()[2]:>5d}', end='\t')
			print(f'{st.getTotalGainedGoals():>4d}', end='\t')
			print(f'{st.getTotalTakenGoals():>4d}', end='\t')
			print(f'{st.getTotalNetGoals():>4d}', end='\t')
			print(f'{st.getNumPlayed():>4d}', end='\t')
			print(f'{st.getPoint():>4d}')


	def getCurrRound(self):
		return self.__currRound
	def getSchedule(self):
		return self.__schedule
	def getTotalRound(self):
		return self.__totalRound
