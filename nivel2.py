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
from funciones import *
from plataformas_moviles import *











        



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


def nivel_2_():

    niveles = cargar_niveles_desde_json("data_niveles.json")
    player = niveles["nivel2"]["player"]
    
    

    plataformas = []
    for plataforma in niveles["nivel2"]["plataformas"]:
        plataformas.append(plataforma)

    plataformas.append(platform_movile(x=1678,y=440,width=144,height=48,limit_x_start=334,limit_x_end=2000,speed=-4,player=player),)
    
    enemy_list = []
    
   
    enemy_list.append(Enemy( 2,x=286,y= 100, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 250, p_scale=1.5))
    enemy_list.append(Enemy( 5,x=4000,y= 20, move_x=5, speed=8, limit_x_start=-4100, limit_x_end= 0, p_scale=1.5))
    enemy_list.append(Enemy( 3,x=-200,y= 50, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 1700, p_scale=1.5))
    enemy_list.append(Enemy( 3,x=-200,y= 90, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 1700, p_scale=1.5))
    enemy_list.append(Enemy( 3,x=0,y= 500, move_x=-5, speed=5, limit_x_start=0, limit_x_end= 280, p_scale=1.5))
    enemy_list.append(Enemy( 1,x=0,y= 700, move_x=-5, speed=10, limit_x_start=0, limit_x_end= 1400, p_scale=1.5))


    meta = meta_(x=1700,y=658,p_scale=1)


    offset_x = 0

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
                        jump_sound = pygame.mixer.Sound("sounds\jump.wav")
                        jump_sound.play()
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

        draw(SCREEN,imagen_fondo,player,plataformas,offset_x,player.rock,enemy_list,niveles["nivel2"]["botin"],niveles["nivel2"]["decoraciones"],text,delta_ms,plataformas,meta,time_limit)




        if player.invulnerable:
                current_time = pygame.time.get_ticks()
                if current_time - player.invulnerable_timer >= player.invulnerable_duration:
                    player.invulnerable = False  # Finalizar la invulnerabilidad si ha pasado el tiempo


        



        #------------------------------------------