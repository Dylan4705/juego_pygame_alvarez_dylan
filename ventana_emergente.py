import pygame
from constantes import *
from player import Player

font_path = "images\hud\Pixelfy Variable.ttf"
font_size = 40
font = pygame.font.Font(font_path, font_size)

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