import itertools
import random


class Cell:
    def __init__(self, around_mines: int, mine: int):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.pole = [[Cell(around_mines=0, mine=0) for _ in range(self.N)] for _ in range(self.N)]

    def init(self):
        coordinates = list(itertools.product(range(self.N), repeat=2))
        for y_x in random.sample(coordinates, self.M):
            self.pole[y_x[0]][y_x[1]].mine = 1

        direct = ([[-1, -1], [-1, 0], [0, -1], [-1, 1], [1, -1], [1, 0], [0, 1], [1, 1]])
        for y in range(self.N):
            for x in range(self.N):
                if not self.pole[y][x].mine:
                    for x_dir, y_dir in direct:
                        x_temp = x + x_dir
                        y_temp = y + y_dir
                        if x_temp in range(self.N) and y_temp in range(self.N):
                            self.pole[y][x].around_mines += self.pole[y_temp][x_temp].mine

    def show(self):
        for y in range(self.N):
            for x in range(self.N):
                if not self.pole[y][x].fl_open:
                    print('#', end='  ')
                elif self.pole[y][x].mine:
                    print('*', end='  ')
                elif self.pole[y][x].around_mines:
                    print(self.pole[y][x].around_mines, end='  ')
                else:
                    print(' ', end='  ')
            print()
        return ''


pole_game = GamePole(10, 12)
pole_game.init()
print(pole_game.show())
