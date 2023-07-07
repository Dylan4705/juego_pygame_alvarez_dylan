import pygame
from constantes import *
from rock import throw_rock
from auxiliar import Auxiliar
from plataformas import *
from trampas import *




orco_verde = {"walk":"caracters/Orc_Warrior/Run.png",
                  "stay": "caracters/Orc_Warrior/Idle.png",
                  "jump": "caracters/Orc_Warrior/jump.png",
                  "jump_Fall": "caracters/Orc_Warrior/jump_Fall.png",
                  "hurt": "caracters/Orc_Warrior/Hurt.png",
                  "shoot": "caracters/Orc_Warrior/Attack_2.png",
                  "knife": "caracters/Orc_Warrior/Attack_1.png"}




class Player:
    def __init__(self,player,x,y,speed_walk,speed_run,gravity,max_limit,p_scale) -> None:

        if player == 0:
            player = orco_verde
        # else:                             #ELEGIR OTRO PERSONAJE
        #     player = personaje_azul
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["walk"]),6,1,scale = p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["walk"]),6,1,True ,scale = p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["stay"]),5,1,True ,scale = p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["stay"]),5,1 ,scale = p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["jump"]),8,1 ,scale = p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["jump"]),8,1,True ,scale = p_scale)
        self.jump_Fall_l = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["jump_Fall"]),2,1,True ,scale = p_scale)
        self.jump_Fall_r = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["jump_Fall"]),2,1 ,scale = p_scale)
        self.hurt_l = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["hurt"]),2,1 ,True,scale = p_scale)
        self.hurt_r = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["hurt"]),2,1 ,scale = p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["shoot"]),4,1,scale = p_scale)
        self.shoot_l = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["shoot"]),4,1,True,scale = p_scale)
        self.knife_r = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["knife"]),4,1 ,scale = p_scale)
        self.knife_l = Auxiliar.getSurfaceFromSpriteSheet((PATH_IMAGE + player["knife"]),4,1,True ,scale = p_scale)
        self.hud_life = Auxiliar.getSurfaceFromSpriteSheet("images\hud\life\HealthUI.png",1,7,False,scale= p_scale)


        self.max_limit = max_limit

        self.tiempo_transcurrido_animacion = 0
        self.tiempo_transcurrido_movement = 0
        
        self.is_fall = True
        self.frame = 0
        self.lives = 6
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.rock = pygame.sprite.Group()
        self.ready_for_shoot = True
        self.shoot_time = 0
        self.shoot_cooldown = 600


        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.recibe_hurt = False
   
        self.animation = self.stay_l
        self.direction = DIRECCION_L
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        self.jump_count = 0
        self.fall_count = 0
        self.invulnerable = False  # Variable de estado de invulnerabilidad
        self.invulnerable_timer = 0  # Temporizador de invulnerabilidad
        self.invulnerable_duration = 600  # Duración en milisegundos de la invulnerabilidad
        
        self.trap_collition = pygame.Rect(self.rect.x +self.rect.w/2.7,self.rect.y + self.rect.h - 14,self.rect.w /4,10)


    


    def landed(self):
  
        self.fall_count = 0
        self.move_y = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.move_y *= -1

    def handle_vertical_collision(player, objects, dy):
        collided_objects = []
        trap_collision = False

        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if isinstance(obj, Trap):
                    trap_collision = True
                else:

                    
                    if dy > 0:
                        player.rect.bottom = obj.rect.top
                        player.landed()
                    elif dy < 0:
                        player.rect.top = obj.rect.bottom
                        player.hit_head()


                collided_objects.append(obj)


        
        if trap_collision:
            
            player.hit_player(3)
            print(player.lives)

        return collided_objects

 
    def hit_player(self,negative_lives):
        if not self.invulnerable:

            self.lives -= negative_lives
            self.move_y = -self.gravity* 0.5
            if self.direction == DIRECCION_L:
                self.move_x += self.gravity*0.3
                
            else:
                self.move_x += -self.gravity*0.3
            self.frame = 0

            self.recibe_hurt = True
            self.invulnerable = True  # Activar el estado de invulnerabilidad
            self.invulnerable_timer = pygame.time.get_ticks()  # Iniciar el temporizador
            print(self.lives)


    def get_input(self):
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]):
                self.walk(DIRECCION_L)
            if(keys[pygame.K_RIGHT]and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]):
                self.walk(DIRECCION_R)
            if(not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]):
                self.stay()
            if(keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and not keys[pygame.K_UP]):
                self.stay()
            if keys[pygame.K_z] and self.ready_for_shoot:
                self.shoot_objeto() 
                self.ready_for_shoot = False
                self.shoot_time = pygame.time.get_ticks()

            

    

    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            
            self.frame= 0
            self.direction=direction
            if direction == DIRECCION_R:
                self.move_x = self.speed_walk
                
            else:
                self.move_x = -self.speed_walk


    def jump(self):
        self.move_y = -self.gravity* 0.7
        self.frame = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
            self.is_fall = True
            



    def do_movement(self,delta_ms):
    
        self.tiempo_transcurrido_movement += delta_ms
        if(self.tiempo_transcurrido_movement > 10):


            self.tiempo_transcurrido_movement = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)




        self.trap_collition = pygame.Rect(self.rect.x +self.rect.w/2.7,self.rect.y + self.rect.h - 25,self.rect.w /4,10)


