import pygame 
from player import Player
from plataformas import *


class Botin():
    def __init__(self,type_botin = 1,x=100, y=200, p_scale=1):
        if type_botin == 1:
            self.rotate_animation_botin = Auxiliar.getSurfaceFromSpriteSheet("images\locations\coins_animation_gold.png",8,1,scale=p_scale)
        if type_botin == 2:
            self.rotate_animation_botin = Auxiliar.getSurfaceFromSpriteSheet("images\locations\coins_animation_silver.png",8,1,scale=p_scale)
        self.rect = self.rotate_animation_botin[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.obtain = False
        self.type_botin = type_botin
        
        self.collision_rect = pygame.Rect(self.rect.x + self.rect.w/2.7, self.rect.y, self.rect.width // 3, self.rect.height)
        self.animation = self.rotate_animation_botin
        self.frame = 0
        self.tiempo_transcurrido_animation = 0
        self.image = self.animation[self.frame]
        self.frame_rate_ms = FPS
        self.flag_first = True
        
    def check_collision(self, player):
        self.collision_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width , self.rect.height)
        if self.collision_rect.colliderect(player.trap_collition):
            self.obtain = True

            if self.flag_first == True:
                if self.type_botin == 1:
                    player.obtain_point(10)
                elif self.type_botin == 2:
                    player.obtain_point(5)
                self.flag_first = False
            print(player.score)


    def update(self, player_rect, point_list, point_index):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.tiempo_transcurrido_animation

        if elapsed_time > self.frame_rate_ms:
            self.tiempo_transcurrido_animation = current_time
            self.frame += 1

            if self.frame >= len(self.animation):
                self.frame = 0

        if self.obtain == True:
            
            del point_list[point_index]
                    # Eliminar el enemigo de la lista
                    

        self.check_collision(player_rect)

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, BLUE, self.collision_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)