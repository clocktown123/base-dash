import pygame
import random

class Ball:
    def __init__(self):
        self.x = 800
        self.y = random.randint(100, 650)
        self.speed = random.uniform(3, 6)
        
    def update(self):
        self.x -= self.speed #moves platform left at a speed from 5 - 7
        
    def draw(self, screen):
        pygame.draw.circle(screen, (30, 50, 20), (self.x, self.y), 5)
        
        
