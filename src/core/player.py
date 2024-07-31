# src/core/player.py

import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)  # Blue color for the player
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jump_strength = 10
        self.gravity = 0.5
        self.is_jumping = False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity.y = -self.jump_strength
            self.is_jumping = True

    def apply_gravity(self):
        self.velocity.y += self.gravity
        if self.rect.y + self.rect.height >= 600:  # Assuming ground level is at 600 pixels
            self.rect.y = 600 - self.rect.height
            self.is_jumping = False
            self.velocity.y = 0

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
