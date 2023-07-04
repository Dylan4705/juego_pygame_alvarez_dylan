import pygame
from constantes import * 
from auxiliar import Auxiliar




class trap(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height, name="Trap"):
                super().__init__()
                self.rect = pygame.Rect(x, y, width, height)
                self.image = pygame.Surface((width, height), pygame.SRCALPHA)
                self.width = width
                self.height = height
                self.name = name

        def draw(self, screen, offset_x):
            if(DEBUG):
                pygame.draw.rect(screen,GREEN,self.rect)
            screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))
            
        



#304, 160
def get_block(type=1):
        if(type == 1):
                path = "images/locations/Nature_environment_01.png"
                image = pygame.image.load(path).convert_alpha()
                surface = pygame.Surface((46,25), pygame.SRCALPHA,32)
                rect = pygame.Rect(353,336,46,25)
                surface.blit(image, (0,0),rect)
                return surface




class Trap(trap):
        def __init__(self,x,y,type,screen):
                super().__init__(x,y,46,25)
                block = get_block(type)
                self.image.blit(block, (0,0))
                self.mask = pygame.mask.from_surface(self.image)
                