# def esta_en_plataforma(self, lista_plataformas):
#         retorno = False
#         for plataforma in lista_plataformas:
#             if self.rectangulo_colision_suelo.colliderect(plataforma.rectangulo_colision_suelo):
#                 retorno = True
#                 self.rectangulo.y = plataforma.rectangulo.y - self.rectangulo.h  # Ajusta la posición del jugador al nivel de la plataforma
#                 break
#         return retorno

    def limits(self):
        if self.rect.left <=-50:
            self.rect.left = -50
        if self.rect.right >= self.max_limit:
            self.rect.right = self.max_limit
    




        

    def stay(self):
            self.move_x = 0
            if(self.is_fall == False):
                self.move_y = 0
            self.frame = 0

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms
        if self.tiempo_transcurrido_animacion > 100:
            self.tiempo_transcurrido_animacion = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

            if self.frame >= len(self.animation):
                self.frame = len(self.animation) - 1



        


   
    def shoot_objeto(self):
        self.rock.add(throw_rock(self.rect.center,-8,self.rect.bottom,self.direction))


    def recharge(self):
        if not self.ready_for_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cooldown:
                self.ready_for_shoot = True


    #CORDENAS RECTANGULOS
    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.trap_collition.x += delta_x
    
    def add_y(self,delta_y):
        self.rect.y += delta_y
        self.trap_collition.y += delta_y

    def draw_hearts(self, screen):
            
            if self.lives == 6:
                heart = self.hud_life[0]
            if self.lives == 5:
                heart = self.hud_life[1]
            if self.lives == 4:
                heart = self.hud_life[2]
            if self.lives == 3:
                heart = self.hud_life[3]
            if self.lives == 2:
                heart = self.hud_life[4]
            if self.lives == 1:
                heart = self.hud_life[5]
            if self.lives <= 0:
                heart = self.hud_life[6]
            x = 0 # Posición x inicial
            y = 0+5 # Posición y
            heart = pygame.transform.scale(heart, (33*5, 10*5))
            screen.blit(heart, (x, y))

    def update_sprites(self):
        try:
            if self.jump_count != 0:
                
                if self.direction == DIRECCION_L:
                    self.animation = self.jump_Fall_l
                else:
                    self.animation = self.jump_Fall_r


            elif self.move_x != 0:
                
                if self.direction == DIRECCION_L:
                    self.animation = self.walk_l
                else:                  
                    self.animation = self.walk_r

                    

            else:
                
                if self.direction == DIRECCION_L:            
                    self.animation = self.stay_l
                else:                  
                    self.animation = self.stay_r
            
            self.image = self.animation[self.frame]
            
            
        except IndexError:
            print("Error: Índice fuera de rango al acceder a la animación")
            
        
    def do_gravity(self):
        self.move_y += min(1, (self.fall_count / FPS) * self.gravity)
        self.fall_count +=1

    def update(self,delta_ms,object,screen):
        self.do_gravity()
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.update_sprites()
        self.limits()
        self.recharge()
        self.handle_vertical_collision(object,self.move_y)
        self.rock.update(screen)
        self.rock.draw(screen)
        self.draw_hearts(screen)
        # print("x={0} y={1}".format(self.rect.x,self.rect.y))
        

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,BLUE,self.trap_collition)


        

        
        screen.blit(self.image,self.rect)
