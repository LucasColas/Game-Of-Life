import pygame
from Ressources.variables import *
from Ressources.game import Game
import time
pygame.init()


Win = pygame.display.set_mode((Width, Height))

clock = pygame.time.Clock()

def main():

    run = True
    FPS = 60
    new_Game = Game(n_rows,n_cols)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        new_Game.draw_grid(grid)
        time.sleep(2)
        new_Game.update_grid(grid)

        pygame.display.update()
        clock.tick(FPS)
main()
