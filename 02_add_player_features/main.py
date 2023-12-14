from team import Team
from team_stat import TeamStat
from league import League
from player import Player

team_names = ["리버풀", "맨시티", "레스터시티", "첼시", "맨유", "울버햄튼", "쉐필드", "아스날", "토트넘", "번리", "에버튼", "크리스탈팰리스", "뉴캐슬", "사우스햄튼", "브라이튼", "웨스트햄", "왓포드", "아스톤빌라", "본머스", "노르위치시티"]

numTeams = len(team_names)
teams = []
list_profile = ["호날두", "FW", "포르투갈", 186, 75, 35]

for i in range(numTeams):
    team = Team(team_names[i])
    for j in range(Team.numPlayers):
        p = Player(list_profile)
        team.addPlayer(p)
    teams.append(team)

epl = League(teams)
epl.begin()
# print(epl.getSchedule())
for i in range(epl.getTotalRound()):
	epl.nextRound()
	epl.showTable()


# 가상의 선수 23명으로 팀을 만들어보았습니다.
# 선수 한명에 관한 정보를 출력해봅시다
teamName = teams[4].getTeamName()
print(f'{teamName}')
for i, player in enumerate(teams[4].getPlayers()):
    print(i, player.getProfileObj().getProfile()["이름"], end='\t')
    print(player.getProfileObj().getProfile()["포지션"], end='\t')
    print(player.getAbilityObj().getTechnical()["드리블"], end='\t')
    print(player.getAbilityObj().getMental()["시야"], end='\t')
    print(player.getAbilityObj().getPhysical()["스피드"], end='\t')
    print(player.getStatObj().getStat()["도움"], end='\t')
    print(player.getFormObj().getForm()["부상"])
