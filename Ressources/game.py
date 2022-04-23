import pygame
pygame.init()
from .variables import Black,White, grid

class Game():
    def __init__(self, n_rows, n_cols):
        self.display_surface = pygame.display.get_surface()
        self.w = self.display_surface.get_width()
        self.h = self.display_surface.get_height()
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.rows = (self.display_surface.get_height()//self.n_rows) #+1 if self.n_rows is not a multiple of the height
        self.cols = (self.display_surface.get_width()//self.n_cols)


    def draw_grid(self):
        self.display_surface.fill(White)
        for row in range(self.n_rows):
            pygame.draw.line(self.display_surface, Black, (0,row*self.rows), (self.w, row*self.rows))

        for col in range(self.n_cols):
            pygame.draw.line(self.display_surface, Black, (col*self.cols,0), (col*self.cols,self.h))


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    Rect = pygame.Rect(col*self.cols, row*self.rows, self.rows, self.cols)
                    pygame.draw.rect(self.display_surface, Black, Rect)
