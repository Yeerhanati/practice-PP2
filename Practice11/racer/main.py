import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 20
player_speed = 7

# Enemy car settings
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 5

# Coin system
coins = []
coin_radius = 15
coin_spawn_rate = 120
score = 0
speed_threshold = 10  # Increase speed after this score

# Font
font = pygame.font.SysFont(None, 40)

# Draw player car
def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

# Draw enemy car
def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

# Create coin with random weight (1, 3, 5)
def create_coin():
    value = random.choice([1, 3, 5])
    x = random.randint(coin_radius, WIDTH - coin_radius)
    y = -coin_radius
    coins.append({"x": x, "y": y, "value": value})

# Draw all coins
def draw_coins():
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin["x"], coin["y"]), coin_radius)
        text = font.render(str(coin["value"]), True, BLACK)
        screen.blit(text, (coin["x"] - 8, coin["y"] - 10))

# Move coins and remove out of screen
def move_coins():
    for coin in coins[:]:
        coin["y"] += 5
        if coin["y"] > HEIGHT:
            coins.remove(coin)

# Check collision between player and coins
def coin_collision():
    global score
    for coin in coins[:]:
        if player_x < coin["x"] < player_x + player_size and player_y < coin["y"] < player_y + player_size:
            score += coin["value"]
            coins.remove(coin)

# Increase enemy speed when reaching threshold
def update_speed():
    global enemy_speed
    if score >= speed_threshold:
        enemy_speed = 8

# Check car collision
def car_collision():
    if player_x < enemy_x < player_x + player_size and player_y < enemy_y < player_y + player_size:
        return True
    return False

frame_count = 0
running = True

# Main game loop
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Spawn coins periodically
    frame_count += 1
    if frame_count % coin_spawn_rate == 0:
        create_coin()

    # Enemy movement and reset
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = -enemy_size

    # Update game logic
    move_coins()
    coin_collision()
    update_speed()

    # Game over on collision
    if car_collision():
        running = False

    # Draw all elements
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)
    draw_coins()

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()