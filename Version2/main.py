import pygame
from Ressources.variables import *
from Ressources.game import Game
import time
pygame.init()

pygame.display.set_caption('Game Of Life')
Win = pygame.display.set_mode((Width, Height))
input_rect = pygame.Rect((Width//2)-75, (Height//2)-16, 140, 32)
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

def main():

    run = True
    FPS = 60
    new_Game = Game(n_rows,n_cols)
    row_entered = False
    row = ''
    col = ''
    col_entered = False

    while run:
        #print(nb)
        Win.fill(White)
        if not row_entered:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        row = row[:-1]
                        print(row)

                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        row_entered = True
                    else:
                        #print(event.unicode, type(event.unicode))
                        if event.unicode >= '0' and event.unicode <= '9':
                            row += event.unicode
                            print(row)
            #nb = int(nb)
            pygame.draw.rect(Win, (0,250,0), input_rect, 2)
            text = font.render(row, True, (Black))
            text2 = font.render("Row : ", True, (Black))
            Win.blit(text2, (input_rect.x, input_rect.y - (font.size("Row : ")[1] + 7)))
            Win.blit(text, (input_rect.x + 5, input_rect.y+5))

        elif not col_entered:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        col = col[:-1]
                        print(col)

                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        col_entered = True

                    else:
                        #print(event.unicode, type(event.unicode))
                        if event.unicode >= '0' and event.unicode <= '9':
                            col += event.unicode
                            print(col)
            #nb = int(nb)
            pygame.draw.rect(Win, (0,250,0), input_rect, 2)
            text = font.render(col, True, (Black))
            text2 = font.render("Col : ", True, (Black))
            Win.blit(text2, (input_rect.x, input_rect.y - (font.size("Col : ")[1] + 7)))
            Win.blit(text, (input_rect.x + 5, input_rect.y+5))


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

            new_Game.draw_grid(grid)
            #time.sleep(1)
            new_Game.update_grid(grid)

        pygame.display.update()
        clock.tick(FPS)

main()
