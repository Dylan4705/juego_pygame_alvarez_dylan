import pygame
from player import *
from constantes import *

class throw_rock(pygame.sprite.Sprite):
	def __init__(self,pos,speed,screen_height,direction):
		super().__init__()
		self.direction = direction
		self.image = pygame.Surface((4,20))
		self.image = pygame.image.load("images/caracters/enemies/monstruito_celeste\Rock2.png").convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.height_y_constraint = screen_height
	def destroy(self):
		if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
			self.kill()

	def update(self):
		if self.direction == DIRECCION_L:
			self.rect.x += self.speed
		if self.direction == DIRECCION_R:
			self.rect.x -= self.speed
		print(self.direction)
		self.destroy()
    
