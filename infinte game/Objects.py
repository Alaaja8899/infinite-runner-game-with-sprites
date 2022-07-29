import pygame as pyg , random as rand
from pygame.locals import*
 
# ------------------------------------------------------------------------------
# functions and classes
class Bg:
	def __init__(self,x,y,image):
		self.image,self.x,self.y = image,x,y
	def update(self,screen,scrn_size):
		self.x -=5
		screen.blit(self.image,[self.x,self.y])
		screen.blit(self.image,[1000+self.x,self.y])
		if self.x <= -scrn_size[0]:
			self.x = 0
# ---------------------------------------------------------
# obstacle-class :-
class Obstacle:
	def __init__(self,x,y,image):
		self.x,self.y = x,y
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.obstacle_speed = 5
	def update(self,screen,scrn_size):
		if self.rect.x >= -scrn_size[0]//2:
			self.rect.x -= self.obstacle_speed
		else:
			self.rect.x = rand.randint(1000,4000)
		screen.blit(self.image,self.rect)
		# pyg.draw.rect(screen,'black',self.rect,2)


# class of the dimond :--
class Dimond:
	def __init__(self,x,y,image):
		self.x,self.y = x,y
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = [self.x,self.y]
		self.vel = 5
	def update(self,screen):
		if self.rect.x >= -200:
			self.rect.x -= self.vel
		else:
			self.rect.x = rand.randint(1000,5000)
		screen.blit(self.image,self.rect)
		# pyg.draw.rect(screen,'black',self.rect,2)
	def restart(self,Player):
		coin = False
		if Player.colliderect(self.rect):
			self.rect.x = rand.randint(1000,4000)
			coin = True
		return coin
# -----------------------------------------------------
# player class
class Player(Bg):
	def __init__(self,x,y,images,jump_images):
		self.x,self.y = x,y
		self.index = 0
		self.counter  = 0
		self.images = images
		self.jump_images = jump_images
		self.image = self.images[self.index]
		self.image_rect = self.image.get_rect()
		self.image_rect.topleft = [self.x,self.y]
		self.velocity = 3*2
		self.jump = False
		self.y_vel = 20
		self.jump_heigtht = self.y_vel
		self.gravity = 1
		self.width = self.image.get_width()
		self.height = self.image.get_height()
	def update(self,screen,sound):

		
		# left and right motion
		key = pyg.key.get_pressed()
		if key[K_RIGHT]:
			self.image_rect.x += self.velocity
		elif key[K_LEFT]:
			self.image_rect.x -= self.velocity*2
		elif key[K_SPACE] and self.jump == False:
			sound.play()
			self.jump = True
		# images animation 
		self.counter +=1
		if self.counter >=5:
			self.index +=1
			if self.index >= len(self.images):
				self.index = 0
			self.counter = 0
		
		# jump animation 
		if self.jump:
			if self.index >= len(self.jump_images):
				self.index -=1
			self.image = self.jump_images[self.index]
			self.image_rect.y -= self.y_vel
			self.y_vel -= self.gravity
			if self.y_vel <-self.jump_heigtht:
				self.jump = False
				self.y_vel = self.jump_heigtht
		
		# drawing into the screen
		self.image = self.images[self.index]
		screen.blit(self.image,self.image_rect)
		# pyg.draw.rect(screen,'black',self.image_rect,2)

	def detect_collision(self,rect_list):
		collide = False
		for rectangle in rect_list:
			for item in rectangle:
				if item.colliderect(self.image_rect):
					collide  = True
		return collide
	def coins(self,dimonds):
		coin = False
		for dm in dimonds:
			if dm.colliderect(self.image_rect.x-30,self.image_rect.y ,self.width,self.height):
				coin = True
		return coin
	# def elf):
		# pass
# --------------------------------------------------------------