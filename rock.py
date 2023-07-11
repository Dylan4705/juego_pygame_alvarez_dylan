import pygame
from player import *
from constantes import *

class throw_rock(pygame.sprite.Sprite):
	def __init__(self,pos,speed,screen_height,direction,is_a_enemy):
		super().__init__()
		self.direction = direction
		self.image = pygame.Surface((4,20))
		self.is_a_enemy = is_a_enemy
		if self.is_a_enemy == False:
			self.image = pygame.image.load("images/caracters/enemies/monstruito_celeste\Rock2.png").convert_alpha()
		else:
			self.image = pygame.image.load("images\caracters/7 Bird\pngfind.com-snowball-png-375535.png").convert_alpha()
			self.image = pygame.transform.scale(self.image,(10,10))
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.height_y_constraint = screen_height
	def destroy(self):
		if self.is_a_enemy == False:
			if self.rect.x <= -50 or self.rect.x >= ANCHO_VENTANA + 50:
				self.kill()
				
		else:
			if self.rect.y >= ALTO_VENTANA or self.rect.x <= -50 or self.rect.x >= ANCHO_VENTANA + 50:
				self.kill()



	def update(self,screen,player):
		if player.is_paused == False:
			if self.is_a_enemy == False:
				if self.direction == DIRECCION_L:
					self.rect.x += self.speed
				if self.direction == DIRECCION_R:
					self.rect.x -= self.speed
			if self.is_a_enemy == True:
				self.rect.y -= self.speed
			if self.is_a_enemy == False:
				self.rock_collition = pygame.Rect(self.rect.x,self.rect.y,self.rect.w,self.rect.h)
			else:
				self.rock_collition = pygame.Rect(self.rect.x,self.rect.y,self.rect.w,self.rect.h)
		else:
			self.rect.x += 0
			self.rect.y += 0
		if DEBUG:
			pygame.draw.rect(screen,BLUE,self.rock_collition)
		self.destroy()
		

           