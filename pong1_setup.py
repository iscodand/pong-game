import pygame
import sys
import random


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    # Defining the movement of the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Defining the limitations of ball in screen
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_start()

    if ball.left >= screen_width:
        opponent_score += 1
        ball_start()

    # Defining the colisions with the player and opponent
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# Defining the limitations of 1° player


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

# Defining the limitations of 2° player


def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# Restarting game with ball in center


def ball_start():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# Starting General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting main window
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# Defining Objects (Rectangles)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 20, 20)
player = pygame.Rect(10, screen_height/2 - 70, 6, 150)
opponent = pygame.Rect(screen_width - 15, screen_height/2 - 70, 6, 150)

# Defining Colors
bg_color = pygame.Color('black')
light_grey = (200, 200, 200)
blue = (0, 139, 0)
red = (139, 0, 0)

# Defining Speed of Ball
ball_speed_x = 11 * random.choice((1, -1))
ball_speed_y = 11 * random.choice((1, -1))

# Defining Speed of Player
player_speed = 0
opponent_speed = 0

# Defining Score
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Defining player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 7
            if event.key == pygame.K_w:
                player_speed += -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed += -7
            if event.key == pygame.K_w:
                player_speed += 7

        # Defining opponent movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                opponent_speed += 7
            if event.key == pygame.K_UP:
                opponent_speed += -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                opponent_speed += -7
            if event.key == pygame.K_UP:
                opponent_speed += 7

    # Functions
    ball_animation()
    player_animation()
    opponent_animation()

    # Defining object colors
    screen.fill(bg_color)
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                       0), (screen_width/2, screen_height))

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (630, 35))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (560, 35))

    # Defining FPS
    pygame.display.flip()
    clock.tick(60)
