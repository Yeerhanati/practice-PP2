import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
RADIUS = 25
SPEED = 20

class Ball:
    def __init__(self, screen_w, screen_h):
        self.x = screen_w // 2
        self.y = screen_h // 2
        self.sw = screen_w
        self.sh = screen_h

    def move(self, dx, dy):
        nx = self.x + dx
        ny = self.y + dy
        if (nx - RADIUS >= 0 and nx + RADIUS <= self.sw and
            ny - RADIUS >= 0 and ny + RADIUS <= self.sh):
            self.x = nx
            self.y = ny

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), RADIUS)