import itertools
import random
import numpy as np 

class League:
	def __init__(self, teams):
		self.currRound = 0
		self.teams = teams
		self.numTeams = len(self.teams)
		self.totalRound = self.numTeams
		self.teamNames = {}
		self.pointTable = np.array(list([int]*self.numTeams))
		self.schedule = [] * self.numTeams * (self.numTeams - 1)

	def begin(self):
		for i, team in enumerate(self.teams):
			self.teamNames[team.getTeamName()] = i
		perm = itertools.permutations(self.teamNames, 2)
		perm = list(perm)
		n = len(perm)
		half = n // 2
		perm1 = perm[:half]
		perm2 = perm[half:]
		random.shuffle(perm1)
		random.shuffle(perm2)
		perm = perm1 + perm2
		self.schedule = list(perm)

	def nextMatch(self, home_team, away_team):
		homeTeam.prepMatch(True)
		awayTeam.prepMatch(False)
		self.curr_match = Match(home_team, away_team)
		self.curr_match.play()


	def nextRound(self):
		self.currRound += 1
		for i in range(self.numTeams - 1):
			match = self.schedule.pop(0)
			home_team = match[0]
			away_team = match[1]
			self.teams[self.teamNames[home_team]].match(self.teams[self.teamNames[away_team]])

		for i in range(self.numTeams):
			self.pointTable[i] = self.teams[i].getStat().getPoint()

		d = {n:i for i, n in list(enumerate(sorted(set(self.pointTable), reverse=True), 1))}
		rank = []
		for pt in self.pointTable:
			rank.append(d[pt])

		# print(rank)

		for i in range(self.numTeams):
			self.teams[i].getStat().setRank(rank[i])


		self.teams.sort(key=lambda x:x.getStat().getRank())



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
		for i in range(self.numTeams):
			st = self.teams[i].getStat()
			print(f'{st.getRank():>5d}', end='\t')
			print(f'{self.teams[i].getTeamName():>15}', end='\t')
			print(f'{st.getWDL()[0]:>5d}', end='\t')
			print(f'{st.getWDL()[1]:>5d}', end='\t')
			print(f'{st.getWDL()[2]:>5d}', end='\t')
			print(f'{st.getTotalGainedGoals():>4d}', end='\t')
			print(f'{st.getTotalTakenGoals():>4d}', end='\t')
			print(f'{st.getTotalNetGoals():>4d}', end='\t')
			print(f'{st.getNumPlayed():>4d}', end='\t')
			print(f'{st.getPoint():>4d}')


	def getCurrRound(self):
		return self.currRound
	def getSchedule(self):
		return self.schedule
	def getTotalRound(self):
		return self.totalRound
