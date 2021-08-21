import pygame,random,time, keyboard


rows, cols = (18, 8)
board = [[0 for i in range(cols)] for j in range(rows)]

#TODO add the 3 missing blocks
#TODO add rotations to missing blocks
#TODO add function that checks for a complete row
#TODO function for gameover
#TODO keeping score
#TODO finish coloring
#TODO add graphics to background
#TODO organize code


class tetrominos:
    type = 0
    rotation = 0
    x = [3] * 4
    y = [0] * 4


    def bottomest_block(self):
        return max(self.y)


    def leftest_block(self):
        return min(self.x)

    def rightest_block(self):
        return max(self.x)

    def rotate_left(self):
        if self.type == 0:
            if self.rotation == 0:
                self.x[1] = self.x[2] = self.x[3] = self.x[0]
                for i in range(1, 4):
                    self.y[i] = self.y[0] - i
                self.rotation = 1
            else:
                self.y[1] = self.y[2] = self.y[3] = self.y[0]
                if self.x[3] <= 2:
                    self.x[3] = 3
                for i in range(0, 3):
                    self.x[i] = self.x[3] - (3 - i)
                self.rotation = 0

        elif self.type == 1:
            if self.rotation == 0:
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
                self.x[0] = self.leftest_block()
                self.y[0] = self.bottomest_block()
                self.x[1] = self.x[0]
                self.y[1] = self.y[0] - 1
                self.x[2] = self.x[1]
                self.x[3] = self.x[2] + 1
                self.y[2] = self.y[1] - 1
                self.y[3] = self.y[2]
                self.rotation = 1
            else:
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



WHITE =(255, 255, 255)
BLACK =(0, 0, 0)

TETROCOLOR = [  (0, 255, 255), (0, 0, 255), (255, 128, 0), (255, 255, 0) ]
pygame.init()
size =(500, 540)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
carryOn = True

def generate_tetro():
    t1 = tetrominos()
    t1.type = random.randint(0,3)  #  [0-I block,  1-J block, 2-L block, O- Block
    t1.rotation = 0
    if t1.type == 0:
        t1.x[0] = 2
        t1.x[1] = 3
        t1.x[2] = 4
        t1.x[3] = 5
        t1.y = [0] * 4
    elif t1.type == 1:
        t1.x[0] = 2
        t1.y[0] = -1
        t1.x[1] = 2
        t1.y[1] = 0
        t1.x[2] = 3
        t1.y[2] = 0
        t1.x[3] = 4
        t1.y[3] = 0
    elif t1.type == 2:
        t1.x[0] = 4
        t1.y[0] = -1
        t1.x[1] = 4
        t1.y[1] = 0
        t1.x[2] = 3
        t1.y[2] = 0
        t1.x[3] = 2
        t1.y[3] = 0
    elif t1.type == 3:
        t1.x[0] = 3
        t1.x[1] = 4
        t1.x[2] = 4
        t1.x[3] = 3
        t1.y[0] = 0
        t1.y[3] = -1
        t1.y[1] = -1
        t1.y[2] = 0
    
    return t1





def move(t1):
    for i in range(4):
        t1.y[i] += 1


def copy(t1,board):
    for i in range(4):
        board[t1.y[i]][t1.x[i]] = 1


def collision(t1,board):
    if t1.bottomest_block() == 17:
        copy(t1, board)
        return True

    for i in range(4):
        if board[t1.y[i] + 1][t1.x[i]] == 1:
            copy(t1,board)
            return True
    return False

gamesleep=0

tetro = generate_tetro()
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and tetro.leftest_block() > 0 and board[tetro.bottomest_block()][tetro.leftest_block() - 1]==0 and board[tetro.bottomest_block() + 1][tetro.leftest_block() - 1] == 0:
                for i in range(4):
                    tetro.x[i] -= 1
            if event.key == pygame.K_RIGHT and tetro.rightest_block() < 7 and board[tetro.bottomest_block()][tetro.rightest_block() + 1]==0 and board[tetro.bottomest_block() + 1][tetro.rightest_block() + 1]==0:
                for i in range(4):
                    tetro.x[i] += 1
            if event.key == pygame.K_DOWN and tetro.bottomest_block() < 17:
                gamesleep = 0.15
            if event.key ==  pygame.K_q:
                tetro.rotate_left()


    screen.fill(WHITE)

    for i in range(4):      #-- print the current tetro
        if tetro.y[i] >= 0:
            pygame.draw.rect(screen, TETROCOLOR[tetro.type] ,[tetro.x[i] *30, tetro.y[i] * 30, 30 ,30] )
            for i in range(4):
                pygame.draw.rect(screen, BLACK, [tetro.x[i] * 30 - 1, tetro.y[i] * 30 - 1, 32, 32] , 1)

    for y in range(18):     #-- print all other blocks
        for x in range (8):
            if board[y][x] == 1:
                pygame.draw.rect(screen, BLACK, [x * 30, y * 30, 30, 30])
    pygame.display.update()


    if collision(tetro, board) == True:
        tetro = generate_tetro()
    move(tetro)
    time.sleep(0.20 - gamesleep)
    if not keyboard.is_pressed('down'):
        gamesleep = 0
    clock.tick(60)

pygame.quit()
