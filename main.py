import pygame 
import sys
from constantes import *
from player import Player
from plataformas import *
from enemigo import Enemy
from rock import throw_rock
from trampas import *
    

def draw(screen,background,player,objects,offset_x):

    screen.blit(background,background.get_rect())

    for obj in objects:
        obj.draw(screen,offset_x)

    player.update(delta_ms,floor)
    player.draw(screen)
    enemy.update(delta_ms,floor)
    enemy.draw(screen)
    

    
    pygame.display.update()






if __name__ == '__main__':
        

    pygame.init()
    screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    player = Player(player=0,x=580,y=500,speed_walk=7,speed_run=10,gravity=20,max_limit=ANCHO_VENTANA,p_scale=1)
    enemy = Enemy(x=500,y=500,speed_walk=5,speed_run= 5,gravity=5,jump_power=5,frame_rate_ms=60,move_rate_ms=60,jump_height= 5,p_scale= 1,interval_time_jump= 100)
    clock = pygame.time.Clock()

    niveles = {"Plataformas":[Trap(-2,750-13,1,screen),
                            Trap(46,750-13,1,screen),
                            Trap(94,750-13,1,screen),
                            Trap(142,750-13,1,screen),
                            Trap(190,750-13,1,screen),
                            Trap(238,750-13,1,screen),
                            Trap(286,750-13,1,screen),
                            Trap(334,750-13,1,screen),
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
                            Block(-2,750,48,304,160),
                            Block(46,750,48,304,160),
                            Block(94,750,48,304,160),
                            Block(142,750,48,304,160),
                            Block(190,750,48,304,160),
                            Block(238,750,48,304,160),
                            Block(286,750,48,304,160),
                            Block(334,750,48,304,160),
                            Block(382,750,48,304,160),
                            Block(430,750,48,304,160),
                            Block(478,750,48,304,160),
                            Block(526,750,48,304,160),
                            Block(574,750,48,304,160),
                            Block(622,750,48,304,160),
                            Block(670,750,48,304,160),
                            Block(718,750,48,304,160),
                            Block(766,750,48,304,160),
                            Block(814,750,48,304,160),
                            Block(862,750,48,304,160),
                            Block(910,750,48,304,160),
                            Block(958,750,48,304,160),
                            Block(1006,750,48,304,160),
                            Block(1054,750,48,304,160),
                            Block(1102,750,48,304,160),
                            Block(1150,750,48,304,160),
                            Block(1198,750,48,304,160),
                            Block(1246,750,48,304,160),
                            Block(1294,750,48,304,160),
                            Block(1342,750,48,304,160),
                            Block(1390,750,48,304,160),
                            Block(1438,750,48,304,160),
                            Block(1486,750,48,304,160),
                            Block(1534,750,48,304,160),
                            Block(1582,750,48,304,160),
                            Block(1630,750,48,304,160),
                            Block(1678,750,48,304,160),
                            Block(1726,750,48,304,160),
                            Block(1774,750,48,304,160),
                            Block(1822,750,48,304,160),
                            Block(600,600,48,304,160)]}

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

        player.get_input(floor.count)
    
    
        draw(screen,imagen_fondo,player,floor,offset_x)
        
			
        #player update --
        #enemigos update 
        #player dibujarlo
        #dibujar todo el nivel


    #------------------------------------------