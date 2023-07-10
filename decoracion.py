import pygame
from constantes import *
from auxiliar import Auxiliar

class BackgroundObject:
    def __init__(self, number, x, y, width, height):
        self.number = number
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Cargar la imagen según el número proporcionado
        image_path = f"images\\locations\\decoracion fotoxfoto\\object ({self.number}).png"
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        # Redimensionar la imagen al tamaño deseado
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        screen.blit(self.image, (self.x, self.y))