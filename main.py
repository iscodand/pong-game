import pygame
import sys
import random


def start_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill(pygame.Color(24, 24, 24))

        pong_game = large_font.render(f"PONG GAME", False, white)
        pong_game_rect = pong_game.get_rect(center=(screen_width/2, 300))
        screen.blit(pong_game, pong_game_rect)

        start = small_font.render(f"PRESS SPACE TO START", False, white)
        start_rect = start.get_rect(center=(screen_width/2, 400))
        screen.blit(start, start_rect)

        license_isco = verysmall_font.render(
            f"Powered by Isco D'Andrade", False, white)
        license_isco_rect = license_isco.get_rect(center=(screen_width/2, 650))
        screen.blit(license_isco, license_isco_rect)

        pygame.display.update()
        clock.tick(60)


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        screen.fill(pygame.Color(24, 24, 24))

        pong_game = small_font.render(f"PONG GAME", False, white)
        pong_game_rect = pong_game.get_rect(center=(screen_width/2, 50))
        screen.blit(pong_game, pong_game_rect)

        pause_text = big_font.render(f"GAME PAUSED", False, white)
        pause_text_rect = pause_text.get_rect(center=(screen_width/2, 250))
        screen.blit(pause_text, pause_text_rect)

        continue_text = medium_font.render(
            f"PRESS SPACE TO 'CONTINUE'", False, white)
        continue_text_rect = continue_text.get_rect(
            center=(screen_width/2, screen_height/2 + 10))
        screen.blit(continue_text, continue_text_rect)

        quit_text = medium_font.render(f"PRESS ESC TO 'QUIT'", False, white)
        quit_text_rect = quit_text.get_rect(
            center=(screen_width/2, screen_height/2 + 50))
        screen.blit(quit_text, quit_text_rect)

        license_isco = verysmall_font.render(
            f"Powered by Isco D'Andrade", False, white)
        license_isco_rect = license_isco.get_rect(center=(screen_width/2, 650))
        screen.blit(license_isco, license_isco_rect)

        pygame.display.update()
        clock.tick(60)


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
        number_three = medium_font.render("3", False, white)
        screen.blit(number_three, (screen_width/2 - 5, 70))

    if 700 < current_time - score_time < 1400:
        number_two = medium_font.render("2", False, white)
        screen.blit(number_two, (screen_width/2 - 5, 70))

    if 1400 < current_time - score_time < 2100:
        number_one = medium_font.render("1", False, white)
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

# Setting main windown
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
pygame.display.set_caption('Pong Game')

# Fonts
verysmall_font = pygame.font.SysFont('Network', 15)
small_font = pygame.font.SysFont('Network', 22)
medium_font = pygame.font.SysFont('Network', 30)
big_font = pygame.font.SysFont('Network', 48)
large_font = pygame.font.SysFont('Network', 90)

# Blink Event
blink_event = pygame.USEREVENT + 0
empty = (0, 0, 0)

# Defining Objects (Rectangles)
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 20, 20)
player = pygame.Rect(10, screen_height/2 - 70, 6, 130)
opponent = pygame.Rect(screen_width - 15, screen_height/2 - 70, 6, 130)

# Defining Speed of Ball
ball_speed_x = 11 * random.choice((1, -1))
ball_speed_y = 11 * random.choice((1, -1))

# Defining Colors
bg_color = pygame.Color('black')
white = pygame.Color('white')

# Defining Speed of Player
player_speed = 0
opponent_speed = 0

# Defining Score
player_score = 0
opponent_score = 0

# Defining score time
score_time = False

# Sounds
pong_sound = pygame.mixer.Sound("Sounds\pong.wav")
score_sound = pygame.mixer.Sound("Sounds\score.wav")


def game():
    global player_speed, opponent_speed
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

            # Defining pause keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()

        # Functions
        ball_animation()
        player_animation()
        opponent_animation()

        # Defining object colors
        screen.fill(bg_color)
        pygame.draw.rect(screen, white, player)
        pygame.draw.rect(screen, white, opponent)
        pygame.draw.ellipse(screen, white, ball)
        pygame.draw.aaline(screen, white, (screen_width/2, 100),
                           (screen_width/2, screen_height))
        pygame.draw.circle(screen, white,
                           (screen_width/2, screen_height/2), 40, 1)

        if score_time:
            ball_start()

        # Defining player and opponent points
        player_text = big_font.render(f"{player_score}", False, white)
        screen.blit(player_text, (695, 30))

        equal = big_font.render(f":", False, white)
        screen.blit(equal, (screen_width/2 - 5, 30))

        opponent_text = big_font.render(f"{opponent_score}", False, white)
        screen.blit(opponent_text, (590, 30))

        # Defining FPS
        pygame.display.flip()
        clock.tick(60)


start_menu()
