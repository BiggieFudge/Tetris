import pygame
import random
import keyboard
import tetrominos
import time
from tetrominos import tetrominos








# TODO organize code

rows, cols = (18, 10)
board = [[0 for i in range(cols)] for j in range(rows)]

#  Graphics -
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
TETROCOLOR = [(0, 255, 255), (0, 0, 255), (255, 128, 0), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0)]

# Game Vars -
carryOn = True
SCORE = 0
timer = 0
level = 1

# Pygame initiallize
pygame.init()
clock = pygame.time.Clock()
size = (540, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
MYFONT = pygame.font.SysFont('Arial', 24)
BACKGROUND = pygame.image.load(r'C:\Users\eytan\Desktop\test2.png')





def print_game(tetro, board):
    screen.blit(BACKGROUND, (0, 0))
    score_label = MYFONT.render(str(SCORE), False, WHITE)
    time_label = MYFONT.render(str("%.2f" % (time.time() - starttime)), False, WHITE)
    level_label = MYFONT.render(str(level), False, WHITE)
    screen.blit(level_label, (430, 310))
    screen.blit(score_label, (430, 450))
    screen.blit(time_label, (430, 380))
    for i in range(4):  # -- print the current tetro
        if tetro.y[i] >= 0:
            pygame.draw.rect(screen, TETROCOLOR[tetro.type], [tetro.x[i] * 30 + 30, tetro.y[i] * 30 + 30, 30, 30])
            for i in range(4):
                pygame.draw.rect(screen, BLACK, [(tetro.x[i] * 30) + 30, (tetro.y[i] * 30) + 30, 31, 31], 1)

    for y in range(18):  # -- print all other blocks
        for x in range(10):
            if board[y][x] > 0:
                pygame.draw.rect(screen, TETROCOLOR[board[y][x] - 1], [x * 30 + 30, y * 30 + 30, 30, 30])
                for i in range(4):
                    pygame.draw.rect(screen, BLACK, [(x * 30) - 1 + 30, (y * 30) - 1 + 30, 31, 31], 1)


def generate_tetro():
    t1 = tetrominos()
    t1.type = random.randint(0, 6)  # [0-I block,  1-J block, 2-L block, 3-O Block, 4-T, 5-S, 6-Z ]
    t1.rotation = 0
    t1.cooldown = 100 - (level * 2)
    t1.last = pygame.time.get_ticks()
    if t1.type == 0:
        t1.y[0] = -3
        t1.y[1] = -2
        t1.y[2] = -1
        t1.y[3] = 0
        t1.x[0] = t1.x[1] = t1.x[2] = t1.x[3] = 5
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
    elif t1.type == 4:
        t1.x[0] = 4
        t1.x[1] = 5
        t1.x[2] = 5
        t1.x[3] = 6
        t1.y[0] = 0
        t1.y[3] = 0
        t1.y[1] = 0
        t1.y[2] = -1
    elif t1.type == 5:
        t1.x[0] = 4
        t1.x[1] = 5
        t1.x[2] = 5
        t1.x[3] = 6
        t1.y[0] = 0
        t1.y[1] = 0
        t1.y[2] = -1
        t1.y[3] = -1
    elif t1.type == 6:
        t1.x[0] = 4
        t1.x[1] = 5
        t1.x[2] = 5
        t1.x[3] = 6
        t1.y[0] = -1
        t1.y[1] = -1
        t1.y[2] = 0
        t1.y[3] = 0
    return t1


def removerow(board, row):
    for i in range(row, 1, -1):
        for j in range(10):
            board[i][j] = board[i - 1][j]


def move(t1):
    for i in range(4):
        t1.y[i] += 1


def copy(t1, board):
    global SCORE
    global level
    for i in range(4):
        if t1.y[i] == -1:
            exit(1)  # TODO add gameover screen (DISPLAYS SCORE)
        board[t1.y[i]][t1.x[i]] = t1.type + 1
    for x in range(4):
        i = 0
        fullrow = 1
        for j in range(10):
            if board[t1.bottomest_block() - i][j] == 0:
                fullrow = 0
        if fullrow == 1:
            SCORE += 1 * level
            removerow(board, t1.bottomest_block() - i)
            if SCORE > 4 * level:
                level += 1

        else:
            i += 1


def collision(t1, board):
    if t1.bottomest_block() == 17:
        return True

    for i in range(4):
        if t1.y[i] + 1 >= 0:
            if board[t1.y[i] + 1][t1.x[i]] > 0:
                return True
    return False


gamesleep = 0
lastchance = 0
tetro = generate_tetro()
starttime = time.time()
while carryOn:                          #TODO add option for pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and tetro.leftest_block() > 0:
                flag = 1
                for j in range(4):
                    if board[tetro.y[j]][tetro.x[j] - 1] > 0:
                        flag = 0
                if flag == 1:
                    for i in range(4):
                        tetro.x[i] -= 1
            elif event.key == pygame.K_RIGHT and tetro.rightest_block() < 9:
                flag = 1
                for j in range(4):
                    if board[tetro.y[j]][tetro.x[j] + 1] > 0:
                        flag = 0
                if flag == 1:
                    for i in range(4):
                        tetro.x[i] += 1

            if event.key == pygame.K_DOWN and tetro.bottomest_block() < 17:
                tetro.cooldown = 50
            if event.key == pygame.K_SPACE:
                tetro.rotate_left(board)

    print_game(tetro, board)
    pygame.display.update()
    now = pygame.time.get_ticks()
    if now - tetro.last >= tetro.cooldown:
        tetro.last = pygame.time.get_ticks()
        if lastchance == 1 and collision(tetro, board):
            copy(tetro, board)
            tetro = generate_tetro()
            lastchance = 0

        elif collision(tetro, board):
            lastchance = 1
        elif collision(tetro, board) is False:
            move(tetro)

        if not keyboard.is_pressed('down'):
            tetro.cooldown = 100 - (level * 2)
    clock.tick(60)

pygame.quit()
