import pygame
pygame.init()

class Game():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()


    def create_grid(self):
        self.display_surface.fill(White)
        
