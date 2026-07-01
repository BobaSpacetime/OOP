import pygame
pygame.init()
WIDTH = 650
HEIGHT = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("#100821FF")

class circ():
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def drawpi(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def movingup(self):
        self.y -= 10
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def movingdown(self):
        self.y += 10
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def movingleft(self):
        self.x -= 10
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def movingright(self):
        self.x += 10
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def sizeup(self):
        self.r += 5
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

circl = circ(325, 225, 30, "white")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circl.drawpi()
        if event.type == pygame.MOUSEBUTTONUP:
            circl.sizeup()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("#100821FF")
                circl.movingup()
            if event.key == pygame.K_DOWN:
                screen.fill("#100821FF")
                circl.movingdown()
            if event.key == pygame.K_LEFT:
                screen.fill("#100821FF")
                circl.movingleft()
            if event.key == pygame.K_RIGHT:
                screen.fill("#100821FF")
                circl.movingright()
    pygame.display.update()
