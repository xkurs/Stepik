import itertools
import random


class Cell:
    def __init__(self, around_mines: int, mine: bool):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.pole = [[Cell(around_mines=0, mine=False) for _ in range(self.N)] for _ in range(self.N)]

    def init(self):
        coordinates = list(itertools.product(range(self.N), repeat=2))
        for x_y in random.sample(coordinates, self.M):
            self.pole[x_y[0]][x_y[1]].mine = True
        self.get_around_mines()

    def get_around_mines(self):
        for i in range(self.N):
            for j in range(self.N):
                self.pole[i][j].around_mines += 1

    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].fl_open:
                    print('#', end='  ')
                elif self.pole[i][j].mine:
                    print('*', end='  ')
                elif self.pole[i][j].around_mines:
                    print(self.pole[i][j].around_mines, end='  ')
                else:
                    print(' ', end='  ')
            print()
        return ''


pole_game = GamePole(10, 12)
pole_game.init()
print(pole_game.show())
