# src/main.py

import pygame
import sys
from core.player import Player

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Your Game Title")

# Create a Player instance
player = Player(x=100, y=500, width=50, height=50)

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game objects
        player.update()

        # Drawing to the screen
        screen.fill(WHITE)  # Fill the screen with white
        player.draw(screen)  # Draw the player character

        pygame.display.flip()  # Update the display

        clock.tick(60)  # Cap the frame rate at 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
