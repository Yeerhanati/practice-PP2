import pygame
import sys
from clock import MickeyClock

WIDTH, HEIGHT = 600, 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey's Clock")
    clock = pygame.time.Clock()

    mk = MickeyClock(screen, (WIDTH//2, HEIGHT//2))
    try:
        mk.load_image("images/mickey_hand.png")
    except:
        print("Image not found!")
        pygame.quit()
        sys.exit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 240, 200))
        mk.update()
        pygame.display.flip()
        clock.tick(1)

if __name__ == "__main__":
    main()