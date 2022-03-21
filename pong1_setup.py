import pygame
import sys

# Starting General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting main window
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# Defining Objects (Rectangles)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(10, screen_height/2 - 70, 10, 150)
opponent = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 150)

# Defining Colors
bg_color = pygame.Color('black')
light_grey = (200, 200, 200)
blue = (0, 139, 0)
red = (139, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Defining object colors
    screen.fill(bg_color)
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                       0), (screen_width/2, screen_height))

    # Defining FPS
    pygame.display.flip()
    clock.tick(60)
