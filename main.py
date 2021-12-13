import random

import pygame
from tetrominos import gen_tet, generate,scanarray
import keyboard
import time
import os


# TODO organize code
# TODO add music


rows, cols = (18, 10)
block_size = 30


#  Graphics -
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
TETROCOLOR = [(0, 255, 255), (0, 0, 255), (255, 128, 0), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0)]

# Game Vars -
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
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'background.png')
BACKGROUND = pygame.image.load(filename)

"""check for first occurence of a value!=0 in a column of a 2d array"""
def check_col(array, col,startindex):
    for i in range(startindex,18):
        if array[i][col] > 0:
            return i
    return 18

"""calculates where the block ia going to land"""
def whereblockland(tetro,board):

    y= [0]*4
    for i in range(4):

        y[i] = check_col(board,tetro.x[i],max(tetro.y))
    print(min(y))
    x,yy= scanarray(tetro.type,tetro.rotation,min(y),tetro.leftest_block())
    for i in range(4):
        if (yy[i]>=18) or (board[yy[i]][tetro.x[i]]>0):
            for j in range(4):
                yy[j]-=1
    return tetro.x,yy


def startover():
    board = [[0 for i in range(cols)] for j in range(rows)]
    return board, time.time(),1,-1


def print_gameover(score):
    gameover = MYFONT.render("You lost, You Score:" + str(score) + "press any key to restart", False, WHITE)
    screen.blit(gameover, (200, 250))


def print_pause():
    presstopause = MYFONT.render("Press any key to start...", False, WHITE)
    screen.blit(presstopause, (200, 250))


def print_menu():
    presstostart = MYFONT.render("Press any key to start...", False, WHITE)
    screen.blit(presstostart, (200, 250))


def print_next(tetro, hold):
    x = [0] * 4
    y = [0] * 4
    nextblock = tetro.nextblock
    x, y = gen_tet(nextblock)
    for i in range(4):  # -- print the current tetro
        pygame.draw.rect(screen, TETROCOLOR[nextblock], [x[i] * 30 + 260, y[i] * 30 + 100, 30, 30])
        for i in range(4):
            pygame.draw.rect(screen, BLACK, [(x[i] * 30) + 260, (y[i] * 30) + 100, 31, 31], 1)
    if hold != -1:
        x, y = gen_tet(hold)
        for i in range(4):  # -- print the current tetro
            pygame.draw.rect(screen, TETROCOLOR[hold], [x[i] * 30 + 270, y[i] * 30 + 200, 30, 30])
            for i in range(4):
                pygame.draw.rect(screen, BLACK, [(x[i] * 30) + 270, (y[i] * 30) + 200, 31, 31], 1)


def print_game(tetro, board, hold, starttime):
    screen.blit(BACKGROUND, (0, 0))
    score_label = MYFONT.render(str(SCORE), False, WHITE)
    time_label = MYFONT.render(str("%.2f" % (time.time() - starttime)), False, WHITE)
    level_label = MYFONT.render(str(level), False, WHITE)
    screen.blit(level_label, (430, 330))
    screen.blit(score_label, (430, 470))
    screen.blit(time_label, (430, 400))
    for i in range(4):  # -- print the current tetro
        if tetro.y[i] >= 0:
            pygame.draw.rect(screen, TETROCOLOR[tetro.type], [tetro.x[i] * 30 + 30, tetro.y[i] * 30 + 30, 30, 30])
            for i in range(4):
                pygame.draw.rect(screen, BLACK, [(tetro.x[i] * 30) + 30, (tetro.y[i] * 30) + 30, 31, 31], 1)
    xarr,yarr= whereblockland(tetro,board)
    for y in range(18):  # -- print all other blocks
        for x in range(10):
            for index in range(4):
                if xarr[index] == x and yarr[index] == y:                              #print where block will land TODO fix
                    pygame.draw.rect(screen, WHITE, [x * 30 + 30, y * 30 + 30, 30, 30])
                    for i in range(4):
                        pygame.draw.rect(screen, BLACK, [(x * 30) - 1 + 30, (y * 30) - 1 + 30, 31, 31], 1)
            if board[y][x] > 0:
                pygame.draw.rect(screen, TETROCOLOR[board[y][x] - 1], [x * 30 + 30, y * 30 + 30, 30, 30])
                for i in range(4):
                    pygame.draw.rect(screen, BLACK, [(x * 30) - 1 + 30, (y * 30) - 1 + 30, 31, 31], 1)
    print_next(tetro, hold)


