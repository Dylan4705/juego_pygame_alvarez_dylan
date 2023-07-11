import pygame
from constantes import *

class platform_movile(pygame.sprite.Sprite):
    def __init__(self, image_number, x, y, width, height, limit_x_start, limit_x_end, speed,player):
        super().__init__()

        self.image = pygame.image.load("images\locations\plataforma.png") 
        self.image = pygame.transform.scale(self.image,(width,height))
        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()
        self.collision_with_player = pygame.Rect(self.rect.x +self.rect.w/2.7,self.rect.y + self.rect.h - 25,self.rect.w /4,10)
        # Establecer la posición inicial
        self.rect.x = x
        self.rect.y = y
        self.player = player

        # Guardar los atributos adicionales
        self.width = width
        self.height = height
        self.limit_x_start = limit_x_start
        self.limit_x_end = limit_x_end
        self.speed = speed


    def update(self,player):  
        if player.is_paused == False: 
            self.collision_with_player = pygame.Rect(self.rect.x ,self.rect.y-100,self.rect.w,self.rect.h+100)         
            if self.collision_with_player.colliderect(self.player.trap_collition):
                self.rect.x += self.speed
                
                if self.rect.x < self.limit_x_start or self.rect.x > self.limit_x_end:
                    self.speed *= -1  # Invertir la dirección si alcanza un límite



    def draw(self, screen,offset_x):
        screen.blit(self.image, self.rect)
        if DEBUG:
            pygame.draw.rect(screen, BLUE, self.collision_with_player)
        