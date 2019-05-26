import pygame as pg
import random
from pygame.locals import *

pg.init()
pg.mixer.init()
clock = pg.time.Clock()

#畫布、背景
width, height = 1200, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("13's game")

bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))
screen.blit(bg, (0, 0))
pg.display.update()


board_image = 'Blank_Go_board.png'
frame_image = 'frame2.png'

def board_reset():
	global background_image
	background_image = pg.image.load(board_image).convert_alpha()
	background_image = pg.transform.scale(background_image, (590, 590))
	

#玩家資訊欄
pg.draw.rect(bg, (230,230,230), [1000, 0, 200, 200], 10)
pg.draw.rect(bg, (230,230,230), [1000, 200, 200, 200], 10)
pg.draw.rect(bg, (230,230,230), [1000, 400, 200, 200], 10)

font = pg.font.SysFont("simhei", 24)

text = font.render("113", True, (0, 0, 0), (255, 255, 255))
bg.blit(text, (1010, 10))
text = font.render("213", True, (0, 0, 0), (255, 255, 255))
bg.blit(text, (1010, 210))
text = font.render("313", True, (0, 0, 0), (255, 255, 255))
bg.blit(text, (1010, 410))

pg.draw.circle(bg, (41, 36, 33), (1050, 17), 8, 0)
pg.draw.circle(bg, (230, 230, 230), (1050, 217), 8, 0)
pg.draw.circle(bg, (48, 120, 217), (1050, 417), 8, 0)

#出題資訊
pg.draw.rect(bg, (230,230,230), [50, 170, 200, 30], 5)
pg.draw.rect(bg, (230,230,230), [50, 200, 200, 100], 5)
text = font.render("Next Question", True, (0, 0, 0), (255, 255, 255))
bg.blit(text, (95, 180))
pg.draw.rect(bg, (230,230,230), [50, 300, 100, 30], 5)
pg.draw.rect(bg, (230,230,230), [150, 300, 100, 30], 5)
text = font.render("Right", True, (0, 250, 0), (255, 255, 255))
bg.blit(text, (80, 307))
text = font.render("Wrong", True, (250, 0, 0), (255, 255, 255))
bg.blit(text, (175, 307))
win = [0, 0, 0]


#棋盤座標
co = []
for i in range(19):
	co.append([])
	for j in range(19):
		a, b = int(320+30.6*i), int(20+30.65*j)
		co[i].append((a, b))
		
#誰下的
color = []
for i in range(19):
	color.append([])
	for j in range(19):
		color[i].append(0)
		
#距離公式
def dis(a, b):
	return (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])

who = 0	
whofirst = -1

#顯示換誰下
def change_sign_whos_turn():
	s = 0
	
#檢查獲勝
def check_win(x, y):
	dirx = [-1, 0, 1, 1, 1, 0, -1, -1]
	diry = [1, 1, 1, 0, -1, -1, -1, 0]
	cnt = [4, 4, 4, 4, 4, 4, 4, 4]
	u = 4
	for i in range(8):
		xx, yy = x, y
		for j in range(1, 5):
			xx = xx + dirx[i]
			yy = yy + diry[i]
			if(xx >= 19 or xx < 0 or yy >= 19 or yy < 0 or color[xx][yy] != color[x][y]):
				cnt[i] = j-1
				break
	if(cnt[0]+cnt[4]+1>=5):
		return True
	elif(cnt[1]+cnt[5]+1>=5):
		return True
	elif(cnt[2]+cnt[6]+1>=5):
		return True
	elif(cnt[3]+cnt[7]+1>=5):
		return True
	else :
		return False
	
#判斷下成功與否
def click_on_spot(pos):
	global who
	for i in range(19):
		for j in range(19):
			if dis(pos, co[i][j]) < 60 and color[i][j] == 0:
				return (i, j)
	return (-1, -1)
			
def put_chess(coordinates):
	global who
	i = coordinates[0]
	j =	coordinates[1]
	if who % 3 == 0:
		pg.draw.circle(background_image, (41, 36, 33), (co[i][j][0]-300, co[i][j][1]), 10, 0)
	elif who %3 == 1:
		pg.draw.circle(background_image, (230, 230, 230), (co[i][j][0]-300, co[i][j][1]), 10, 0)
	else:
		pg.draw.circle(background_image, (48, 120, 217), (co[i][j][0]-300, co[i][j][1]), 10, 0)
	color[i][j] = who + 1
	screen.blit(background_image, (300, 0))
	pg.display.update()	