def hold(tetro, hold):
    oldblock = tetro.type
    if hold == -1:
        next = tetro.nextblock
        tetro = generate(level, next)
    else:
        tetro = generate(level, hold)
    return tetro, oldblock


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
        if t1.y[i] == 0:
            return 3
        board[t1.y[i]][t1.x[i]] = t1.type + 1
    rowtocheck = t1.bottomest_block()
    for x in range(4):
        fullrow = 1
        for j in range(10):
            if board[rowtocheck][j] == 0:
                fullrow = 0
        if fullrow == 1:
            SCORE += 1 * level
            removerow(board, rowtocheck)
            rowtocheck += 1
            if SCORE > 4 * level:
                level += 1
        rowtocheck -= 1


def collision(t1, board):
    if t1.bottomest_block() == 17:
        return True

    for i in range(4):
        if t1.y[i] + 1 >= 0:
            if board[t1.y[i] + 1][t1.x[i]] > 0:
                return True
    return False


def main():
    board = [[0 for i in range(cols)] for j in range(rows)]
    holdlasttime = 1
    starttime = 0
    carryOn = 0  # (0-Start Menu, 1-Play, 2-Pause, 3-gameover, -1-EXIT)
    holdblock = -1
    lastchance = 0
    tetro = generate(level,random.randint(0,6))
    while carryOn >= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = -1
            elif event.type == pygame.KEYDOWN:
                if carryOn == 0:
                    starttime = time.time()
                    carryOn = 1
                elif carryOn == 1 and event.key == pygame.K_ESCAPE:
                    carryOn = 2
                elif carryOn == 2:
                    carryOn = 1
                elif carryOn == 3:
                    board , starttime, carryOn,holdblock = startover()
                    tetro = generate(level, -1)
                if event.key == pygame.K_LEFT and tetro.leftest_block() > 0:
                    tetro.minusX(board)
                elif event.key == pygame.K_RIGHT and tetro.rightest_block() < 9:
                    tetro.plusX(board)
                if event.key == pygame.K_h and holdlasttime == 1:
                    holdlasttime = 0
                    tetro, holdblock = hold(tetro, holdblock)
                if event.key == pygame.K_DOWN and tetro.bottomest_block() < 17:
                    tetro.cooldown = 50
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    tetro.rotate(board)
        if carryOn == 0:
            print_menu()
            pygame.display.update()
        elif carryOn == 1:
            print_game(tetro, board, holdblock, starttime)
            pygame.display.update()
            now = pygame.time.get_ticks()
            if now - tetro.last >= tetro.cooldown:
                tetro.last = now
                if lastchance == 1 and collision(tetro, board):
                    if copy(tetro, board) == 3:
                        carryOn = 3
                    next = tetro.nextblock
                    tetro = generate(level, next)
                    lastchance = 0
                    holdlasttime = 1
                elif collision(tetro, board):
                    lastchance = 1
                elif collision(tetro, board) is False:
                    move(tetro)

            if not keyboard.is_pressed('down'):
                tetro.cooldown = 200 - (level * 2)
        elif carryOn == 2:  # Pause_game
            screen.fill(BLACK)
            print_pause()
            pygame.display.update()
        else:
            screen.fill(BLACK)
            print_gameover(SCORE)
            pygame.display.update()
        clock.tick(60)

    pygame.quit()


main()
