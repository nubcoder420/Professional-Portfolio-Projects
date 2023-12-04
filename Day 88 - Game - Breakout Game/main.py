import pygame
import sys


pygame.init()

# ----- Set up game window ----- #
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakout Game')

# ----- Colors ----- #
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
BLUE = (0, 0 , 255)

def breakout():

    # ----- Paddle ----- #
    paddle_width = 150
    paddle_height = 20

    paddle_x = (WIDTH - paddle_width // 2)
    paddle_y = (HEIGHT - 3 * paddle_height)
    paddle_speed = 10

    # ----- Ball ----- #
    ball_radius = 10
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = 5
    ball_speed_y = 5

    # ----- Bricks ----- #
    brick_width = 80
    brick_height = 30
    brick_spacing = 10
    bricks = []

    # Create bricks
    for row in range(5):
        for col in range(10):
            brick = pygame.Rect(col * (brick_width + brick_spacing),
                                row * (brick_height + brick_spacing),
                                brick_width,
                                brick_height)
            bricks.append(brick)

    # ----- Main Game Loop ----- #
    score = 0
    game_over = False

    while not game_over:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # ----- Key Controls ----- #
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_d] and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed

        # ----- Ball Position ----- #
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x <= 0 or ball_x >= WIDTH:
            ball_speed_x *= -1
        if ball_y <= 0 or ball_y >= HEIGHT:
            game_over = True

        # ----- Ball Collision with Paddle ----- #
        if (
            paddle_x <= ball_x <= (paddle_x + paddle_width) and
            paddle_y <= ball_y <= (paddle_y + paddle_height)
        ):
            # print(f'ball_speed_y: {ball_speed_y}, paddle_y: {paddle_y}, ball_y: {ball_y}')
            if ball_speed_y > 0:
                ball_speed_y *= -1

        # ----- Ball Collision with Bricks ----- #
        for brick in bricks:
            if brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
                bricks.remove(brick)
                ball_speed_y *= -1
                score += 1

        # ----- Draw on Screen ----- #
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (paddle_x, paddle_y, paddle_width, paddle_height))
        pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

        # ----- Draw bricks ----- #
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)

        # ----- Draw score ----- #
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, RED)
        screen.blit(score_text, (10, HEIGHT - 40))

        # ----- Refresh the Display ----- #
        pygame.time.delay(10)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # ----- Game over screen ----- #
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

    pygame.time.delay(2000)

while True:
    breakout()

    # Ask for restart
    restart_font = pygame.font.Font(None, 36)
    restart_text = restart_font.render("Press R to restart or Q to quit", True, RED)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()

    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()