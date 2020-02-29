import pygame
from random import randrange as rd
from lines import Lines


if __name__ == '__main__':
    SZ = 600
    FPS = 60

    pygame.init()
    win = pygame.display.set_mode((SZ, SZ))

    lines = Lines(SZ // 50, SZ // 50, 50, win)
    clock = pygame.time.Clock()

    while True:
        lines.show()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                lines.click()
        clock.tick(FPS)

