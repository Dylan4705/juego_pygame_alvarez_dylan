import pygame 
import sys
from constantes import *
from player import Player
from plataformas import *
from enemigo import Enemy
from rock import throw_rock
from trampas import *
from botin import Botin    
from decoracion import *
from meta import meta_
from main import main
from ventana_emergente import *












        


screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
gane = False
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE + "locations/fondoestatico.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

font_path = "images\hud\Pixelfy Variable.ttf"
font_size = 40
font = pygame.font.Font(font_path, font_size)
pygame.init()

marco_1_rect = pygame.Rect(700, 200, 90, 90)
marco_2_rect = pygame.Rect(850, 200, 90, 90)
marco_3_rect = pygame.Rect(1000, 200, 90, 90)

def draw(screen,background,player,objects,offset_x,rock,enemy_list,botin_list,decoration_list,score_text,delta_ms,floor,meta,time_limit):

    screen.blit(background,background.get_rect())

    for obj in objects:
        obj.draw(screen,offset_x)

    player.update(delta_ms, floor, screen,enemy_list)
    player.draw(screen)

    contador_enemigos = 0
    for enemy in enemy_list:
        
        enemy.draw(screen)
        enemy.update(player,rock,enemy_list,contador_enemigos,screen)
        
        contador_enemigos +=1

    meta.update(player,enemy_list)
    meta.draw(screen)

    contador_botin = 0
    for botin in botin_list:
        botin.draw(screen)
        botin.update(player,botin_list,contador_botin)
        contador_botin +=1
        
    

    for decoration in decoration_list:
        decoration.draw(screen)

    if player.is_paused:
        marco_1_rect,marco_2_rect,marco_3_rect,score = ventana(screen,player,time_limit)

    screen.blit(score_text, (165, 0))
    
    pygame.display.update()




def nivel_1_():

    player = Player(player=0, x=-6, y=654, speed_walk=7, speed_run=10, gravity=20, max_limit=ANCHO_VENTANA, p_scale=1)

    enemy_list = []
    botin_list = []
    decoration_list = []
    floor = []

    enemy_list.append(Enemy( 2,x=382, y=550, move_x=-5, speed=2, limit_x_start=0, limit_x_end= 50, p_scale=1.5))
    enemy_list.append(Enemy( 1,x=1582, y=350, move_x=-5, speed=4, limit_x_start=0, limit_x_end= 96, p_scale=1.5))
    enemy_list.append(Enemy( 4,x=954, y=90, move_x=5, speed=2, limit_x_start=0, limit_x_end=300,shoot_interval=3000, p_scale=2))
    enemy_list.append(Enemy( 3,x=614, y=550, move_x=5, speed=2, limit_x_start=0, limit_x_end=60, p_scale=1.5))


    botin_list.append(Botin(type_botin= 1,x= 644,y=510,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 406,y=510,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 906,y=510,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 1148,y=460,p_scale=3))
    botin_list.append(Botin(type_botin= 1,x= 800,y=680,p_scale=3))
    botin_list.append(Botin(type_botin= 1,x= 1342,y=90,p_scale=3))

    # Crear objetos de Decoracion y agregarlos a decoration_list
    decoration_list.append(BackgroundObject(number=31,x=50,y=666,width=100,height=100)) 
    decoration_list.append(BackgroundObject(number=33,x=750,y=666,width=100,height=100)) 
    decoration_list.append(BackgroundObject(number=22,x=150,y=656,width=100,height=100)) 
    decoration_list.append(BackgroundObject(number=134,x=256,y=203,width=50,height=50)) 
    decoration_list.append(BackgroundObject(number=135,x=256,y=255,width=50,height=50)) 
    decoration_list.append(BackgroundObject(number=136,x=203,y=255,width=50,height=50)) 
    decoration_list.append(BackgroundObject(number=137,x=309,y=255,width=50,height=50)) 
    decoration_list.append(BackgroundObject(number=67,x=409,y=255,width=50,height=50)) 
    # Agregar más objetos de Decoracion si es necesario

    meta = meta_(x=-6,y=658,p_scale=1)


    

    niveles = {"Plataformas":[

                            Trap(574,750-13,1,screen),
                            Trap(622,750-13,1,screen),
                            Trap(670,750-13,1,screen),
                            Trap(1102,750-13,1,screen),
                            Trap(1150,750-13,1,screen),
                            Trap(1198,750-13,1,screen),
                            
                            #PLATAFORMAS
                            # Plataforma 1, primer salto
                            Block(382,600,48,16*19,16*13), 
                            Block(430,600,48,16*28,16*13),

                            # Plataforma 2, primer salto
                            Block(858,600,48,16*19,16*13), 
                            Block(906,600,48,16*19,16*10),
                            Block(954,600,48,16*28,16*13),

                        #Plataforma 3,segundo salto
                            Block(1342,500,48,16*19,16*13),
                            Block(1390,500,48,16*28,16*13),

                            #Plataforma 3,segundo salto
                            Block(1582,400,48,16*19,16*13), 
                            Block(1630,400,48,16*19,16*10),
                            Block(1678,400,48,16*28,16*13),


                            Block(1294,250,48,16*19,16*13), 
                            Block(1342,250,48,16*16,16*10),
                            Block(1390,250,48,16*28,16*13),

                            # Block(1582,750,48,16*19,16*10),
                            # Block(1630,750,48,16*19,16*10),
                            # Block(1678,750,48,16*19,16*10),

                            




                    
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


    


    

  




    offset_x = 0
    for plataforma in niveles["Plataformas"]:
        plataformas = [plataforma]
        floor.extend(plataformas)

    

    time_limit = 60
    elapsed_time = 0
    finally_time = 0
        #------------------------------------------
    while True:



        delta_ms = clock.tick(FPS)


        elapsed_time += delta_ms / 1000  # Convertir delta_ms a segundos y agregarlo al tiempo transcurrido

        if player.is_win or time_limit == 0 or player.is_paused == True:
            finally_time = time_limit  # Guardar el tiempo restante en la variable finally_time

                
            if time_limit == 0:
                player.is_dead = True
        else:
            # Actualizar el cronómetro
            elapsed_time += delta_ms / 1000  # Convertir delta_ms a segundos y agregarlo al tiempo transcurrido

            if elapsed_time >= 1:
                time_limit -= 1
                elapsed_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if player.is_paused:
                        if marco_1_rect.collidepoint(event.pos):
                            main(player.is_win,False)
                        if marco_2_rect.collidepoint(event.pos):
                            nivel_1_()
                        if marco_3_rect.collidepoint(event.pos):
                            player.is_paused = False


            if event.type == pygame.KEYDOWN:
                if player.is_dead == False and player.is_paused == False:
                    if event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()
                if event.key == pygame.K_ESCAPE:
                    player.pause()
                if event.key == pygame.K_r:
                    nivel_1_()
                else:
                    pass

        player.get_input()
    
        text = font.render("Score: " + str(player.score)+ "    Time: "+str(time_limit), True, (0, 0, 0))

        draw(screen,imagen_fondo,player,floor,offset_x,player.rock,enemy_list,botin_list,decoration_list,text,delta_ms,floor,meta,time_limit)




        if player.invulnerable:
                current_time = pygame.time.get_ticks()
                if current_time - player.invulnerable_timer >= player.invulnerable_duration:
                    player.invulnerable = False  # Finalizar la invulnerabilidad si ha pasado el tiempo




        #player update --
        #enemigos update 
        #player dibujarlo
        #dibujar todo el nivel


        #------------------------------------------