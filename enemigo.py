import pygame
from player import *
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    def __init__(self, x=100, y=200, move_x=5, speed=2, limit_x_start=0, limit_x_end=200, p_scale=1):
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Run_6.png", 6, 1, scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Run_6.png", 6, 1, flip=True, scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png", 6, 1, scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png", 6, 1, flip=True, scale=p_scale)
        
        self.rect = self.walk_l[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = move_x
        self.speed_walk = speed
        self.limit_x_start = x + limit_x_start
        self.limit_x_end = x + limit_x_end
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = FPS
        self.frame = 0
        self.animation = self.walk_l
        self.direction = DIRECCION_L
        self.image = self.animation[self.frame]
        self.contador = 0

        # Definir el tamaño del rectángulo de colisión del enemigo
        self.collision_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width // 2, self.rect.height)

    def change_x(self, delta_x):
        self.rect.x += delta_x

    def do_movement(self):
        if self.rect.x <= self.limit_x_start:
            self.move_x = self.speed_walk
            self.animation = self.walk_r
        elif self.rect.x >= self.limit_x_end:
            self.move_x = -self.speed_walk
            self.animation = self.walk_l

        self.change_x(self.move_x)

    def check_collision(self, player):
        self.collision_rect = pygame.Rect(self.rect.x +self.rect.w/2.7, self.rect.y, self.rect.width // 3, self.rect.height)
        if self.collision_rect.colliderect(player.trap_collition):
            # Colisión detectada, puedes agregar aquí el código que deseas ejecutar cuando ocurra la colisión
            print("¡El enemigo ha chocado con el jugador!")
            player.hit_player()

    def update(self, player_rect):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.tiempo_transcurrido_animation

        if elapsed_time > self.frame_rate_ms:
            self.tiempo_transcurrido_animation = current_time
            self.frame += 1
            if self.frame >= len(self.animation):
                self.frame = 0
        self.check_collision(player_rect)
        self.do_movement()

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, BLUE, self.collision_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)