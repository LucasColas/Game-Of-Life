import pygame
pygame.init()
from .variables import Black,White

class Game():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.w = self.display_surface.get_width()
        self.h = self.display_surface.get_height()
        self.rows = self.display_surface.get_height()//20
        self.cols = self.display_surface.get_width()//20


    def create_grid(self):
        self.display_surface.fill(White)
        for row in range(20):
            pygame.draw.line(self.display_surface, Black, (0,row*self.rows), (self.w, row*self.rows))

        for col in range(20):
            pygame.draw.line(self.display_surface, Black, (col*self.cols,0), (col*self.cols,self.h))
