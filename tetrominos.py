

class tetrominos:
    type = 0
    rotation = 0
    x = [3] * 4
    y = [0] * 4
    last = 0
    cooldown = 200

    def minusY(self):
        for i in range(4):
            self.y[i] -= 1

    def minusX(self):
        for i in range(4):
            self.x[i] -= 1

    def plusX(self):
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
                if board[self.bottomest_block() - 1][self.leftest_block()] ==0 and board[self.bottomest_block() - 1][self.leftest_block() + 1] ==0 and board[self.bottomest_block() - 1][self.leftest_block() + 2] ==0 and board[self.bottomest_block()][self.leftest_block() + 2] ==0:
                    self.x[0] = self.leftest_block()
                    if self.x[0] >5:
                        self.x[0] =5
                    self.y[0] = self.bottomest_block() - 1
                    self.x[1] = self.x[0] + 1
                    self.y[1] = self.y[0]
                    self.x[2] = self.x[1] + 1
                    self.y[2] = self.y[1]
                    self.x[3] = self.x[2]
                    self.y[3] = self.y[2] + 1
                    self.rotation = 2
            elif self.rotation == 2:
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
            else:
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
                self.plusX()
            if self.x[i]>9:
                self.minusX()
            if self.y[i]>=17:
                self.minusY()







