import pygame
from constantes import *


# Dimensiones de la ventana


# Inicializar Pygame
pygame.init()
pygame.display.set_caption("Ingrese Nivel")


fondo = pygame.image.load(r"gui\jungle\menu\bg.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

marco = pygame.image.load(r"gui\jungle\level_select\table2.png")
marco = pygame.transform.scale(marco, (1000, 500))  # Ajusta el tamaño de la imagen según sea necesario
marco_rect = marco.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))

marco_1_image = pygame.image.load(r"gui\jungle\pause\bg.png")
marco_1_image = pygame.transform.scale(marco_1_image, (100, 100))
marco_1_rect = pygame.Rect(570, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario



marco_2_image = pygame.image.load(r"gui\jungle\pause\bg.png")
marco_2_image = pygame.transform.scale(marco_2_image, (100, 100))
marco_2_rect = pygame.Rect(820, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario
bloqued_lvl2 = pygame.image.load(r"gui\jungle\level_select\lock.png")
bloqued_lvl2 = pygame.transform.scale(bloqued_lvl2, (50, 50))


marco_3_image = pygame.image.load(r"gui\jungle\pause\bg.png")
marco_3_image = pygame.transform.scale(marco_3_image, (100, 100))
marco_3_rect = pygame.Rect(1070, 300, 90, 90)  # Ajusta las coordenadas y el tamaño según sea necesario
bloqued_lvl3 = pygame.image.load(r"gui\jungle\level_select\lock.png")
bloqued_lvl3 = pygame.transform.scale(bloqued_lvl3, (50, 50))

        

nivel_1_numero = pygame.image.load(r"gui\jungle\bubble\1.png")
nivel_2_numero = pygame.image.load(r"gui\jungle\bubble\2.png")
nivel_3_numero = pygame.image.load(r"gui\jungle\bubble\3.png")

# Ajustar el tamaño de las imágenes según sea necesario
nivel_1_numero = pygame.transform.scale(nivel_1_numero, (35, 70))
nivel_1_rect = pygame.Rect(570+30, 315, 90, 90)
nivel_2_numero = pygame.transform.scale(nivel_2_numero, (70, 70))
nivel_2_rect = pygame.Rect(820+15, 315, 90, 90)
nivel_3_numero = pygame.transform.scale(nivel_3_numero, (70, 70))
nivel_3_rect = pygame.Rect(1070+ 15, 315, 90, 90)



def main(player_is_win_lvl1,player_is_win_lvl2):
    # Lógica del juego
    from nivel1 import nivel_1_
    from nivel2 import nivel_2_
    from nivel3 import nivel_3
    running = True
    current_level = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if nivel_1_rect.collidepoint(event.pos):
                    current_level = 1
                elif nivel_2_rect.collidepoint(event.pos):
                    current_level = 2
                elif nivel_3_rect.collidepoint(event.pos):
                    current_level = 3



        

        
        if current_level == 1:
            nivel_1_()
        elif current_level == 2 and player_is_win_lvl1 == True:
            nivel_2_()
        elif current_level == 3 and player_is_win_lvl2 == True:
            nivel_3()
        # Añade más niveles según sea necesario

        SCREEN.blit(fondo, (0, 0))
        SCREEN.blit(marco, marco_rect)
        SCREEN.blit(marco_1_image, marco_1_rect)
        SCREEN.blit(marco_2_image, marco_2_rect)
        SCREEN.blit(marco_3_image, marco_3_rect)
        SCREEN.blit(nivel_1_numero, nivel_1_rect)
        SCREEN.blit(nivel_2_numero, nivel_2_rect)
        SCREEN.blit(nivel_3_numero, nivel_3_rect)
        if player_is_win_lvl1 == False:
            SCREEN.blit(bloqued_lvl2, (845, 370))
        if player_is_win_lvl2 == False:
            SCREEN.blit(bloqued_lvl3, (1100, 370))
        pygame.display.flip()  # Actualizar la pantalla en cada iteración del bucle

    pygame.quit()

if __name__ == "__main__":
    main(False,False)


