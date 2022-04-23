import pygame
pygame.init()
from .variables import Black,White

class Game():
    def __init__(self, n_rows, n_cols):
        self.display_surface = pygame.display.get_surface()
        self.w = self.display_surface.get_width()
        self.h = self.display_surface.get_height()
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.rows = self.display_surface.get_height()//self.n_rows
        self.cols = self.display_surface.get_width()//self.n_cols


    def create_grid(self):
        self.display_surface.fill(White)
        for row in range(self.n_rows+1):
            if row == self.n_rows:

                print(self.rows/self.n_rows,row, self.rows,self.rows*row)
            pygame.draw.line(self.display_surface, Black, (0,row*self.rows), (self.w, row*self.rows))

        for col in range(self.n_cols):
            pygame.draw.line(self.display_surface, Black, (col*self.cols,0), (col*self.cols,self.h))
