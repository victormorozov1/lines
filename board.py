import pygame


class Board:
    def __init__(self, n, m, sz, win, margin=1, grid_color=(255, 255, 255)):
        self.n = n
        self.m = m
        self.sz = sz
        self.margin = margin
        self.grid_color = grid_color
        self.win = win
        self.SZX = self.sz * n
        self.SZY = self.sz * m

    def draw_cell(self, i, j, color=(0, 0, 0)):
        pygame.draw.circle(self.win, color, (i * self.sz + self.sz // 2, j * self.sz + self.sz // 2), self.sz // 2 - 4)

    def draw_grid(self):
        pygame.draw.rect(self.win, self.grid_color, (0, 0, self.SZX, self.SZY))
        for i in range(self.n):
            for j in range(self.m):
                pygame.draw.rect(self.win, (0, 0, 0), [i * self.sz, j * self.sz, self.sz, self.sz])
                pygame.draw.rect(self.win, (255, 255, 255), [i * self.sz, j * self.sz, self.sz, self.sz], self.margin)

    def show(self):
        self.draw_grid()
        for i in range(self.n):
            for j in range(self.m):
                self.draw_cell(i, j)
        pygame.display.update()
