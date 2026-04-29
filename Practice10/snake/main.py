import pygame
import math

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# Drawing variables
is_drawing = False
start_point = (0, 0)
current_shape = "square"
color_list = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_index = 0

# Draw selected shape
def draw_shape(surface, shape, p1, p2, color):
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    top_left = (min(x1, x2), min(y1, y2))

    if shape == "square":
        side = max(width, height)
        pygame.draw.rect(surface, color, (top_left[0], top_left[1], side, side), 2)

    elif shape == "right_triangle":
        points = [(x1, y1), (x1, y2), (x2, y2)]
        pygame.draw.polygon(surface, color, points, 2)

    elif shape == "equilateral_triangle":
        side = max(width, height)
        tri_height = (math.sqrt(3) / 2) * side
        points = [(x1, y1), (x1 + side, y1), (x1 + side / 2, y1 + tri_height)]
        pygame.draw.polygon(surface, color, points, 2)

    elif shape == "rhombus":
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        half_w = abs(x1 - x2) // 2
        half_h = abs(y1 - y2) // 2
        points = [
            (center_x - half_w, center_y),
            (center_x, center_y - half_h),
            (center_x + half_w, center_y),
            (center_x, center_y + half_h)
        ]
        pygame.draw.polygon(surface, color, points, 2)

running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_drawing = True
            start_point = event.pos

        # Real-time preview while dragging
        if event.type == pygame.MOUSEMOTION and is_drawing:
            temp_surface = screen.copy()
            draw_shape(temp_surface, current_shape, start_point, event.pos, color_list[color_index])
            pygame.display.blit(temp_surface, (0, 0))

        # Finish drawing
        if event.type == pygame.MOUSEBUTTONUP and is_drawing:
            is_drawing = False
            draw_shape(screen, current_shape, start_point, event.pos, color_list[color_index])

        # Keyboard control for shapes and color
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_shape = "square"
            if event.key == pygame.K_2:
                current_shape = "right_triangle"
            if event.key == pygame.K_3:
                current_shape = "equilateral_triangle"
            if event.key == pygame.K_4:
                current_shape = "rhombus"
            if event.key == pygame.K_SPACE:
                color_index = (color_index + 1) % len(color_list)

    # Instruction text
    hint = pygame.font.SysFont(None, 30).render(
        "1:Square  2:RightTri  3:EquiTri  4:Rhombus  SPACE:Color",
        True, (0, 0, 0)
    )
    screen.blit(hint, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()