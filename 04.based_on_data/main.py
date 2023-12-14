from team import Team
from team_stat import TeamStat
from league import League
from player import Player
import pygame
import numpy as np  
import csv
import random







ground_img = pygame.image.load("./img/ground.png")
w, h = ground_img.get_rect().size

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (100,100,100)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
RED = (255,0,0)
half_grid_size = (100, 100)
padding = 40
print(w,h)
input()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("football simulator")
clock  = pygame.time.Clock()

detail = 100
ground_rect = [
            36, 
            20, 
            1156, 
            775 
            ]

sx = ground_rect[0]
sy = ground_rect[1]
ex = ground_rect[2]
ey = ground_rect[3]

dx = (ex - sx) / (detail * 2) 
dy = (ey - sy) / detail


grid = []
for x in range(half_grid_size[0] * 2):
    row = []
    for y in range(half_grid_size[1]):
        row.append(0)
    grid.append(row)


teams = {}
with open('./data/team_stats.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        teams[row['common_name']] = Team(row)

# print(teams['West Ham United'].name)
players = {}
with open('./data/player_stats.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        teams[row['Current Club']].addPlayer(row)

# print(teams['Tottenham Hotspur'].players['Heung-Min Son'])


# ground_img = ground_img.subsurface((100*j, 100*i, cell_size2, cell_size2))
def drawGround():
    screen.blit(ground_img, (0,0))

def drawGrid(visible):
    global ground_rect
    for i in range(detail * 2 + 1):
        curr_x = sx + i * dx
        if visible:
            pygame.draw.line(screen, GRAY, [curr_x,sy], [curr_x,ey], 1)

    for i in range(detail + 1):
        curr_y = sy + i * dy
        if visible:
            pygame.draw.line(screen, GRAY, [sx,curr_y], [ex,curr_y], 1)


def drawBall(pos_x, pos_y):
    global ground_rect
    curr_x = sx + pos_x * dx
    curr_y = sy + pos_y * dy
    pygame.draw.circle(screen, YELLOW, (curr_x, curr_y), 5)


def drawPlayer(pos_x, pos_y, home, possessed):
    global ground_rect
    curr_x = sx + pos_x * dx
    curr_y = sy + pos_y * dy
    if possessed:
        pygame.draw.circle(screen, GRAY, (curr_x, curr_y), 8)
    elif home:
        pygame.draw.circle(screen, BLUE, (curr_x, curr_y), 8)
    else:
        pygame.draw.circle(screen, RED, (curr_x, curr_y), 8)


def drawPlayers(eleven, home):
    for _, player in eleven.items():
        px, py = player['Pos']
        print(px, py)
        drawPlayer(px, py, home, player['possession'])

def drawEverything(home_players, away_players):
    drawGround()
    drawGrid(visible=True)
    drawPlayers(home_players, True)
    drawPlayers(away_players, False)
    drawBall(match_homeTeam.ball_pos[0], match_homeTeam.ball_pos[1])





epl = League(teams)
team1 = epl.teams['Tottenham Hotspur']
team2 = epl.teams['Manchester City']

epl.nextMatch(team1, team2)

homeTeamPlayers = homeTeam.match.formation.eleven
awayTeamPlayers = awayTeam.match.formation.eleven

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    match_homeTeam.chaseBall()
    match_awayTeam.chaseBall()

    match_homeTeam.dribble()
    match_awayTeam.dribble()

    match_homeTeam.ballPass()
    match_awayTeam.ballPass()

    match_homeTeam.ballMove()
    match_awayTeam.ballMove()
    
    drawEverything(homeTeamPlayers, awayTeamPlayers)
    pygame.display.flip()
    clock.tick(120)



# epl = League(teams)
# epl.begin()
# # print(epl.getSchedule())
# for i in range(epl.getTotalRound()):
# 	epl.nextRound()
# 	epl.showTable()


# # 가상의 선수 23명으로 팀을 만들어보았습니다.
# # 선수 한명에 관한 정보를 출력해봅시다
# teamName = teams[4].getTeamName()
# print(f'{teamName}')
# for i, player in enumerate(teams[4].getPlayers()):
#     print(i, player.getProfileObj().getProfile()["이름"], end='\t')
#     print(player.getProfileObj().getProfile()["포지션"], end='\t')
#     print(player.getAbilityObj().getTechnical()["드리블"], end='\t')
#     print(player.getAbilityObj().getMental()["시야"], end='\t')
#     print(player.getAbilityObj().getPhysical()["스피드"], end='\t')
#     print(player.getStatObj().getStat()["도움"], end='\t')
#     print(player.getFormObj().getForm()["부상"])
