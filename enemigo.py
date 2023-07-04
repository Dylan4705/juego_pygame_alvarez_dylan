# from player import *
# from constantes import *
# from auxiliar import Auxiliar


# class Enemy():
    
#     def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,p_scale) -> None:
#         self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Walk_6.png",4,1,scale=p_scale)
#         self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Walk_6.png",4,1,flip=True,scale=p_scale)
#         self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Idle_4.png",4,1,scale=p_scale)
#         self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Idle_4.png",4,1,flip=True,scale=p_scale)

#         self.contador = 0
#         self.frame = 0
#         self.lives = 5
#         self.score = 0
#         self.move_x = 0
#         self.move_y = 0
#         self.speed_walk =  speed_walk
#         self.speed_run =  speed_run
#         self.gravity = gravity
#         self.jump_power = jump_power
#         self.animation = self.stay_r
#         self.direction = DIRECCION_R
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
#         self.ground_collition_rect = pygame.Rect(self.collition_rect)
#         self.tiempo_transcurrido_animation = 0
#         self.frame_rate_ms = frame_rate_ms
#         self.is_jump = False
#         self.is_fall = False
#         self.is_shoot = False
#         self.is_knife = False

# class Player:
#     def __init__(self,x,y,limit_x,limit_y,dead) -> None:


#         self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Walk_6.png",4,1,scale=p_scale)
#         self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Walk_6.png",4,1,flip=True,scale=p_scale)
#         self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Idle_4.png",4,1,scale=p_scale)
#         self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/enemies/monstruito_celeste/Dude_Monster_Idle_4.png",4,1,flip=True,scale=p_scale)

#         self.x = x
#         self.y = y
#         self.limit_x = limit_x
#         self.limit_y = limit_y


    


        

 

#     def walk(self,direction):
#         if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            
#             self.frame= 0
#             self.direction=direction
#             if direction == DIRECCION_R:
#                 self.move_x = self.speed_walk
                
#             else:
#                 self.move_x = -self.speed_walk





#     def do_movement(self,delta_ms):
    
#         self.tiempo_transcurrido_movement += delta_ms
#         if(self.tiempo_transcurrido_movement > 10):


#             self.tiempo_transcurrido_movement = 0
#             self.add_x(self.move_x)
#             self.add_y(self.move_y)



#         self.trap_collition = pygame.Rect(self.rect.x +self.rect.w/2.7,self.rect.y + self.rect.h - 25,self.rect.w /4,10)


# # def esta_en_plataforma(self, lista_plataformas):
# #         retorno = False
# #         for plataforma in lista_plataformas:
# #             if self.rectangulo_colision_suelo.colliderect(plataforma.rectangulo_colision_suelo):
# #                 retorno = True
# #                 self.rectangulo.y = plataforma.rectangulo.y - self.rectangulo.h  # Ajusta la posición del jugador al nivel de la plataforma
# #                 break
# #         return retorno




        


#     def do_animation(self, delta_ms):
#         self.tiempo_transcurrido_animacion += delta_ms
#         if self.tiempo_transcurrido_animacion > 100:
#             self.tiempo_transcurrido_animacion = 0
#             if self.frame < len(self.animation) - 1:
#                 self.frame += 1
#             else:
#                 self.frame = 0

#             if self.frame >= len(self.animation):
#                 self.frame = len(self.animation) - 1



        


   
#     def shoot_objeto(self):
#         self.rock.add(throw_rock(self.rect.center,-8,self.rect.bottom,self.direction))


#     def recharge(self):
#         if not self.ready_for_shoot:
#             current_time = pygame.time.get_ticks()
#             if current_time - self.shoot_time >= self.shoot_cooldown:
#                 self.ready_for_shoot = True


#     #CORDENAS RECTANGULOS
#     def add_x(self,delta_x):
#         self.rect.x += delta_x
#         self.trap_collition.x += delta_x
    
#     def add_y(self,delta_y):
#         self.rect.y += delta_y
#         self.trap_collition.y += delta_y



#     def update_sprites(self):
#         if self.move_x != 0:
                
#             if self.direction == DIRECCION_L:
#                 self.animation = self.walk_l
#             else:                  
#                 self.animation = self.walk_r

                    



        

#     def update(self,delta_ms,object):

#         self.update_sprites()
  
   
        

#     def draw(self,screen):
#         if(DEBUG):
#             pygame.draw.rect(screen,RED,self.rect)
#             pygame.draw.rect(screen,BLUE,self.trap_collition)
#             self.rock.draw(screen)

        

        
#         screen.blit(self.image,self.rect)
from player import *
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/1 Pink_Monster/Pink_Monster_Run_6.png",1,6,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/1 Pink_Monster/Pink_Monster_Run_6.png",1,6,flip=True,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png",1,6,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/1 Pink_Monster/Pink_Monster_Idle_4.png",1,6,flip=True,scale=p_scale)

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECCION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = 0
        self.ground_collition_rect.y = y + self.rect.height - 0

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y



    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0

    def update(self,delta_ms,plataform_list):

        self.do_animation(delta_ms) 

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.lives -= 1
