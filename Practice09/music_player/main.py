import pygame
import sys
from player import Player

WIDTH, HEIGHT = 600, 300
WHITE = (255,255,255)
BLACK = (0,0,0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    font = pygame.font.Font(None, 36)
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: player.play()
                if event.key == pygame.K_s: player.stop()
                if event.key == pygame.K_n: player.next()
                if event.key == pygame.K_b: player.prev()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        screen.blit(font.render(f"Track: {player.current()}", True, BLACK), (20,50))
        screen.blit(font.render("P=Play | S=Stop | N=Next | B=Back | Q=Quit", True, BLACK), (20,150))
        pygame.display.flip()

if __name__ == "__main__":
    main()