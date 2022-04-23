import pygame
pygame.init()
from .variables import White

class Game():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.w = self.display_surface.get_width()
        self.h = self.display_surface.get_height()
        self.rows = self.display_surface.get_height()//20
        self.cols = self.display_surface.get_width()//20


    def create_grid(self):
        self.display_surface.fill(White)
        for row in range(self.rows):
            pygame.draw.line(self.display_surface, color, row*, end_pos)
