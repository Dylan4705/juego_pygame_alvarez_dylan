import pygame 
import sys
from constantes import *
from player import Player
from plataformas import *
from enemigo import Enemy
from rock import throw_rock
from trampas import *
from botin import Botin    

def draw(screen,background,player,objects,offset_x,rock,enemy_list,botin_list):

    screen.blit(background,background.get_rect())

    for obj in objects:
        obj.draw(screen,offset_x)

    player.update(delta_ms, floor, screen)
    player.draw(screen)

    contador_enemigos = 0
    for enemy in enemy_list:
        
        enemy.draw(screen)
        enemy.update(player,rock,enemy_list,contador_enemigos)
        contador_enemigos +=1

    contador_botin = 0
    for botin in botin_list:
        
        botin.draw(screen)
        botin.update(player,botin_list,contador_botin)
        contador_botin +=1
        
    
    

    
    pygame.display.update()






if __name__ == '__main__':
        

    pygame.init()
    enemy_list = []
    botin_list = []
    screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    player = Player(player=0, x=50, y=50, speed_walk=7, speed_run=10, gravity=20, max_limit=ANCHO_VENTANA, p_scale=1)
    enemy_list.append(Enemy( 1,x=700, y=550, move_x=5, speed=2, limit_x_start=0, limit_x_end=100, p_scale=1.5))
    enemy_list.append(Enemy( 1,x=700, y=300, move_x=-5, speed=2, limit_x_start=-100, limit_x_end=0, p_scale=1.5))
    enemy_list.append(Enemy( 1,x=700, y=200, move_x=-5, speed=2, limit_x_start=-100, limit_x_end=0, p_scale=1.5))
    enemy_list.append(Enemy( 2,x=300, y=700, move_x=-5, speed=3, limit_x_start=-100, limit_x_end=0, p_scale=1.5))
    botin_list.append(Botin(x= 50,y=50,p_scale=3))
    clock = pygame.time.Clock()
    rock = player.rock

    niveles = {"Plataformas":[
                            Trap(382,750-13,1,screen),
                            Trap(430,750-13,1,screen),
                            Trap(478,750-13,1,screen),
                            Trap(526,750-13,1,screen),
                            Trap(574,750-13,1,screen),
                            Trap(622,750-13,1,screen),
                            Trap(670,750-13,1,screen),
                            Trap(718,750-13,1,screen),
                            Trap(766,750-13,1,screen),
                            Trap(814,750-13,1,screen),
                            Trap(862,750-13,1,screen),
                            Trap(910,750-13,1,screen),
                            Trap(958,750-13,1,screen),
                            Trap(1006,750-13,1,screen),
                            Trap(1054,750-13,1,screen),
                            Trap(1102,750-13,1,screen),
                            Trap(1150,750-13,1,screen),
                            Trap(1198,750-13,1,screen),
                            Trap(1246,750-13,1,screen),
                            Trap(1294,750-13,1,screen),
                            Trap(1342,750-13,1,screen),
                            Trap(1390,750-13,1,screen),
                            Trap(1438,750-13,1,screen),
                            Trap(1486,750-13,1,screen),
                            Trap(1534,750-13,1,screen),
                            Trap(1582,750-13,1,screen),
                            Trap(1630,750-13,1,screen),
                            Trap(1678,750-13,1,screen),
                            Trap(1726,750-13,1,screen),
                            Trap(1774,750-13,1,screen),
                            Trap(1822,750-13,1,screen), 
                            #PLATAFORMAS
                            # Plataforma 1, primer salto
                            Block(286,600,48,16*13,16*13), 
                            Block(334,600,48,16*34,16*13),

                            # Plataforma 1, primer salto
                            Block(286*3,600,48,16*13,16*13), 
                            Block(286*3+48,600,48,16*19,16*10),
                            Block(286*3+(48*2),600,48,16*34,16*13),



                             




                      
                            Block(-2,750,48,16*10,16*10),
                            Block(46,750,48,16*19,16*10),
                            Block(94,750,48,16*19,16*10),
                            Block(142,750,48,16*19,16*10),
                            Block(190,750,48,16*19,16*10),
                            Block(238,750,48,16*19,16*10),
                            Block(286,750,48,16*19,16*10),
                            Block(334,750,48,16*19,16*10),
                            Block(382,750,48,16*19,16*10),
                            Block(430,750,48,16*19,16*10),
                            Block(478,750,48,16*19,16*10),
                            Block(526,750,48,16*19,16*10),
                            Block(574,750,48,16*19,16*10),
                            Block(622,750,48,16*19,16*10),
                            Block(670,750,48,16*19,16*10),
                            Block(718,750,48,16*19,16*10),
                            Block(766,750,48,16*19,16*10),
                            Block(814,750,48,16*19,16*10),
                            Block(862,750,48,16*19,16*10),
                            Block(910,750,48,16*19,16*10),
                            Block(958,750,48,16*19,16*10),
                            Block(1006,750,48,16*19,16*10),
                            Block(1054,750,48,16*19,16*10),
                            Block(1102,750,48,16*19,16*10),
                            Block(1150,750,48,16*19,16*10),
                            Block(1198,750,48,16*19,16*10),
                            Block(1246,750,48,16*19,16*10),
                            Block(1294,750,48,16*19,16*10),
                            Block(1342,750,48,16*19,16*10),
                            Block(1390,750,48,16*19,16*10),
                            Block(1438,750,48,16*19,16*10),
                            Block(1486,750,48,16*19,16*10),
                            Block(1534,750,48,16*19,16*10),
                            Block(1582,750,48,16*19,16*10),
                            Block(1630,750,48,16*19,16*10),
                            Block(1678,750,48,16*19,16*10),
                            Block(1726,750,48,16*19,16*10),
                            Block(1774,750,48,16*19,16*10),
                            Block(1822,750,48,16*19,16*10)
                            ]
                            }

    imagen_fondo = pygame.image.load(PATH_IMAGE + "locations/fondoestatico.jpg")
    imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))




    offset_x = 0
  
    floor = []

   


    for plataforma in niveles["Plataformas"]:
        plataformas = [plataforma]
        floor.extend(plataformas)

    

  
    #------------------------------------------
    while True:


        delta_ms = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jump_count < 2:
                    player.jump()

        player.get_input()
    
    
        draw(screen,imagen_fondo,player,floor,offset_x,player.rock,enemy_list,botin_list)
        
        if player.invulnerable:
                current_time = pygame.time.get_ticks()
                if current_time - player.invulnerable_timer >= player.invulnerable_duration:
                    player.invulnerable = False  # Finalizar la invulnerabilidad si ha pasado el tiempo

		
        #player update --
        #enemigos update 
        #player dibujarlo
        #dibujar todo el nivel


    #------------------------------------------