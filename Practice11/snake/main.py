import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

# Game Settings
BLOCK_SIZE = 20
SPEED = 10
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.SysFont(None, 40)

class SnakeGame:
    def __init__(self):
        self.snake = [(WIDTH//2, HEIGHT//2)]
        self.dx = BLOCK_SIZE
        self.dy = 0
        self.food = self.spawn_food()
        self.score = 0
        self.level = 1
        self.speed = SPEED

    def spawn_food(self):
        """Spawn food NOT on snake body"""
        while True:
            x = random.randint(0, (WIDTH-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, (HEIGHT-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def move_snake(self):
        """Move snake and check wall collision"""
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.dx, head_y + self.dy)

        # Border Collision (Game Over)
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            return False

        # Self Collision
        if new_head in self.snake:
            return False

        self.snake.insert(0, new_head)
        
        # Eat Food
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
            # Level Up every 4 foods
            if self.score % 4 == 0:
                self.level += 1
                self.speed += 2
        else:
            self.snake.pop()
        return True

    def draw(self):
        screen.fill(BLACK)
        # Draw Snake
        for segment in self.snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE-2, BLOCK_SIZE-2))
        # Draw Food
        pygame.draw.rect(screen, RED, (self.food[0], self.food[1], BLOCK_SIZE-2, BLOCK_SIZE-2))
        # Draw UI
        screen.blit(font.render(f"Score: {self.score}", True, WHITE), (10, 10))
        screen.blit(font.render(f"Level: {self.level}", True, WHITE), (WIDTH-120, 10))

# Game Instance
game = SnakeGame()
running = True

while running:
    clock.tick(game.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Direction Control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.dy == 0:
                game.dx = 0
                game.dy = -BLOCK_SIZE
            if event.key == pygame.K_DOWN and game.dy == 0:
                game.dx = 0
                game.dy = BLOCK_SIZE
            if event.key == pygame.K_LEFT and game.dx == 0:
                game.dx = -BLOCK_SIZE
                game.dy = 0
            if event.key == pygame.K_RIGHT and game.dx == 0:
                game.dx = BLOCK_SIZE
                game.dy = 0

    # Move Snake
    if not game.move_snake():
        print("Game Over!")
        running = False

    game.draw()
    pygame.display.update()

pygame.quit()
sys.exit()