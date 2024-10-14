import os
import pygame


os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"


pygame.init()


WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game") 


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# Maze dimensions
ROWS, COLS = 10, 10
TILE_SIZE = WIDTH // COLS

# Define the maze layout (1 = wall, 0 = path)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Start and goal positions
start_pos = (1, 1)
goal_pos = (8, 8)
player_pos = list(start_pos)

def draw_maze(win):
    win.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            if maze[row][col] == 1:
                pygame.draw.rect(win, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
            else:
                pygame.draw.rect(win, WHITE, (x, y, TILE_SIZE, TILE_SIZE))
    
    
    pygame.draw.rect(win, GREEN, (goal_pos[1] * TILE_SIZE, goal_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    pygame.draw.circle(win, RED, (player_pos[1] * TILE_SIZE + TILE_SIZE // 2, player_pos[0] * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 3)

    pygame.display.update()

def move_player(direction):
    x, y = player_pos
    if direction == 'UP' and x > 0 and maze[x - 1][y] == 0:
        player_pos[0] -= 1
    elif direction == 'DOWN' and x < ROWS - 1 and maze[x + 1][y] == 0:
        player_pos[0] += 1
    elif direction == 'LEFT' and y > 0 and maze[x][y - 1] == 0:
        player_pos[1] -= 1
    elif direction == 'RIGHT' and y < COLS - 1 and maze[x][y + 1] == 0:
        player_pos[1] += 1

def show_end_screen(win):
    win.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Congratulations! You've reached the goal.", True, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
    
    
    button_width, button_height = 160, 50
    button_x = WIDTH // 2 - button_width // 2
    button_y = HEIGHT // 2
    
    pygame.draw.rect(win, GRAY, (button_x, button_y, button_width, button_height))
    again_text = font.render("Play Again", True, BLACK)
    win.blit(again_text, (button_x + button_width // 2 - again_text.get_width() // 2, button_y + button_height // 2 - again_text.get_height() // 2))
    pygame.display.update()

    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                    return "again"

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        draw_maze(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_player('UP')
                elif event.key == pygame.K_DOWN:
                    move_player('DOWN')
                elif event.key == pygame.K_LEFT:
                    move_player('LEFT')
                elif event.key == pygame.K_RIGHT:
                    move_player('RIGHT')

        clock.tick(60)

        
        if player_pos == list(goal_pos):
            result = show_end_screen(WIN)
            if result == "quit":
                run = False
            elif result == "again":
                player_pos[:] = start_pos

    pygame.quit()

if __name__ == "__main__":
    main()
