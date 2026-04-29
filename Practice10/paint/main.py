import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")
clock = pygame.time.Clock()

# Drawing Settings
drawing = False
mode = "circle"  # Default mode: circle, rect, eraser
color = (0, 0, 0)
eraser_color = (255, 255, 255)
brush_size = 15
last_pos = (0, 0)

# Colors
colors = {
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0)
}

# UI Buttons
color_buttons = [
    (10, 10, 30, 30, colors["black"]),
    (50, 10, 30, 30, colors["red"]),
    (90, 10, 30, 30, colors["green"]),
    (130, 10, 30, 30, colors["blue"]),
    (170, 10, 30, 30, colors["yellow"]),
]

mode_buttons = [
    (220, 10, 80, 30, "Circle"),
    (310, 10, 80, 30, "Rect"),
    (400, 10, 80, 30, "Eraser")
]

screen.fill((255, 255, 255))

def draw_ui():
    """Draw color and mode buttons"""
    # Color Buttons
    for btn in color_buttons:
        pygame.draw.rect(screen, btn[4], btn[:4])
    # Mode Buttons
    font = pygame.font.SysFont(None, 24)
    for btn in mode_buttons:
        pygame.draw.rect(screen, (200, 200, 200), btn[:4])
        text = font.render(btn[4], True, (0,0,0))
        screen.blit(text, (btn[0]+5, btn[1]+5))

# Game Loop
running = True
while running:
    clock.tick(60)
    draw_ui()
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse Down
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Color Selection
            for btn in color_buttons:
                if pygame.Rect(btn[:4]).collidepoint(pos):
                    color = btn[4]
                    mode = "circle"
            # Mode Selection
            for btn in mode_buttons:
                if pygame.Rect(btn[:4]).collidepoint(pos):
                    if btn[4] == "Circle":
                        mode = "circle"
                    elif btn[4] == "Rect":
                        mode = "rect"
                    elif btn[4] == "Eraser":
                        mode = "eraser"
            # Start Drawing
            drawing = True
            last_pos = pos

        # Mouse Up
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Mouse Drag
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "circle":
                pygame.draw.circle(screen, color, pos, brush_size)
            elif mode == "rect":
                pygame.draw.rect(screen, color, (last_pos[0], last_pos[1], pos[0]-last_pos[0], pos[1]-last_pos[1]))
            elif mode == "eraser":
                pygame.draw.circle(screen, eraser_color, pos, brush_size*2)

    pygame.display.update()

pygame.quit()
sys.exit()