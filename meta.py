# import pygame
# from player import *
# from constantes import *
# from auxiliar import Auxiliar


# class meta_():
#     def __init__(self,x=100, y=200, p_scale=1):
#         self.portal_animation = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\Orc_Warrior\Dead.png", 6, 1, flip=True ,scale=p_scale)
        
#         self.rect = self.portal_animation[0].get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.tiempo_transcurrido_animation = 0
#         self.frame_rate_ms = FPS
#         self.frame = 0
#         self.animation = self.portal_animation
#         self.image = self.animation[self.frame]
#         self.paused_frame = 0

#         # Definir el tamaño del rectángulo de colisión del enemigo
#         self.collision_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width // 2, self.rect.height)



#     def check_collision(self, player, enemy_list):
#         self.collision_rect = pygame.Rect(self.rect.x + self.rect.w/2.7, self.rect.y, self.rect.width // 3, self.rect.height)
#         if player.is_dead == False:
#             if self.collision_rect.colliderect(player.trap_collition) and not enemy_list:
#                 player.is_win = True
#         else:
#             pass





#     def update(self, player_rect, enemy_list):
#         current_time = pygame.time.get_ticks()
#         elapsed_time = current_time - self.tiempo_transcurrido_animation

#         if player_rect.is_paused:
#             self.frame = self.paused_frame
#         else:
#             if elapsed_time > 1000 / FPS:  # Actualiza el atributo frame_rate_ms con el valor correcto
#                 self.tiempo_transcurrido_animation = current_time
#                 self.frame += 1

#                 if self.frame >= len(self.animation):
#                     self.frame = 0
                    
#         self.image = self.animation[self.frame]
#         self.check_collision(player_rect,enemy_list)




        

        

#     def draw(self, screen):
#         if DEBUG:
#             pygame.draw.rect(screen, RED, self.rect)
#             pygame.draw.rect(screen, BLUE, self.collision_rect)
#         self.image = self.animation[self.frame]
#         screen.blit(self.image, self.rect)

import pygame 
from player import Player
from plataformas import *


class meta_():
    def __init__(self,x=100, y=200, p_scale=1):
        self.portal_animation = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\Orc_Warrior\Dead2.png",6, 1, flip=True ,scale=p_scale)
        self.rect = self.portal_animation[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collision_rect = pygame.Rect(self.rect.x + self.rect.w/2.7, self.rect.y, self.rect.width // 3, self.rect.height)
        self.animation = self.portal_animation
        self.frame = 0
        self.tiempo_transcurrido_animation = 0
        self.image = self.animation[self.frame]
        self.frame_rate_ms = FPS
        self.paused_frame = 0


    def check_collision(self, player,enemy_list):
        self.collision_rect = pygame.Rect(self.rect.x+20, self.rect.y+20, self.rect.width/1.6 , self.rect.height/1.6)
        if self.collision_rect.colliderect(player.trap_collition):
            if enemy_list:
                pass
            else:
                player.is_win = True

    def update(self, player_rect, enemy_list):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.tiempo_transcurrido_animation
        if elapsed_time > self.frame_rate_ms:
            self.tiempo_transcurrido_animation = current_time
            self.frame += 1

            if self.frame >= len(self.animation):
                self.frame = 0
                    

        self.check_collision(player_rect,enemy_list)

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, BLUE, self.collision_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)