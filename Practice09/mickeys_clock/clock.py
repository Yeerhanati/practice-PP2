import pygame
from datetime import datetime

class MickeyClock:
    def __init__(self, screen, center):
        self.screen = screen
        self.center = center
        self.hand = None

    def load_image(self, path):
        self.hand = pygame.image.load(path).convert_alpha()
        self.hand = pygame.transform.scale(self.hand, (30, 180))

    def rotate(self, angle, offset):
        if not self.hand:
            return
        rot = pygame.transform.rotate(self.hand, angle)
        rect = rot.get_rect(center=(self.center[0]+offset, self.center[1]))
        self.screen.blit(rot, rect)

    def update(self):
        now = datetime.now()
        sec = now.second
        min = now.minute

        ang_sec = -sec * 6 + 90
        ang_min = -min * 6 + 90

        self.rotate(ang_sec, -30)
        self.rotate(ang_min, 30)