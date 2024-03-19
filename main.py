import pygame
import random

#give us access to all the functions inside pygame
pygame.init() 


# initial set up
WIDTH = 410
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

# 2048 game color library
colors = {0:(204,192,179),
          2:(238,228,218),
          4:(237,224,200),
          8:(242,177,121),
          16:(245,149,99),
          32:(246,124,95),
          64:(246,94,59),
          128:(237,207,114),
          256:(237,204,97),
          512:(237,200,80),
          1024:(237,197,63),
          2048:(237,194,46),
          'light text':(249,246,242),
          'dark text':(119,110,101),
          'other':(0,0,0),
          'bg':(187,173,160)}

# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)] # creates 4x4 board for game

# draw backround for the board
def draw_board():
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)
    pass

#draw tiles for game
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = color['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75])
# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    # drawing board
    draw_board()
    draw_pieces(board_values)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
