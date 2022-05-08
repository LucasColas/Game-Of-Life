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
    nb_entered = False
    nb = ''

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

            if not nb_entered:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        nb = nb[:-1]

                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        nb_entered = True
                    else:
                        nb += event.unicode




        new_Game.draw_grid(grid)
        #time.sleep(1)
        new_Game.update_grid(grid)

        pygame.display.update()
        clock.tick(FPS)
main()
