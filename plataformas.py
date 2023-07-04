import pygame
from constantes import * 
from auxiliar import Auxiliar




class Platform(pygame.sprite.Sprite):
#         def __init__(self,x,y,w,h,type=0,on_off=True) -> None:
#                 self.image = Auxiliar.getSurfaceFromSeparateFiles(path_format="images/locations/Nature_environment_01_foto_por_foto/tile{}.png",from_index=1,quantity=128)[type]
#                 self.image = pygame.transform.scale(self.image,(w,h))
#                 self.image = self.image.convert_alpha()
#                 self.rect = self.image.get_rect()
#                 self.rect.x= x
#                 self.rect.y = y
#                 if(type != 105 and on_off == True):
#                         self.rect_ground_collition = pygame.Rect(self.rect.x ,self.rect.y,self.rect.w, 10)
#                 elif(on_off == True):
#                         self.rect_ground_collition = pygame.Rect(self.rect.x,self.rect.y+32,self.rect.w,10)
#                 else: 
#                         self.rect_ground_collition = pygame.Rect(0,0,0,0)
                

#         def draw(self,screen):
#                 if(DEBUG):

#                         pygame.draw.rect(screen,RED,self.rect)

#                 screen.blit(self.image,self.rect)


#                 if(DEBUG):

#                         pygame.draw.rect(screen,GREEN,self.rect_ground_collition)


        def __init__(self, x, y, width, height, name=None):
                super().__init__()
                self.rect = pygame.Rect(x, y, width, height)
                self.image = pygame.Surface((width, height), pygame.SRCALPHA)
                self.width = width
                self.height = height
                self.name = name

        def draw(self, screen, offset_x):
            screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))




#304, 160
def get_block(size,pos_x_in_img,pos_y_in_img):
        path = "images/locations/Nature_environment_01.png"
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size,size), pygame.SRCALPHA,32)
        rect = pygame.Rect(pos_x_in_img,pos_y_in_img,size,size)
        surface.blit(image, (0,0),rect)
        return surface




class Block(Platform):
        def __init__(self, x, y, size,pos_x_in_img, pos_y_in_img):
                super().__init__(x,y,size,size)
                block = get_block(size,pos_x_in_img,pos_y_in_img)
                self.image.blit(block, (0,0))
                self.mask = pygame.mask.from_surface(self.image)



