import pygame
from constantes import *
import json
from player import Player
from plataformas import *
from enemigo import Enemy
from rock import throw_rock
from trampas import *
from botin import Botin    
from decoracion import *
from plataformas_moviles import *

font_path = "images\hud\Pixelfy Variable.ttf"
font_size = 40
font = pygame.font.Font(font_path, font_size)
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))


def ventana(screen,player,time_limit):
    marco = pygame.image.load(r"gui\jungle\level_select\table2.png")
    marco = pygame.transform.scale(marco, (600, 500))  # Ajusta el tamaño de la imagen según sea necesario
    marco_rect = marco.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

    marco_1_image = pygame.image.load(r"gui\jungle\menu\prize.png")
    marco_1_image = pygame.transform.scale(marco_1_image, (100, 100))
    marco_1_rect = pygame.Rect(700, 200, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    marco_2_image = pygame.image.load(r"gui\jungle\btn\restart.png")
    marco_2_image = pygame.transform.scale(marco_2_image, (100, 100))
    marco_2_rect = pygame.Rect(850, 200, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario


    marco_3_image = pygame.image.load(r"gui\jungle\menu\play.png")
    marco_3_image = pygame.transform.scale(marco_3_image, (100, 100))
    marco_3_rect = pygame.Rect(1000, 200, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario

    you_win_image = pygame.image.load(r"gui\jungle\you_win\header.png")
    you_win_image = pygame.transform.scale(you_win_image, (400, 100))
    you_lose_image = pygame.image.load(r"gui\jungle\you_lose\header.png")
    you_lose_image = pygame.transform.scale(you_lose_image, (400, 100))
    you_pause = pygame.image.load(r"gui\jungle\pause\header.png")
    you_pause = pygame.transform.scale(you_pause, (400, 100))
    you_score_bar = pygame.image.load(r"gui\jungle\load_bar\2.png")
    you_score_bar = pygame.transform.scale(you_score_bar,(600,40))


    screen.blit(marco, marco_rect)
    screen.blit(marco_1_image, marco_1_rect)
    screen.blit(marco_2_image, marco_2_rect)

    if not player.is_dead and player.is_win == False:
        screen.blit(marco_3_image, marco_3_rect)
        screen.blit(you_pause, (690, 100))
    elif player.is_dead == True:
        screen.blit(you_lose_image, (690, 100))
        
    score = 0
    if player.is_win:
        score = player.score * time_limit
        text = font.render("Your level Score: " + str(score), True, (0, 0, 0))
        screen.blit(you_win_image, (690, 100))
        screen.blit(you_score_bar,(600,500))
        screen.blit(text, (730, 500))


    return marco_1_rect,marco_2_rect,marco_3_rect,score



def crear_objeto_desde_string(objeto_str):
    clase, *args = objeto_str.split("(")
    args = [arg.strip(")").strip() for arg in args]

    args = args[0]
    args = args.split(",")
    print(args)


    if clase == "Trap":
        x, y, type, screen = [eval(arg) for arg in args]
        objeto = Trap(x,y,type,screen)

    elif clase == "Block":

        x,y,size,pos_x_in_img,pos_y_in_img = [eval(arg) for arg in args]
        objeto = Block(x,y,size,pos_x_in_img,pos_y_in_img)

    # elif clase == "Enemy":
        
    #     enemy,x,y,move_x,speed,limit_x_start,limit_x_end,shoot_interval,p_scale = [eval(arg) for arg in args]
    #     objeto = Enemy(enemy,x,y,move_x,speed,limit_x_start,limit_x_end,shoot_interval,p_scale)

    elif clase == "BackgroundObject":
        number,x,y,width,height = [eval(arg) for arg in args]
        objeto = BackgroundObject(number,x,y,width,height)

    elif clase == "Botin":
        type_botin,x,y,p_scale = [eval(arg) for arg in args]
        objeto = Botin(type_botin,x,y,p_scale)
    
    elif clase == "Player":
        player,x,y,speed_walk,speed_run,gravity,max_limit,p_scale = [eval(arg) for arg in args]
        objeto = Player(player,x,y,speed_walk,speed_run,gravity,max_limit,p_scale)
        

    return objeto

def cargar_niveles_desde_json(nombre_archivo):
    with open(nombre_archivo, "r") as json_file:
        data = json.load(json_file)

    niveles = {}

    for nivel, nivel_data in data.items():
        plataformas = []
        enemigos = []
        decoraciones = []
        botines = []

        for plataforma_str in nivel_data["plataformas"]:
            plataforma = crear_objeto_desde_string(plataforma_str)
            plataformas.append(plataforma)

        # for enemigo_str in nivel_data["enemigos"]:
        #     enemigo = crear_objeto_desde_string(enemigo_str)
        #     enemigos.append(enemigo)
        
        for decoracion_str in nivel_data["decoraciones"]:
            decoracion = crear_objeto_desde_string(decoracion_str)
            decoraciones.append(decoracion)
    
        for botin_str in nivel_data["botin"]:
            botin = crear_objeto_desde_string(botin_str)
            botines.append(botin)

        for player_str in nivel_data["player"]:
            player = crear_objeto_desde_string(player_str)


        niveles[nivel] = {
            "plataformas": plataformas,
            # "enemigos": enemigos,
            "decoraciones": decoraciones,
            "botin": botines,
            "player": player
        }

    return niveles






def draw(screen,background,player,objects,offset_x,rock,enemy_list,botin_list,decoration_list,score_text,delta_ms,floor,meta,time_limit):

    screen.blit(background,background.get_rect())

    for obj in objects:
        obj.draw(screen,offset_x)
        if isinstance(obj, platform_movile):
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



