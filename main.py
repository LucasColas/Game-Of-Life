import pygame
from Ressources.variables import Width, Height
pygame.init()


Win = pygame.display.set_mode((Width, Height))

clock = pygame.time.Clock()

def main():

    run = True
    FPS = 60

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
main()
