import pygame 
import sys
from constantes import *
from player import Player
from plataformas import *
from enemigo import Enemy
from rock import throw_rock
from trampas import *

screen = 0
niveles = {"nivel1":{"Plataformas":[Trap(-2,750-13,1,screen),
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
                            Block(-2,800,48,304,160),
                            Block(46,800,48,304,160),
                            Block(94,800,48,304,160),
                            Block(142,800,48,304,160),
                            Block(190,800,48,304,160),
                            Block(238,800,48,304,160),
                            Block(286,800,48,304,160),
                            Block(334,800,48,304,160),
                            Block(382,800,48,304,160),
                            Block(430,800,48,304,160),
                            Block(478,800,48,304,160),
                            Block(526,800,48,304,160),
                            Block(574,800,48,304,160),
                            Block(622,800,48,304,160),
                            Block(670,800,48,304,160),
                            Block(718,800,48,304,160),
                            Block(766,800,48,304,160),
                            Block(814,800,48,304,160),
                            Block(862,800,48,304,160),
                            Block(910,800,48,304,160),
                            Block(958,800,48,304,160),
                            Block(1006,800,48,304,160),
                            Block(1054,800,48,304,160),
                            Block(1102,800,48,304,160),
                            Block(1150,800,48,304,160),
                            Block(1198,800,48,304,160),
                            Block(1246,800,48,304,160),
                            Block(1294,800,48,304,160),
                            Block(1342,800,48,304,160),
                            Block(1390,800,48,304,160),
                            Block(1438,800,48,304,160),
                            Block(1486,800,48,304,160),
                            Block(1534,800,48,304,160),
                            Block(1582,800,48,304,160),
                            Block(1630,800,48,304,160),
                            Block(1678,800,48,304,160),
                            Block(1726,800,48,304,160),
                            Block(1774,800,48,304,160),
                            Block(1822,800,48,304,160)]}}

    #    anchura = -50
    # while anchura < ANCHO_VENTANA:
    #     anchura += 48
    #     spikes = [Trap(anchura,750-13,1,screen,,304,160)]
        
    #     print("Trap({0},750-13,1,screen),".format(anchura))
        
    #     floor.extend(spikes)
    # floor.extend(blocks)
