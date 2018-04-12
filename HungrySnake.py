import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hungry Snake")

food = (4, 5)
body = [(1, 1),(1, 2)]
head = (1, 3)

BLACK = 0, 0, 0
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255

def my_draw_rect(zb, color, screen):
    pygame.draw.rect(screen, color, ((zb[1]-1)*50+1, (zb[0]-1)*50+1, 48, 48))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    my_draw_rect(food, RED, screen)
    my_draw_rect(head, GREEN, screen)
    for i in body:
        my_draw_rect(i, BLUE, screen)

    pygame.display.update()