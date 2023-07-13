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






def nivel_1_():



    niveles = cargar_niveles_desde_json("data_niveles.json")

    enemy_list = []
    enemy_list.append(Enemy( 2,x=382, y=550, move_x=-5, speed=2, limit_x_start=0, limit_x_end= 50, p_scale=1.5))
    enemy_list.append(Enemy( 1,x=1582, y=350, move_x=-5, speed=4, limit_x_start=0, limit_x_end= 96, p_scale=1.5))
    enemy_list.append(Enemy( 4,x=954, y=90, move_x=5, speed=2, limit_x_start=0, limit_x_end=300,shoot_interval=3000, p_scale=2))
    enemy_list.append(Enemy( 3,x=614, y=550, move_x=5, speed=2, limit_x_start=0, limit_x_end=60, p_scale=1.5))


    player = niveles["nivel1"]["player"]


    meta = meta_(x=-6,y=658,p_scale=1)


    

   
    

  




    offset_x = 0
    # for plataforma in niveles["nivel1"]["plataformas"]:
    #     plataformas = [plataforma]
    #     floor.extend(plataformas)

    # for decoracion in niveles["nivel1"]["decoraciones"]:
    #     decoraciones = [decoracion]
    #     decoration_list.extend(decoraciones)

    # for botin in niveles["nivel1"]["botin"]:
    #     botines = [botin]
    #     botin_list.extend(botines)


    

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
                        jump_sound = pygame.mixer.Sound("sounds\jump.wav")
                        jump_sound.play()
                if event.key == pygame.K_ESCAPE:
                    player.pause()
                if event.key == pygame.K_r:
                    nivel_1_()
                else:
                    pass

        player.get_input()
    
        text = font.render("Score: " + str(player.score)+ "    Time: "+str(time_limit), True, (0, 0, 0))

        draw(SCREEN,imagen_fondo,player,niveles["nivel1"]["plataformas"],offset_x,player.rock,enemy_list,niveles["nivel1"]["botin"],niveles["nivel1"]["decoraciones"],text,delta_ms,niveles["nivel1"]["plataformas"],meta,time_limit)




        if player.invulnerable:
                current_time = pygame.time.get_ticks()
                if current_time - player.invulnerable_timer >= player.invulnerable_duration:
                    player.invulnerable = False  # Finalizar la invulnerabilidad si ha pasado el tiempo




        #player update --
        #enemigos update 
        #player dibujarlo
        #dibujar todo el nivel


        #------------------------------------------