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

def get_clicked_pos(pos, Width, Height, n_rows, n_cols):

    gap_Width = Width//n_cols
    gap_Height = Height//n_rows
    row = pos[1]//gap_Height
    col = pos[0]//gap_Width
    print(row, col)
    return row, col

def main():

    run = True
    FPS = 60

    n_rows_entered = False
    n_rows = ''
    n_cols = ''
    n_cols_entered = False
    created = False
    started = False

    while run:
        #print(nb)
        Win.fill(White)
        if not n_rows_entered:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        n_rows = n_rows[:-1]
                        print(n_rows)

                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        n_rows_entered = True
                    else:
                        #print(event.unicode, type(event.unicode))
                        if event.unicode >= '0' and event.unicode <= '9':
                            n_rows += event.unicode
                            print(n_rows)
            #nb = int(nb)
            pygame.draw.rect(Win, (0,250,0), input_rect, 2)
            text = font.render(n_rows, True, (Black))
            text2 = font.render("n_rows : ", True, (Black))
            Win.blit(text2, (input_rect.x, input_rect.y - (font.size("n_rows : ")[1] + 7)))
            Win.blit(text, (input_rect.x + 5, input_rect.y+5))

        elif not n_cols_entered:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        n_cols = n_cols[:-1]
                        print(n_cols)

                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        n_cols_entered = True

                    else:
                        #print(event.unicode, type(event.unicode))
                        if event.unicode >= '0' and event.unicode <= '9':
                            n_cols += event.unicode
                            print(n_cols)
            #nb = int(nb)
            pygame.draw.rect(Win, (0,250,0), input_rect, 2)
            text = font.render(n_cols, True, (Black))
            text2 = font.render("n_cols : ", True, (Black))
            Win.blit(text2, (input_rect.x, input_rect.y - (font.size("n_cols : ")[1] + 7)))
            Win.blit(text, (input_rect.x + 5, input_rect.y+5))


        else:
            if not created:
                new_Game = Game(int(n_rows),int(n_cols))
                created = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

                if started:
                    #new_Game.update_grid()
                    new_Game.draw_grid()
                    continue

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, Width, Height, int(n_rows),int(n_cols))
                    new_Game.grid[row][col] = 1 if new_Game.grid[row][col] == 0 else 0

                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        started = True
            new_Game.draw_grid()



        pygame.display.update()
        clock.tick(FPS)

main()
