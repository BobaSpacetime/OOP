import pygame
pygame.init()
WIDTH = 650
HEIGHT = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("#1008216C")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()