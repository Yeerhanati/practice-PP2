import pygame
import os

class Player:
    def __init__(self, path="music/"):
        pygame.mixer.init()
        self.tracks = [f for f in os.listdir(path) if f.endswith(('.mp3','.wav'))]
        self.index = 0
        self.playing = False

    def play(self):
        if self.tracks:
            pygame.mixer.music.load(os.path.join("music", self.tracks[self.index]))
            pygame.mixer.music.play()
            self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()

    def current(self):
        return self.tracks[self.index] if self.tracks else "No tracks"