import pygame
import time
from .variables import Black,White

pygame.init()

class Game():
    def __init__(self, n_rows, n_cols):
        self.display_surface = pygame.display.get_surface()
        self.w = self.display_surface.get_width()
        self.h = self.display_surface.get_height()
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.row = self.create_cell(1)
        self.col = self.create_cell(0)
        self.grid = self.create_grid(self.n_rows, self.n_cols)
        self.default_grid = self.default_grid()

        #print(self.grid)
    def create_cell(self, type):
        if type:
            if self.n_rows%self.h != 0:
                return (self.h//self.n_rows)+1  #+1 if self.n_rows is not a multiple of the height
            else:
                return (self.h//self.n_rows)

        else:
            if self.n_cols%self.w != 0:
                return (self.w//self.n_cols)+1
            else:
                return (self.w//self.n_cols)


    def create_grid(self, n_rows, n_cols):
        return [[0 for i in range(n_rows)] for j in range(n_cols)]
    def default_grid(self):
        """
        self.grid[30][30] = 1
        self.grid[30][36] = 1
        self.grid[31][32] = 1
        self.grid[32][32] = 1

        self.grid[33][31] = 1
        self.grid[33][33] = 1

        self.grid[31][36] = 1
        self.grid[32][35] = 1
        self.grid[32][37] = 1

        """
        self.grid[41][40] = 1


        self.grid[1][2] = 1
        self.grid[2][1] = 1
        self.grid[2][1] = 1


        self.grid[20][4] = 1
        self.grid[20][6] = 1
        self.grid[21][5] = 1
        self.grid[22][4] = 1
        self.grid[21][6] = 1

        self.grid[31][10] = 1
        self.grid[33][10] = 1
        self.grid[33][9] = 1
        self.grid[33][11] = 1
        self.grid[34][10] = 1

    def draw_grid(self):
        self.display_surface.fill(White)
        for row in range(self.n_rows):
            pygame.draw.line(self.display_surface, Black, (0,row*self.row), (self.w, row*self.row))

        for col in range(self.n_cols):
            pygame.draw.line(self.display_surface, Black, (col*self.col,0), (col*self.col,self.h))

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col]:
                    Rect = pygame.Rect(col*self.col, row*self.row, self.row, self.col)
                    pygame.draw.rect(self.display_surface, Black, Rect)


    def update_grid(self):
        #print("in update")
        def countNeighbors(r,c):
            nei = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):

                    if ((i == r and j == c) or i < 0 or j < 0 or
                        i == len(self.grid) or j == len(self.grid[0])):
                        continue

                    if self.grid[i][j] in [1,3]:
                        nei += 1

            #print("nei : ", nei)
            return nei

        for r in range(self.n_rows):

            for c in range(self.n_cols):
                nei = countNeighbors(r,c)
                if self.grid[r][c]:
                    if nei in [2,3]:
                        print("self grid ",self.grid[r][c])
                        self.grid[r][c] = 3
                        print("self grid : ", self.grid[r][c])
                elif nei == 3:
                    print("self grid in nei",self.grid[r][c])
                    self.grid[r][c] = 2
                    print("self grid : ",self.grid[r][c])

        #print(self.grid)
        for r in range(self.n_rows):

            for c in range(self.n_cols):

                if self.grid[r][c] == 1:
                    print("cell dead", self.grid[r][c])
                    self.grid[r][c] = 0
                    print("cell dead", self.grid[r][c])
                elif self.grid[r][c] in [2,3]:
                    self.grid[r][c] = 1

        time.sleep(0.4)
