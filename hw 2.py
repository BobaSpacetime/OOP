import pygame
pygame.init()
WIDTH = 650
HEIGHT = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("#1008216C")

class rect():
    def __init__(self, w, h, x, y, color, t):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.color = color
        self.t = t
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), self.t)
RECT = rect(200, 250, 10, 10, "white", int(2.5))
RECT.draw()
REC = rect( 250, 200, 390, 240, "white", 0)
REC.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

