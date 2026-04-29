import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 480, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game Variables
clock = pygame.time.Clock()
FPS = 60
score = 0

# Player Car
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 120
player_speed = 10

# Enemy Car
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -100
enemy_speed = 7

# Coin Settings
coin_size = 30
coin_x = random.randint(50, WIDTH - 50)
coin_y = -50
coin_speed = 8

# Font for Score
font = pygame.font.SysFont(None, 55)

def show_score():
    """Render and display collected coins count"""
    score_text = font.render(f"Coins: {score}", True, YELLOW)
    screen.blit(score_text, (WIDTH - 180, 10))

# Game Loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement (Arrow Keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # Draw Player Car
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Enemy Car Movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - enemy_size)
    pygame.draw.rect(screen, GREEN, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Coin Movement & Collision
    coin_y += coin_speed
    pygame.draw.circle(screen, YELLOW, (coin_x + coin_size//2, coin_y + coin_size//2), coin_size//2)
    
    # Collect Coin
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)
    
    # Reset Coin if out of screen
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)

    # Show Score
    show_score()

    # Game Over (Collision with Enemy)
    if player_rect.colliderect(pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)):
        print("Game Over!")
        running = False

    pygame.display.update()

pygame.quit()
sys.exit()