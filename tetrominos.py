import random,pygame


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
    t1.x, t1.y = generate_tetro(t1.type)
    return t1



def generate_tetro(type):
    x = [4] * 4
    y = [0] * 4
    if type == 0:
        y[0] = -3
        y[1] = -2
        y[2] = -1
        y[3] = 0
        x[0] = x[1] = x[2] = x[3] = 4
    elif type == 1:
        x[0] = 3
        y[0] = -1
        x[1] = 3
        y[1] = 0
        x[2] = 4
        y[2] = 0
        x[3] = 5
        y[3] = 0
    elif type == 2:
        x[0] = 4
        y[0] = -1
        x[1] = 4
        y[1] = 0
        x[2] = 3
        y[2] = 0
        x[3] = 2
        y[3] = 0
    elif type == 3:
        x[0] = 3
        x[1] = 4
        x[2] = 4
        x[3] = 3
        y[0] = 0
        y[3] = -1
        y[1] = -1
        y[2] = 0
    elif type == 4:
        x[0] = 3
        x[1] = 4
        x[2] = 4
        x[3] = 5
        y[0] = 0
        y[3] = 0
        y[1] = 0
        y[2] = -1
    elif type == 5:
        x[0] = 3
        x[1] = 4
        x[2] = 4
        x[3] = 5
        y[0] = 0
        y[1] = 0
        y[2] = -1
        y[3] = -1
    elif type == 6:
        x[0] = 3
        x[1] = 4
        x[2] = 4
        x[3] = 5
        y[0] = -1
        y[1] = -1
        y[2] = 0
        y[3] = 0
    return x, y


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

    def minusX(self,board):
        flag = 1
        for j in range(4):
            if board[self.y[j]][self.x[j] - 1] > 0:
                flag = 0
        if flag == 1:
            for i in range(4):
                self.x[i] -= 1

    def plusX(self,board):
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

    def rotate_left(self,board):
        if self.type == 0:                                 # Check type
            if self.rotation == 0:                         # Check Rotation
                if self.x[0] + 2 >= 9:
                    for i in range(4): self.x[i] -= 2
                if board[self.bottomest_block()-2][self.x[0] - 1]== 0 and board[self.bottomest_block()-2][self.x[1]]==0 and board[self.bottomest_block()-2][self.x[2] + 1]==0 and board[self.bottomest_block()-2][self.x[3] + 2]==0:
                    self.y[0] = self.y[1] = self.y[2] = self.y[3] = self.bottomest_block() - 2
                    self.x[0] = self.x[1] - 1
                    self.x[2] = self.x[1] + 1
                    self.x[3] = self.x[1] + 2
                    if self.x[0] < 0:
                        for i in range(4): self.x[i] += 1
                    self.rotation = 1
            else:                                           # Check Rotation
                if self.bottomest_block() + 2 > 17:
                    for i in range(4): self.y[i] -= 2
                if board[self.bottomest_block()-2][self.x[0] + 2]== 0 and board[self.bottomest_block()-1][self.x[1] + 1]==0 and board[self.bottomest_block()][self.x[2]]==0 and board[self.bottomest_block() + 1][self.x[3] - 1]==0:
                    self.x[0] = self.x[1] = self.x[3] = self.x[2]
                    self.y[0] -= 2
                    self.y[1] -= 1
                    self.y[3] += 1
                    self.rotation = 0

        elif self.type == 1:
            if self.rotation == 0:
                if board[self.bottomest_block()][self.leftest_block()] ==0 and board[self.bottomest_block()][self.leftest_block() + 1] ==0 and board[self.bottomest_block() + 1][self.leftest_block() + 1] ==0:
                    self.x[0] = self.leftest_block()
                    if self.x[0] < 0:
                        self.x[0] = 0
                    self.y[0] = self.bottomest_block()
                    self.x[1] = self.x[0] + 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[1] - 1
                    self.x[3] = self.x[2]
                    self.y[3] = self.y[2] - 1
                    self.rotation = 3
            elif self.rotation == 3:
                try :
                    if board[self.bottomest_block() - 1][self.leftest_block()] ==0 and board[self.bottomest_block() - 1][self.leftest_block() + 1] ==0 and board[self.bottomest_block() - 1][self.leftest_block() + 2] ==0 and board[self.bottomest_block()][self.leftest_block() + 2] ==0:
                        self.x[0] = self.leftest_block()
                        self.y[0] = self.bottomest_block() - 1
                        self.x[1] = self.x[0] + 1
                        self.y[1] = self.y[0]
                        self.x[2] = self.x[1] + 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[2]
                        self.y[3] = self.y[2] + 1
                        self.rotation = 2
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    self.y[0] = self.bottomest_block() - 1
                    self.x[1] = self.x[0] + 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1] + 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[2]
                    self.y[3] = self.y[2] + 1
                    self.rotation = 2
            elif self.rotation == 2:
                try:
                    if board[self.bottomest_block()][self.leftest_block()] ==0 and board[self.bottomest_block() - 1][self.leftest_block()] ==0 and  board[self.bottomest_block() - 2][self.leftest_block()] ==0 and board[self.bottomest_block() - 2][self.leftest_block() + 1] ==0:
                        self.x[0] = self.leftest_block()
                        self.y[0] = self.bottomest_block()
                        self.x[1] = self.x[0]
                        self.y[1] = self.y[0] - 1
                        self.x[2] = self.x[1]
                        self.y[2] = self.y[1] - 1
                        self.x[3] = self.x[2] + 1
                        self.y[3] = self.y[2]
                        self.rotation = 1
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    self.y[0] = self.bottomest_block()
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[1] - 1
                    self.x[3] = self.x[2] + 1
                    self.y[3] = self.y[2]
                    self.rotation = 1
            else:
                try:
                    if board[self.bottomest_block()][self.leftest_block()] ==0 and board[self.bottomest_block() - 1][self.leftest_block()] ==0 and board[self.bottomest_block()][self.leftest_block() + 1] ==0 and board[self.bottomest_block()][self.leftest_block() + 2] ==0:
                        self.x[0] = self.leftest_block()
                        self.x[1] = self.x[0]
                        self.x[2] = self.x[0] + 1
                        self.x[3] = self.x[0] + 2
                        self.y[0] = self.bottomest_block()
                        self.y[1] = self.y[0] - 1
                        self.y[2] = self.y[0]
                        self.y[3] = self.y[0]
                        self.rotation = 0
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    self.y[0] = self.bottomest_block()
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[1] - 1
                    self.x[3] = self.x[2] + 1
                    self.y[3] = self.y[2]
                    self.rotation = 1


        elif self.type == 2:                                 # Check type
            if self.rotation==0:                             # Check Rotation
                if board[self.bottomest_block() - 1][self.rightest_block() -3] == 0 and board[self.bottomest_block() - 1][self.rightest_block() - 2] == 0 and board[self.bottomest_block() - 1][self.rightest_block() - 2] == 0 and board[self.bottomest_block() + 1][self.rightest_block() - 2] == 0:
                    self.x[0] = self.rightest_block() - 3
                    self.y[0] = self.bottomest_block() - 1
                    self.x[1] = self.x[0] + 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[0] + 1
                    self.x[3] = self.x[2]
                    self.y[3] = self.y[2] + 1
                    self.rotation = 1
            elif self.rotation==1:
                try:
                    if board[self.bottomest_block() + 1][self.leftest_block()] == 0 and board[self.bottomest_block()][self.leftest_block()] == 0 and board[self.bottomest_block()][self.leftest_block() + 1] == 0 and board[self.bottomest_block()][self.leftest_block() + 2] == 0:
                        self.x[0] = self.leftest_block()
                        self.y[0] = self.bottomest_block() + 1
                        self.x[1] = self.x[0]
                        self.y[1] = self.y[0] - 1
                        self.x[2] = self.x[0] + 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[0] + 2
                        self.y[3] = self.y[1]
                        self.rotation = 2
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    if self.x[0] < 0: self.x[0]=0
                    elif self.x[0] > 7 :self.x[0] = 7
                    self.y[0] = self.bottomest_block()
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[0] + 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[0] + 2
                    self.y[3] = self.y[1]
                    self.rotation = 2
            elif self.rotation==2:
                try:
                    if board[self.bottomest_block()][self.rightest_block() + 1] == 0 and board[self.bottomest_block()][self.rightest_block()] == 0 and board[self.bottomest_block() - 1][self.rightest_block()] == 0 and board[self.bottomest_block() - 2][self.rightest_block()] == 0:
                        self.x[0] = self.rightest_block() + 1
                        self.y[0] = self.bottomest_block()
                        self.x[1] = self.x[0] - 1
                        self.y[1] = self.y[0]
                        self.x[2] = self.x[1]
                        self.y[2] = self.y[1] - 1
                        self.x[3] = self.x[1]
                        self.y[3] = self.y[1] - 2
                        self.rotation = 3
                except(IndexError):
                    self.x[0] = self.rightest_block() + 1
                    if self.x[0] > 9:
                        self.x[0] -= 1
                    self.y[0] = self.bottomest_block()
                    self.x[1] = self.x[0] - 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[1] - 1
                    self.x[3] = self.x[1]
                    self.y[3] = self.y[1] - 2
                    self.rotation = 3
            elif self.rotation==3:
                try:
                    if board[self.bottomest_block() - 3][self.rightest_block()] == 0 and board[self.bottomest_block() - 2][self.rightest_block()] == 0 and board[self.bottomest_block() - 2][self.rightest_block() - 1] == 0 and board[self.bottomest_block() - 3][self.rightest_block() + 2] == 0:
                        self.x[0] = self.rightest_block()
                        self.y[0] = self.bottomest_block() - 3
                        self.x[1] = self.x[0]
                        self.y[1] = self.y[0] + 1
                        self.x[2] = self.x[1] - 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[2] - 1
                        self.y[3] = self.y[1]
                        self.rotation = 0
                except (IndexError):
                    self.x[0] = self.rightest_block()
                    if self.x[0] > 9:
                        self.x[0] -= 1
                    self.y[0] = self.bottomest_block() - 3
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] + 1
                    self.x[2] = self.x[1] - 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[2] - 1
                    self.y[3] = self.y[1]
                    self.rotation = 0
        elif self.type == 4:
            if self.rotation == 0:
                try:
                    if board[self.bottomest_block() + 2][self.leftest_block() - 1] == 0 and board[self.bottomest_block() + 1][self.leftest_block() + 1] == 0 and board[self.bottomest_block() + 1][self.leftest_block()] == 0 and board[self.bottomest_block() - 1][self.leftest_block() + 1] == 0:
                        self.x[0] = self.leftest_block() + 1
                        self.y[0] = self.bottomest_block() + 2
                        self.x[1] = self.x[0]
                        self.y[1] = self.y[0] - 1
                        self.x[2] = self.x[1] - 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[0]
                        self.y[3] = self.y[2] - 1
                        self.rotation = 1
                except(IndexError):
                    self.x[0] = self.leftest_block() + 1
                    self.y[0] = self.bottomest_block() + 2
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[1] - 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[0]
                    self.y[3] = self.y[2] - 1
                    self.rotation = 1
            elif self.rotation == 1:
                try:
                    if board[self.bottomest_block()][self.leftest_block() + 2] == 0 and board[self.bottomest_block() - 1][self.leftest_block() + 1] == 0 and board[self.bottomest_block() - 1][self.leftest_block() + 2] == 0 and board[self.bottomest_block() - 1][self.leftest_block() + 3] == 0:
                        self.x[0] = self.leftest_block() + 2
                        self.y[0] = self.bottomest_block()
                        self.x[1] = self.x[0] - 1
                        self.y[1] = self.y[0] - 1
                        self.x[2] = self.x[1] + 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[2] + 1
                        self.y[3] = self.y[1]
                        self.rotation = 2
                except(IndexError):
                    self.x[0] = self.leftest_block() + 2
                    self.y[0] = self.bottomest_block()
                    self.x[1] = self.x[0] - 1
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[1] + 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[2] + 1
                    self.y[3] = self.y[1]
                    self.rotation = 2
            elif self.rotation == 2:
                try:
                    if board[self.bottomest_block() - 1][self.leftest_block() + 1] == 0 and \
                            board[self.bottomest_block() - 2][self.leftest_block() + 1] == 0 and \
                            board[self.bottomest_block() - 2][self.leftest_block() + 2] == 0 and \
                            board[self.bottomest_block() - 3][self.leftest_block() + 1] == 0:
                        self.x[0] = self.leftest_block() + 1
                        self.y[0] = self.bottomest_block() - 1
                        self.x[1] = self.x[0]
                        self.y[1] = self.y[0] - 1
                        self.x[2] = self.x[1] + 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[0]
                        self.y[3] = self.y[0] - 2
                        self.rotation = 3
                except(IndexError):
                    self.x[0] = self.leftest_block() + 1
                    self.y[0] = self.bottomest_block() - 1
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[1] + 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[0]
                    self.y[3] = self.y[0] -2
                    self.rotation = 3
            elif self.rotation == 3:
                try:
                    if board[self.bottomest_block() - 1][self.leftest_block()] == 0 and \
                            board[self.bottomest_block() - 1][self.leftest_block() - 1] == 0 and \
                            board[self.bottomest_block() - 1][self.leftest_block() - 2] == 0 and \
                            board[self.bottomest_block() - 2][self.leftest_block() - 1] == 0:
                        self.x[0] = self.leftest_block()
                        self.y[0] = self.bottomest_block() - 1
                        self.x[1] = self.x[0] -1
                        self.y[1] = self.y[0]
                        self.x[2] = self.x[1]
                        self.y[2] = self.y[1] + 1
                        self.x[3] = self.x[2] - 1
                        self.y[3] = self.y[2] - 1
                        self.rotation = 0
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    self.y[0] = self.bottomest_block() - 1
                    self.x[1] = self.x[0] - 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[1] + 1
                    self.x[3] = self.x[2] - 1
                    self.y[3] = self.y[2] - 1
                    self.rotation = 0
        elif self.type == 5:                                 # Check type
            if self.rotation == 0:                           # Check Rotation
                try:
                    if board[self.bottomest_block() + 1][self.leftest_block()] == 0 and \
                            board[self.bottomest_block()][self.leftest_block()] == 0 and \
                            board[self.bottomest_block()][self.leftest_block() - 1] == 0 and \
                            board[self.bottomest_block() - 1][self.leftest_block() - 1] == 0:
                        self.x[0] = self.leftest_block()
                        self.y[0] = self.bottomest_block() - 1
                        self.x[1] = self.x[0]
                        self.y[1] = self.y[0] - 1
                        self.x[2] = self.x[1] - 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[2]
                        self.y[3] = self.y[2] - 1
                        self.rotation = 1
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    self.y[0] = self.bottomest_block() - 1
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[1] - 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[2]
                    self.y[3] = self.y[2] - 1
                    self.rotation = 1
            elif self.rotation == 1:                  # Check Rotation
                try:
                    if board[self.bottomest_block() ][self.leftest_block()] == 0 and \
                            board[self.bottomest_block() ][self.leftest_block() + 1] == 0 and \
                            board[self.bottomest_block() - 1][self.leftest_block() + 1] == 0 and \
                            board[self.bottomest_block() - 1][self.leftest_block() + 2] == 0:
                        self.x[0] = self.leftest_block()
                        self.y[0] = self.bottomest_block()
                        self.x[1] = self.x[0] + 1
                        self.y[1] = self.y[0]
                        self.x[2] = self.x[1]
                        self.y[2] = self.y[1] - 1
                        self.x[3] = self.x[2] + 1
                        self.y[3] = self.y[2]
                        self.rotation = 0
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    self.y[0] = self.bottomest_block()
                    self.x[1] = self.x[0] + 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[1] - 1
                    self.x[3] = self.x[2] + 1
                    self.y[3] = self.y[2]
                    self.rotation = 0
        elif self.type == 6:                                 # Check type
            if self.rotation == 0:                           # Check Rotation
                try:
                    if board[self.bottomest_block() + 1][self.leftest_block() - 1] == 0 and \
                            board[self.bottomest_block()][self.leftest_block() - 1] == 0 and \
                            board[self.bottomest_block()][self.leftest_block() ] == 0 and \
                            board[self.bottomest_block() - 1][self.leftest_block() ] == 0:
                        self.x[0] = self.leftest_block() - 1
                        self.y[0] = self.bottomest_block() - 1
                        self.x[1] = self.x[0]
                        self.y[1] = self.y[0] - 1
                        self.x[2] = self.x[1] + 1
                        self.y[2] = self.y[1]
                        self.x[3] = self.x[2]
                        self.y[3] = self.y[2] - 1
                        self.rotation = 1
                except(IndexError):
                    self.x[0] = self.leftest_block() - 1
                    self.y[0] = self.bottomest_block() - 1
                    self.x[1] = self.x[0]
                    self.y[1] = self.y[0] - 1
                    self.x[2] = self.x[1] + 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[2]
                    self.y[3] = self.y[2] - 1
                    self.rotation = 1
            elif self.rotation == 1:                  # Check Rotation
                try:
                    if board[self.bottomest_block() + 1][self.leftest_block()] == 0 and \
                            board[self.bottomest_block() + 1 ][self.leftest_block() + 1] == 0 and \
                            board[self.bottomest_block() ][self.leftest_block() + 1] == 0 and \
                            board[self.bottomest_block() ][self.leftest_block() + 2] == 0:
                        self.x[0] = self.leftest_block()
                        self.y[0] = self.bottomest_block() + 1
                        self.x[1] = self.x[0] + 1
                        self.y[1] = self.y[0]
                        self.x[2] = self.x[1]
                        self.y[2] = self.y[1] + 1
                        self.x[3] = self.x[2] + 1
                        self.y[3] = self.y[2]
                        self.rotation = 0
                except(IndexError):
                    self.x[0] = self.leftest_block()
                    self.y[0] = self.bottomest_block() + 1
                    self.x[1] = self.x[0] + 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1]
                    self.y[2] = self.y[1] + 1
                    self.x[3] = self.x[2] + 1
                    self.y[3] = self.y[2]
                    self.rotation = 0
        for i in range(4):
            if self.x[i]<0:
                self.plusX(board)
            if self.x[i]>9:
                self.minusX(board)
            if self.y[i]>=17:
                self.minusY()







