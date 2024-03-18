import pygame
import random

#give us access to all the functions inside pygame
pygame.init() 


# initial set up
WIDTH = 480
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
