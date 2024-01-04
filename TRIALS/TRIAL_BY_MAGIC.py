import copy
import random


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell(self.FREE_CELL) for j in range(3)) for i in range(3))

        self.free_cells = []
        for i in range(3):
            for j in range(3):
                if bool(self.pole[i][j]):
                    self.free_cells.append([i, j])

    def __getitem__(self, item):
        r, c = item
        if not all(isinstance(x, int) for x in [r, c]) or not (0 <= r <= 2 and 0 <= c <= 2):
            raise IndexError('некорректно указанные индексы')
        if isinstance(item, tuple):
            return self.pole[r][c].value
        elif isinstance(r, int) or isinstance(c, int):
            return self.pole[r][c]

    def __setitem__(self, key, value):
        r, c = key
        if not all(isinstance(x, int) for x in [r, c]) or not (0 <= r <= 2 and 0 <= c <= 2):
            raise IndexError('некорректно указанные индексы')

        temp = [list(i) for i in self.pole]
        temp[r][c] = Cell(value)
        self.pole = copy.deepcopy(temp)

        self.free_cells = []
        for i in range(3):
            for j in range(3):
                if bool(self.pole[i][j]):
                    self.free_cells.append([i, j])

    def init(self):
        self.pole = tuple(tuple(Cell(self.FREE_CELL) for j in range(3)) for i in range(3))

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value, end=' ')
            print()

    def human_go(self, cell):
        r, c = cell
        if not all(isinstance(x, int) for x in [r, c]) or not (0 <= r <= 2 and 0 <= c <= 2):
            raise IndexError('некорректно указанные индексы')

        self.free_cells = []
        for i in range(3):
            for j in range(3):
                if bool(self.pole[i][j]):
                    self.free_cells.append([i, j])

        temp = [list(i) for i in self.pole]

        if cell in self.free_cells:
            temp[r][c] = Cell(self.HUMAN_X)
        else:
            print('Busy')

        self.pole = copy.deepcopy(temp)

    def computer_go(self):
        cell = [random.randint(0, 2) for i in range(2)]
        index = 0
        for i in range(float('inf')):
            r, c = cell
            if index > len(self.free_cells):
                index = 0
            if bool(self.pole[r][c]) and cell in self.free_cells:
                temp = [list(i) for i in self.pole]
                temp[r][c] = Cell(self.COMPUTER_O)
                self.pole = copy.deepcopy(temp)
                break
            else:
                cell = [random.randint(0, 2) for i in range(2)]

    @property
    def is_human_win(self):
        if bool(self):
            return self.human_win
        else:
            return False

    @property
    def is_computer_win(self):
        if bool(self):
            return self.computer_win
        else:
            return False

    @property
    def is_draw(self):
        if bool(self):
            return self.draw

    def __bool__(self):
        self.human_win = False
        self.computer_win = False
        self.draw = False
        left = []
        right = []
        rows = []
        cols = []

        for i in range(3):
            left.append(self.pole[i][i].value)
            right.append(self.pole[i][-i - 1].value)

        for row in self.pole:
            rows.append([cell.value for cell in row])

        for i in range(len(self.pole)):
            column = [row[i].value for row in self.pole]
            cols.append(column)

        if all(x == 1 for x in left) or all(x == 1 for x in right) or all(x == 1 for x in rows) or all(
                x == 1 for x in cols):
            self.human_win = True
            return True
        elif any(all(x == 2 for x in column) for column in cols) or \
                any(all(x == 2 for x in row) for row in rows) or \
                all(x == 2 for x in left) or \
                all(x == 2 for x in right):
            self.computer_win = True
            return True
        else:
            self.draw = False
            return True


class Cell:

    def __init__(self, value=0):
        self.value = value

    def __bool__(self):
        return True if self.value == 0 else False


a = TicTacToe()

a.init()


for i in range(9):
    r, c = list(map(int, input().split()))
    a.human_go([r, c])
    a.computer_go()
    if a.is_human_win:
        print('You won')
    elif a.is_computer_win:
        print("You've been beaten by a computer")
    a.show()

