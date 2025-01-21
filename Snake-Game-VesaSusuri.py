import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the game speed
clock = pygame.time.Clock()

# Font for score
def draw_text(text, color, x, y, font_size=30):
    font = pygame.font.SysFont("comicsansms", font_size)
    screen.blit(font.render(text, True, color), (x, y))

# Game over function
def game_over_message(score):
    screen.fill(BLACK)
    draw_text("Game Over!", RED, WIDTH // 2 - 100, HEIGHT // 2 - 50, 50)
    draw_text(f"Your Score: {score}", WHITE, WIDTH // 2 - 100, HEIGHT // 2 + 10, 35)
    draw_text("Press Q to Quit or R to Restart", WHITE, WIDTH // 2 - 150, HEIGHT // 2 + 60, 25)
    pygame.display.update()
    time.sleep(1)

# Main game loop
def snake_game():
    # Initial position and direction
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = BLOCK_SIZE, 0  # Start moving to the right

    # Snake body and length
    snake = [(x, y)]
    snake_length = 1

    # Food position
    food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

    # Score
    score = 0

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        # Update snake position
        x += dx
        y += dy

        # Check for collisions with walls
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over_message(score)
            return

        # Check for collisions with itself
        if (x, y) in snake:
            game_over_message(score)
            return

        # Add new position to the snake
        snake.append((x, y))

        # Check if the snake has eaten the food
        if x == food_x and y == food_y:
            score += 1
            snake_length += 1
            food_x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            food_y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        else:
            # Remove the tail if the snake hasn't grown
            if len(snake) > snake_length:
                snake.pop(0)

        # Draw everything
        screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        # Display score
        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.update()

        # Control game speed
        clock.tick(10)

    pygame.quit()
    quit()

# Run the game
if __name__ == "__main__":
    while True:
        snake_game()
        # Restart or quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    break
