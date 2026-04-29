import pygame
import sys
from ball import Ball

WIDTH, HEIGHT = 800, 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball")
    clock = pygame.time.Clock()
    ball = Ball(WIDTH, HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            ball.move(0, -SPEED)
        if keys[pygame.K_DOWN]:
            ball.move(0, SPEED)
        if keys[pygame.K_LEFT]:
            ball.move(-SPEED, 0)
        if keys[pygame.K_RIGHT]:
            ball.move(SPEED, 0)

        screen.fill(WHITE)
        ball.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()