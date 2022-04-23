import pygame

pygame.init()

Width, Height = 1500, 700
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
