from board import Board
from way import Way
import pygame

class Lines(Board):
    def __init__(self, n, m, sz, win, margin=1, grid_color=(255, 255, 255)):
        super().__init__(n, m, sz, win, margin=margin, grid_color=grid_color)
        self.arr = []
        for i in range(n):
            self.arr.append([])
            for j in range(m):
                self.arr[-1].append(0)

    def get_color(self, x, y):
        return [[0, 0, 0], [0, 0, 255], [255, 0, 0]][self.arr[x][y]]

    def upd_used(self):
        self.used = []
        for i in range(self.n):
            self.used.append([])
            for j in range(self.m):
                self.used[-1].append(0)

    def has_path(self, x1, y1, x2, y2, first_call=True):
        ways = []

        if first_call:
            self.upd_used()

        if x1 not in range(0, self.n) or y1 not in range(self.m) or self.used[x1][y1]:
            return False

        self.draw_cell(x1, y1, (111, 111, 111))

        if self.arr[x1][y1] != 0 and not first_call:
            return False

        self.used[x1][y1] = True

        if x1 == x2 and y1 == y2:
            return Way([[x1, y1]])

        w = [-1, 0, 1]
        for add_i in w:
            for add_j in w:
                if add_i == 0 or add_j == 0:
                    way = self.has_path(x1 + add_i, y1 + add_j, x2, y2, first_call=False)
                    if way:
                        ways.append(way)
        if not len(ways):
            return False
        ways.sort(key=lambda x: x.len)
        for i in ways:
            print(i)
        print()
        ways[0].append(x1, y1)
        return ways[0]

    def show(self):
        self.draw_grid()
        for i in range(self.n):
            for j in range(self.m):
                self.show_i_j(i, j)
        pygame.display.update()

    def draw_way(self, way):
        print(way)
        """
        for i in range(1, len(way)):
            self.draw_cell(*(way[i]), (0, 0, 255))
            self.draw_cell(*(way[i - 1]), (0, 0, 0))"""



    def click(self, x=None, y=None):
        global move

        if x is None:
            x, y = pygame.mouse.get_pos()
            x //= self.sz
            y //= self.sz

        move = False

        if self.arr[x][y] == 0:
            for i in range(self.n):
                for j in range(self.m):
                    if self.arr[i][j] == 2:
                        way = self.has_path(i, j, x, y)
                        if way:
                            self.draw_way(way)
                            self.arr[i][j] = 0
                            self.arr[x][y] = 1
                            move = True
        if not move:
            self.arr[x][y] = (self.arr[x][y] + 1) % 3

    def show_i_j(self, x, y):
        self.draw_cell(x, y, self.get_color(x, y))