def update_win():
	for i in range(len(win)):
		text = font.render("Wins : " + str(win[i]), True, (0, 0, 0), (255, 255, 255))
		bg.blit(text, (1010, 30+200*i))
	screen.blit(bg, (0, 0))
	pg.display.update()

def pop_frame():	
	sz = 10
	global frame
	while(sz <= 295):
		clock.tick(30)
		frame = pg.image.load(frame_image).convert_alpha()
		frame = pg.transform.scale(frame, (2*sz, sz))
		screen.blit(background_image, (300, 0))
		screen.blit(frame, (595 - sz, 290-sz/2)) 
		pg.display.update()
		sz = sz + 5

def reset_game():
	global who, whofirst
	board_reset()
	for i in range(19):
		for j in range(19):
			color[i][j] = 0
	whofirst = (whofirst + 1)%3
	who = whofirst
	
	
num_of_question = 1
num_of_choice = [0, 2]

def emergency():
	a = 0
	##輸出用完題目

##隨機出題
cur_prob = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
max_prob = [10,10,10,10,10,10,10,10,10,10]

def pop_question():	
	theme = random.randint(0,9)
	tmp_cnt = 0
	while(cur_prob[theme]>=max_prob[theme]):
		theme = random.randint(0,9)
		tmptmp = random.randint(0,9)
		theme = (theme+tmptmp)%10
		tmp_cnt = tmp_cnt + 1
		if tmp_cnt >= 500:
			print("running out of questions")
			emergency()
			return
	cur_prob[theme] = cur_prob[theme] + 1
	string = str(theme) + "-" + str(cur_prob[theme])
	text = font.render(string, True, (0, 0, 0), (255, 255, 255))
	bg.blit(text, (120, 230))
	screen.blit(bg, (0, 0))
	pg.display.update()	

##以下為main
running = True
update_win()
reset_game()
pause = False
wrong = 0
right = False
answering = False
coordinates = []

while running:
	pos = (0, 0)	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		elif event.type == MOUSEBUTTONDOWN:
			if pause == True:
				reset_game()
				pause = False
				break
			if answering == True:
				pos = pg.mouse.get_pos()
				pressed_array = pg.mouse.get_pressed()
				for index in range(len(pressed_array)):
					if(pressed_array[index]):
						if index == 0:
							if(pos[0]>=50 and pos[0] <= 149 and pos[1] >= 300 and pos[1] <= 330):
								wrong = 0
								right = True
								put_chess(coordinates)
								pg.mixer.music.load("correct.mp3")
								pg.mixer.music.play()
								answering = False
								who = (who+1)%3
								if(check_win(coordinates[0], coordinates[1])):
									win[whofirst] = win[whofirst]+1
									print("win!!!!!!!!!!!!!!!")	
									pg.mixer.music.load("mario.mp3")
									pg.mixer.music.play()
									pause = True
									update_win()
									pop_frame()
									break
							elif(pos[0]>=150 and pos[0] <= 250 and pos[1] >= 300 and pos[1] <= 330):
								wrong = wrong + 1
								pg.mixer.music.load("wrong.mp3")
								pg.mixer.music.play()
								right = False
								if wrong >= 3:
									wrong = 0
								answering = False
								who = (who+1)%3			
			else:
				pos = pg.mouse.get_pos()
				pressed_array = pg.mouse.get_pressed()
				for index in range(len(pressed_array)):
					if(pressed_array[index]):
						if index == 0:
							coordinates = click_on_spot(pos)
							print(pos)
							#按下棋盤座標後須要有回饋
							#按下按鈕要有回饋
							#待更改之處尚有很多
							if coordinates[0] == -1:
								break
							pg.mixer.music.load("chesssound.mp3")
							pg.mixer.music.play()
							if wrong == 0:
								pop_question()
							answering = True
	if(pause == False):
		screen.blit(background_image, (300, 0))
		pg.display.update()	
pg.quit()