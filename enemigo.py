import pygame
from player import *
from constantes import *
from auxiliar import Auxiliar
from rock import *

class Enemy():
    def __init__(self, enemy = 1,x=100, y=200, move_x=5, speed=2, limit_x_start=0, limit_x_end=200, p_scale=1):

        if enemy == 1:
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Run_6.png", 6, 1, scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Run_6.png", 6, 1, flip=True, scale=p_scale)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png", 6, 1, scale=p_scale)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png", 6, 1, flip=True, scale=p_scale)
            self.dead_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Death_8.png", 8, 1 ,scale=p_scale)
            self.dead_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Death_8.png", 8, 1, flip=True ,scale=p_scale)
        elif enemy == 2:
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemies\monstruito_celeste\Dude_Monster_Run_6.png", 6, 1, scale=p_scale)
            self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemies\monstruito_celeste\Dude_Monster_Run_6.png", 6, 1, flip=True, scale=p_scale)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png", 6, 1, scale=p_scale)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png", 6, 1, flip=True, scale=p_scale)
            self.dead_r = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemies\monstruito_celeste\Dude_Monster_Death_8.png", 8, 1 ,scale=p_scale)
            self.dead_l = Auxiliar.getSurfaceFromSpriteSheet("images\caracters\enemies\monstruito_celeste\Dude_Monster_Death_8.png", 8, 1, flip=True ,scale=p_scale)

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
        self.is_dead = False

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

    def dead(self):
        if self.is_dead:
            self.is_dead = False
            if self.animation == self.walk_r:
                self.move_x = 0
                self.frame = 0
                self.animation = self.dead_r
            elif self.animation == self.walk_l:
                self.move_x = 0
                self.frame = 0
                self.animation = self.dead_l


    def check_collision(self, player, rocks):
        self.collision_rect = pygame.Rect(self.rect.x + self.rect.w/2.7, self.rect.y, self.rect.width // 3, self.rect.height)
        if self.collision_rect.colliderect(player.trap_collition):
            if player.trap_collition.y < self.rect.y and player.invulnerable== False:
                self.is_dead = True
            player.hit_player(2)

        for rock in rocks:
            if self.collision_rect.colliderect(rock.rect):
                self.is_dead = True
                rock.kill()


                

    def update(self, player_rect, rock, enemy_list, enemy_index):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.tiempo_transcurrido_animation

        if elapsed_time > self.frame_rate_ms:
            self.tiempo_transcurrido_animation = current_time
            self.frame += 1

            if self.frame >= len(self.animation):
                if self.animation == self.dead_r or self.animation == self.dead_l:
                    del enemy_list[enemy_index]
                else:
                    self.frame = 0
                    # Eliminar el enemigo de la lista
                    

        self.check_collision(player_rect, rock)
        self.do_movement()
        self.dead()

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, BLUE, self.collision_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)