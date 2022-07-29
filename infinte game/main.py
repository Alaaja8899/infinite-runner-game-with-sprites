"""
Aouthor : {Abdirizak abdullahi hussein}}
date : 25/7/2022

Note:- i have on only the code this beutiful graphics i get from online 
the code is free i was just chilling to code this game 
"""

import pygame as pyg ,random as rand ,sys,os,time
from pygame.locals import *
from Objects import *
# ----------------------------------------------
scrn_size = [1000,500]
pyg.init()
screen = pyg.display.set_mode(scrn_size)
pyg.display.set_caption('infinte-runner')
# ----------------------------------------------

# images 
bg = pyg.transform.scale(pyg.image.load('img/BG.jpg'),scrn_size)
pl_imgs = [pyg.transform.scale(pyg.image.load(f'Player/Run__00{num}.png'),[150,150]) for num in range(0,10)]
jump_imgs = [pyg.transform.scale(pyg.image.load(f'Player/Jump__00{num}.png'),[150,200]) for num in range(1,10)]
gover_img = pyg.transform.scale(pyg.image.load('img/gover.png'),[300,200])
# -------------------------------------------------------------------------------------------------------------------------
# obsctacles images 
box_img = pyg.transform.scale(pyg.image.load('img/box.png'),[50,50])
bujuq_img  = pyg.transform.scale(pyg.image.load('img/bujuq.png'),[50,40])
mushrom_img = pyg.transform.scale(pyg.image.load('img/mushroom.png'),[50,50])
dimond_imgs = [pyg.transform.scale(pyg.image.load(f'img/d{num}.png'),[50,50]) for num in range(1,5)]

print(len(dimond_imgs))

# game-variables
timer = pyg.time.Clock()
fps = 30
rect_list = []
score_count = 0
# objects
def Objects():
	global background
	global player
	global mush
	global box
	global buj
	background  = Bg(0,0,bg)
	player = Player(100,300-10,pl_imgs,jump_imgs)
	mush = Obstacle(rand.randint(1000,2000),325+60,mushrom_img)
	box = Obstacle(rand.randint(2000,3000),325+60,box_img)
	buj = Obstacle(rand.randint(3000,4000),325+60,bujuq_img)
Objects()
def make_dimond(dimonds):
	for count in range(0,4):
		dm = Dimond(rand.randint(1000,5000),325+60,dimond_imgs[count])
		dimonds.append(dm)

rect_list.append([mush.rect,buj.rect,box.rect])
Dimonds = []
make_dimond(Dimonds)
print(len(Dimonds))
on_mode = True
# mt = Math()
# sounds 
dm_rects = [dm.rect for dm in Dimonds]
init = pyg.mixer.init()
soundObj = pyg.mixer.Sound('beeb.wav')
pyg.mixer.music.load('sounds/bg.mp3')
pyg.mixer.music.play(-1)
game_over_sound = pyg.mixer.Sound('sounds/over.wav')
coins_sound = pyg.mixer.Sound('sounds/coin.wav')
jump_sound = pyg.mixer.Sound('sounds/jump.wav')




def Score(score_count):
	score_font = pyg.font.SysFont('carbel',35)
	txt = f'Score : {score_count}'
	obj = score_font.render(txt,True,'blue')
	screen.blit(obj,[10,10])
# game-over surface 
def game_over():
	global on_mode
	while on_mode:
 		screen.fill('black')
 		screen.blit(bg,[0,0])
 		screen.blit(gover_img,[scrn_size[0]//2-50-100,300-200])
 		for event in pyg.event.get():
 			if event.type == QUIT:
 				sys.exit()
 				pyg.quit()
 		if key_pressed[K_SPACE]:
 			Active = True
 			on_mode = False

 		pyg.display.update()
 		time.sleep(5)
 		pyg.quit()
 		sys.exit()
Active = True
running = True

# main-loop or 'main-logic'
while running:
	screen.fill([0,0,0])
	timer.tick(fps)

	# updating each objects
	if Active:
		background.update(screen,scrn_size)
		player.update(screen,jump_sound)
		mush.update(screen,scrn_size)
		box.update(screen,scrn_size)
		buj.update(screen,scrn_size)
	else:
		game_over()
	for dimond in Dimonds:
		dimond.update(screen)
		if dimond.restart(player.image_rect):
			coins_sound.play()
			score_count +=1
			print(score_count)
	# event handling
	for event in pyg.event.get():
		if event.type == QUIT:
			running = False
	if player.detect_collision(rect_list):
			Active = False
			game_over_sound.play()
	key_pressed = pyg.key.get_pressed()
	if player.coins(dm_rects):
		pass
	Score(score_count)
	if key_pressed[K_ESCAPE]:
		running = False
	# mt.add(scrn_size[0],scrn_size[1])
	pyg.display.update()
pyg.quit()