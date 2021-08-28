

class tetrominos:
    type = 0
    rotation = 0
    x = [3] * 4
    y = [0] * 4
    last = 0
    cooldown = 100

    def bottomest_block(self):
        return max(self.y)


    def leftest_block(self):
        return min(self.x)

    def rightest_block(self):
        return max(self.x)

    def rotate_left(self,board):
        if self.type == 0:
            if self.rotation == 0:
                if board[self.y[0]][self.x[0]]==0:
                    self.x[1] = self.x[2] = self.x[3] = self.x[0]
                elif board[self.y[0]][self.x[0]-1]==0:
                    self.x[1] = self.x[2] = self.x[3] = self.x[0] - 1
                elif board[self.y[0]][self.x[0]+1]==0:
                    self.x[1] = self.x[2] = self.x[3] = self.x[0] + 1
                else:
                    return
                for i in range(1, 4):
                    self.y[i] = self.y[0] - i
                self.rotation = 1
            else:
                if board[self.y[0]][self.x[0]] ==0 and board[self.y[0]][self.x[1] -1] ==0 and board[self.y[0]][self.x[2] - 2] ==0 and board[self.y[0]][self.x[3]] ==0:
                    if self.x[3] <= 2:
                        self.x[3] = 3
                else:
                    return
                for i in range(0, 3):
                    self.x[i] = self.x[3] - (3 - i)
                self.y[1] = self.y[2] = self.y[3] = self.y[0]
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
        elif self.type == 2:
            1
        elif self.type == 3:
            2    #  --O Block Dont do nothing
