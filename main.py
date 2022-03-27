import pygame
import sys
import random


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    # Defining the movement of the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Defining the limitations of ball in screen
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.left >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    # Defining the colisions with the player and opponent
    if ball.colliderect(opponent) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - opponent.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(player) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - player.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

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
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 5, 70))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 5, 70))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 5, 70))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0

    else:
        ball_speed_y = 11 * random.choice((1, -1))
        ball_speed_x = 11 * random.choice((1, -1))
        score_time = None


# Starting General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting main window
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# Defining Objects (Rectangles)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 20, 20)
player = pygame.Rect(10, screen_height/2 - 70, 6, 130)
opponent = pygame.Rect(screen_width - 15, screen_height/2 - 70, 6, 130)

# Defining Colors
bg_color = pygame.Color('black')
light_grey = (200, 200, 200)
green = (0, 139, 0)
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
player_font = pygame.font.Font("freesansbold.ttf", 12)

# Defining score time
score_time = True

# Sounds
pong_sound = pygame.mixer.Sound("Sounds\pong.wav")
score_sound = pygame.mixer.Sound("Sounds\score.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Defining player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 8
            if event.key == pygame.K_w:
                player_speed += -8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed += -8
            if event.key == pygame.K_w:
                player_speed += 8

        # Defining opponent movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                opponent_speed += 8
            if event.key == pygame.K_UP:
                opponent_speed += -8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                opponent_speed += -8
            if event.key == pygame.K_UP:
                opponent_speed += 8

    # Functions
    ball_animation()
    player_animation()
    opponent_animation()

    # Defining object colors
    screen.fill(bg_color)
    pygame.draw.rect(screen, green, player)
    pygame.draw.rect(screen, red, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 100),
                       (screen_width/2, screen_height))
    pygame.draw.circle(screen, light_grey,
                       (screen_width/2, screen_height/2), 80, 1)

    if score_time:
        ball_start()

    # Defining player and opponent points // Defining details

    player_text = game_font.render(f"{player_score}", False, red)
    screen.blit(player_text, (695, 40))
    player_one = player_font.render("P2", False, red)
    screen.blit(player_one, (690, 15))

    equal = game_font.render(f":", False, light_grey)
    screen.blit(equal, (screen_width/2 - 5, 40))

    opponent_text = game_font.render(f"{opponent_score}", False, green)
    screen.blit(opponent_text, (590, 40))
    player_two = player_font.render("P1", False, green)
    screen.blit(player_two, (585, 15))

    # Defining FPS
    pygame.display.flip()
    clock.tick(60)
