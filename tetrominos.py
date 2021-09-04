import random, pygame

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapearr = [I, J, L, O, T, S, Z]


def checkboardright(board, x, y, num):
    flag = 1
    for i in range(4):
        if board[y[i]][x[i] + num] > 0:
            return False
    return True


def checkboardleft(board, x, y, num):
    flag = 1
    for i in range(4):
        if board[y[i]][x[i] - num] > 0:
            return False
    return True


def generate(level, type):
    t1 = tetrominos()
    t1.nextblock = random.randint(0, 6)  # [0-I block,  1-J block, 2-L block, 3-O Block, 4-T, 5-S, 6-Z ]
    if type != -1:
        t1.type = type
    else:
        t1.type = random.randint(0, 6)
    t1.rotation = 0
    t1.cooldown = 200 - (level * 2)
    t1.last = pygame.time.get_ticks()
    t1.x, t1.y = gen_tet(t1.type)
    return t1


def gen_tet(type):
    x = [0] * 4
    y = [0] * 4
    index = 0
    for i in range(5):
        for j, str in enumerate(shapearr[type][0][i]):
            if str == "0":
                x[index] = j + 4
                y[index] = i - 2
                index += 1
    return x, y


def scanarray(type, rotation, bottomest, leftest):
    x = [0] * 4
    y = [0] * 4
    index = 0
    for i in range(5):
        for j, str in enumerate(shapearr[type][rotation][i]):
            if str == "0":
                x[index] = j + leftest - 1 
                y[index] = bottomest + i - 2
                index += 1
    return x, y


# noinspection SpellCheckingInspection
class tetrominos:
    type = 0
    rotation = 0
    x = [3] * 4
    y = [0] * 4
    last = 0
    cooldown = 200
    nextblock = 0

    def minusY(self):
        for i in range(4):
            self.y[i] -= 1

    def minusX(self, board):
        flag = 1
        for j in range(4):
            if board[self.y[j]][self.x[j] - 1] > 0:
                flag = 0
        if flag == 1:
            for i in range(4):
                self.x[i] -= 1

    def plusX(self, board):
        flag = 1
        for j in range(4):
            if board[self.y[j]][self.x[j] + 1] > 0:
                flag = 0
        if flag == 1:
            for i in range(4):
                self.x[i] += 1

    def bottomest_block(self):
        return max(self.y)

    def leftest_block(self):
        return min(self.x)

    def rightest_block(self):
        return max(self.x)

    def define(self, board, rotation, x, y):
        flag = 1
        for i in range(4):
            if y[i] not in range(0, 18):
                for j in range(4):
                    y[j] -= 1
        if max(x) > 9 and checkboardleft(board, x, y, max(x) - 9):
            num = max(x) - 9
            for j in range(4):
                x[j] -= num
        elif min(x) < 0 and checkboardright(board, x, y, 0 - min(x)):
            num = 0 - min(x)
            for j in range(4):
                x[j] -= num
        for i in range(4):
            if x[i] not in range(0, 10) or board[y[i]][x[i]] > 0:
                flag = 0
        if flag == 1:
            self.rotation = rotation
            self.x = x
            self.y = y

    def rotate(self, board):
        if self.type == 1 or self.type == 2 or self.type == 4:
            x, y = scanarray(self.type, (self.rotation + 1) % 4, self.bottomest_block(), self.leftest_block())
            self.define(board, (self.rotation + 1) % 4, x, y)
        elif self.type != 3:
            x, y = scanarray(self.type, (self.rotation + 1) % 2, self.bottomest_block(), self.leftest_block())
            self.define(board, (self.rotation + 1) % 2, x, y)
