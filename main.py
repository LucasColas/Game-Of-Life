import pygame
from Ressources.variables import Width, Height
from Ressources.game import Game
pygame.init()


Win = pygame.display.set_mode((Width, Height))

clock = pygame.time.Clock()

def main():

    run = True
    FPS = 60
    new_Game = Game()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        new_Game.create_grid()

        pygame.display.update()
        clock.tick(FPS)
main()
