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
from plataformas_moviles import *











        


screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
gane = False
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE + "background\origbig.png")
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
        obj.update(player)

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




def nivel_2_():
    player = Player(player=0, x=-6, y=50, speed_walk=7, speed_run=10, gravity=20, max_limit=ANCHO_VENTANA, p_scale=1)

    enemy_list = []
    botin_list = []
    decoration_list = []
    floor = []
 

    #ENEMIGOS
    enemy_list.append(Enemy( 2,x=286,y= 100, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 250, p_scale=1.5))
    enemy_list.append(Enemy( 5,x=4000,y= 20, move_x=5, speed=8, limit_x_start=-4100, limit_x_end= 0, p_scale=1.5))
    enemy_list.append(Enemy( 3,x=-200,y= 50, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 1700, p_scale=1.5))
    enemy_list.append(Enemy( 3,x=-200,y= 90, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 1700, p_scale=1.5))
    enemy_list.append(Enemy( 3,x=0,y= 500, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 280, p_scale=1.5))
    enemy_list.append(Enemy( 1,x=0,y= 700, move_x=-5, speed=10, limit_x_start=0, limit_x_end= 1400, p_scale=1.5))






    botin_list.append(Botin(type_botin= 3,x= 1500,y=100,p_scale=2))
    botin_list.append(Botin(type_botin= 2,x= 729,y=60,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 379,y=60,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 1010,y=60,p_scale=3))
    botin_list.append(Botin(type_botin= 1,x= 1650,y=115,p_scale=3))
    botin_list.append(Botin(type_botin= 1,x= 1342,y=255,p_scale=3))
    botin_list.append(Botin(type_botin= 1,x= 958,y=255,p_scale=3))
    botin_list.append(Botin(type_botin= 1,x= 575,y=255,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 140,y=440,p_scale=3))

    botin_list.append(Botin(type_botin= 2,x= 729,y=700,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 379,y=700,p_scale=3))
    botin_list.append(Botin(type_botin= 2,x= 1010,y=700,p_scale=3))

    decoration_list.append(BackgroundObject(number=31,x=860,y=666,width=100,height=100)) 
    decoration_list.append(BackgroundObject(number=33,x=350,y=666,width=100,height=100)) 
    decoration_list.append(BackgroundObject(number=22,x=55,y=56,width=100,height=100)) 

    decoration_list.append(BackgroundObject(number=41,x=100,y=650,width=100,height=100)) 
    decoration_list.append(BackgroundObject(number=24,x=74,y=518,width=150,height=150)) 
    decoration_list.append(BackgroundObject(number=27,x=74,y=640,width=50,height=50)) 
    decoration_list.append(BackgroundObject(number=27,x=174,y=670,width=50,height=50)) 

            # decoration_list.append(BackgroundObject(number=135,x=256,y=255,width=50,height=50)) 
            # decoration_list.append(BackgroundObject(number=136,x=203,y=255,width=50,height=50)) 
            # decoration_list.append(BackgroundObject(number=137,x=309,y=255,width=50,height=50)) 
            # decoration_list.append(BackgroundObject(number=67,x=409,y=255,width=50,height=50)) 


    meta = meta_(x=1700,y=658,p_scale=1)


    

    niveles = {"Plataformas":[

                            #PISO 1
                            Trap(238,150-13,1,screen),
                            Trap(574,150-13,1,screen),
                            Trap(622,150-13,1,screen),
                            Trap(862,150-13,1,screen),
                            Trap(910,150-13,1,screen),
                            Trap(1150,150-13,1,screen),
                            Trap(1198,150-13,1,screen),
                            Trap(1246,150-13,1,screen),
                            Block(-2,150,48,16*19,16*13),
                            Block(46,150,48,16*19,16*10),
                            Block(94,150,48,16*19,16*10),
                            Block(142,150,48,16*19,16*10),
                            Block(190,150,48,16*19,16*10),
                            Block(238,150,48,16*19,16*10),
                            Block(286,150,48,16*19,16*10),
                            Block(334,150,48,16*19,16*10),
                            Block(382,150,48,16*19,16*10),
                            Block(430,150,48,16*19,16*10),
                            Block(478,150,48,16*19,16*10),
                            Block(526,150,48,16*19,16*10),
                            Block(574,150,48,16*19,16*10),
                            Block(622,150,48,16*19,16*10),
                            Block(670,150,48,16*19,16*10),
                            Block(718,150,48,16*19,16*10),
                            Block(766,150,48,16*19,16*10),
                            Block(814,150,48,16*19,16*10),
                            Block(862,150,48,16*19,16*10),
                            Block(910,150,48,16*19,16*10),
                            Block(958,150,48,16*19,16*10),
                            Block(1006,150,48,16*19,16*10),
                            Block(1054,150,48,16*19,16*10),
                            Block(1102,150,48,16*19,16*10),
                            Block(1150,150,48,16*19,16*10),
                            Block(1198,150,48,16*19,16*10),
                            Block(1246,150,48,16*19,16*10),
                            Block(1294,150,48,16*19,16*10),
                            Block(1342,150,48,16*19,16*10),
                            Block(1390,150,48,16*19,16*10),
                            Block(1438,150,48,16*19,16*10),
                            Block(1486,150,48,16*19,16*10),
                            Block(1534,150,48,16*19,16*10),
                            Block(1534,150,48,16*28,16*13),
                            

                            #PISO 1.5
                            Block(-2,198,48,16*16,16*19),
                            Block(46,198,48,16*37,16*16),
                            Block(94,198,48,16*37,16*16),
                            Block(142,198,48,16*37,16*16),
                            Block(190,198,48,16*37,16*16),
                            Block(238,198,48,16*37,16*16),
                            Block(286,198,48,16*37,16*16),
                            Block(334,198,48,16*37,16*16),
                            Block(382,198,48,16*37,16*16),
                            Block(430,198,48,16*37,16*16),
                            Block(478,198,48,16*37,16*16),
                            Block(526,198,48,16*37,16*16),
                            Block(574,198,48,16*37,16*16),
                            Block(622,198,48,16*37,16*16),
                            Block(670,198,48,16*37,16*16),
                            Block(718,198,48,16*37,16*16),
                            Block(766,198,48,16*37,16*16),
                            Block(814,198,48,16*37,16*16),
                            Block(862,198,48,16*37,16*16),
                            Block(910,198,48,16*37,16*16),
                            Block(958,198,48,16*37,16*16),
                            Block(1006,198,48,16*37,16*16),
                            Block(1054,198,48,16*37,16*16),
                            Block(1102,198,48,16*37,16*16),
                            Block(1150,198,48,16*37,16*16),
                            Block(1198,198,48,16*37,16*16),
                            Block(1246,198,48,16*37,16*16),
                            Block(1294,198,48,16*37,16*16),
                            Block(1342,198,48,16*37,16*16),
                            Block(1390,198,48,16*37,16*16),
                            Block(1438,198,48,16*37,16*16),
                            Block(1486,198,48,16*37,16*16),
                            Block(1534,198,48,16*13,16*19),
 

                            #PISO 2(pinches)
                            Trap(334,500-14,1,screen),
                            Trap(382,500-14,1,screen),
                            Trap(430,500-14,1,screen),
                            Trap(478,500-14,1,screen),
                            Trap(526,500-14,1,screen),
                            Trap(574,500-14,1,screen),
                            Trap(622,500-14,1,screen),
                            Trap(670,500-14,1,screen),
                            Trap(718,500-14,1,screen),
                            Trap(766,500-14,1,screen),
                            Trap(814,500-14,1,screen),
                            Trap(862,500-14,1,screen),
                            Trap(910,500-14,1,screen),
                            Trap(958,500-14,1,screen),
                            Trap(1006,500-14,1,screen),
                            Trap(1054,500-14,1,screen),
                            Trap(1102,500-14,1,screen),
                            Trap(1150,500-14,1,screen),
                            Trap(1198,500-14,1,screen),
                            Trap(1246,500-14,1,screen),
                            Trap(1294,500-14,1,screen),
                            Trap(1342,500-14,1,screen),
                            Trap(1390,500-14,1,screen),
                            Trap(1438,500-14,1,screen),
                            Trap(1486,500-14,1,screen),
                            Trap(1534,500-14,1,screen),
                            Trap(1582,500-14,1,screen),
                            Trap(1630,500-14,1,screen),
                            Trap(1678,500-14,1,screen),
                            Trap(1726,500-14,1,screen),
                            Trap(1774,500-14,1,screen),
                            Trap(1822,500-14,1,screen),
                            #PISO 2.5                          
                            Block(334,500,48,16*16,16*19),
                            Block(382,500,48,16*37,16*16),
                            Block(430,500,48,16*37,16*16),
                            Block(478,500,48,16*37,16*16),
                            Block(526,500,48,16*37,16*16),
                            Block(574,500,48,16*37,16*16),
                            Block(622,500,48,16*37,16*16),
                            Block(670,500,48,16*37,16*16),
                            Block(718,500,48,16*37,16*16),
                            Block(766,500,48,16*37,16*16),
                            Block(814,500,48,16*37,16*16),
                            Block(862,500,48,16*37,16*16),
                            Block(910,500,48,16*37,16*16),
                            Block(958,500,48,16*37,16*16),
                            Block(1006,500,48,16*37,16*16),
                            Block(1054,500,48,16*37,16*16),
                            Block(1102,500,48,16*37,16*16),
                            Block(1150,500,48,16*37,16*16),
                            Block(1198,500,48,16*37,16*16),
                            Block(1246,500,48,16*37,16*16),
                            Block(1294,500,48,16*37,16*16),
                            Block(1342,500,48,16*37,16*16),
                            Block(1390,500,48,16*37,16*16),
                            Block(1438,500,48,16*37,16*16),
                            Block(1486,500,48,16*37,16*16),
                            Block(1534,500,48,16*37,16*16),
                            Block(1582,500,48,16*37,16*16),
                            Block(1630,500,48,16*37,16*16),
                            Block(1678,500,48,16*37,16*16),
                            Block(1726,500,48,16*37,16*16),
                            Block(1774,500,48,16*37,16*16),
                            Block(1822,500,48,16*37,16*16),
                            platform_movile(image_number=45,x=1678,y=440,width=144,height=48,limit_x_start=334,limit_x_end=2000,speed=-4,player=player),
                            Block(575,390,48,16*25,16*19),
                            Trap(575,410,1,screen),
                            Block(958,390,48,16*25,16*19),
                            Trap(958,410,1,screen),
                            Block(1342,390,48,16*25,16*19),
                            Trap(1342,410,1,screen),
                            #TECHO
                            Block(-2,-50,48,16*19,16*13),
                            Block(46,-50,48,16*19,16*10),
                            Block(94,-50,48,16*19,16*10),
                            Block(142,-50,48,16*19,16*10),
                            Block(190,-50,48,16*19,16*10),
                            Block(238,-50,48,16*19,16*10),
                            Block(286,-50,48,16*19,16*10),
                            Block(334,-50,48,16*19,16*10),
                            Block(382,-50,48,16*19,16*10),
                            Block(430,-50,48,16*19,16*10),
                            Block(478,-50,48,16*19,16*10),
                            Block(526,-50,48,16*19,16*10),
                            Block(574,-50,48,16*19,16*10),
                            Block(622,-50,48,16*19,16*10),
                            Block(670,-50,48,16*19,16*10),
                            Block(718,-50,48,16*19,16*10),
                            Block(766,-50,48,16*19,16*10),
                            Block(814,-50,48,16*19,16*10),
                            Block(862,-50,48,16*19,16*10),
                            Block(910,-50,48,16*19,16*10),
                            Block(958,-50,48,16*19,16*10),
                            Block(1006,-50,48,16*19,16*10),
                            Block(1054,-50,48,16*19,16*10),
                            Block(1102,-50,48,16*19,16*10),
                            Block(1150,-50,48,16*19,16*10),
                            Block(1198,-50,48,16*19,16*10),
                            Block(1246,-50,48,16*19,16*10),
                            Block(1294,-50,48,16*19,16*10),
                            Block(1342,-50,48,16*19,16*10),
                            Block(1390,-50,48,16*19,16*10),
                            Block(1438,-50,48,16*19,16*10),
                            Block(1486,-50,48,16*19,16*10),
                            Block(1534,-50,48,16*19,16*10),
                            Block(1534,-50,48,16*19,16*10),
                            Block(1582,-50,48,16*19,16*10),
                            Block(1630,-50,48,16*19,16*10),
                            Block(1678,-50,48,16*19,16*10),
                            Block(1726,-50,48,16*19,16*10),
                            Block(1774,-50,48,16*19,16*10),
                            Block(1822,-50,48,16*19,16*10),

                            




                            #PISO
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

    

    time_limit = 300
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
                            if player.is_win == True:
                                main(True,True)
                            else:
                                main(True,False)
                        if marco_2_rect.collidepoint(event.pos):
                            nivel_2_()
                        if marco_3_rect.collidepoint(event.pos):
                            player.is_paused = False


            if event.type == pygame.KEYDOWN:
                if player.is_dead == False and player.is_paused == False:
                    if event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()
                if event.key == pygame.K_ESCAPE:
                    player.pause()
                if event.key == pygame.K_y:
                    DEBUG = not DEBUG
                if event.key == pygame.K_r:
                    nivel_2_()
                else:
                    pass

        player.get_input()
    
        text = font.render("Score: " + str(player.score)+ "    Time: "+str(time_limit), True, (0, 0, 0))

        draw(screen,imagen_fondo,player,floor,offset_x,player.rock,enemy_list,botin_list,decoration_list,text,delta_ms,floor,meta,time_limit)




        if player.invulnerable:
                current_time = pygame.time.get_ticks()
                if current_time - player.invulnerable_timer >= player.invulnerable_duration:
                    player.invulnerable = False  # Finalizar la invulnerabilidad si ha pasado el tiempo


        



        #------------------------------------------