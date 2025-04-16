import pygame
import sys
import random
import time

# paramaters

WIDTH = 1024
HEIGHT = 768
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 10, 10
BLACK = [0, 0, 0]
WHITE = (255, 255, 255)
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
ORANGE = [255, 165, 0]
L_BLUE = [173, 216, 230]

pygame.init()

# create screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
font = pygame.font.Font(None, 36)

# clock
clock = pygame.time.Clock()

# Initialize para for var

player_pos = [735, 600]
reset_player_pos = [735, 600]
player_speed = 3
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

tile_size = 10
maze_offset_x = (WIDTH - len(maze[0]) * tile_size) // 2
maze_offset_y = (HEIGHT - len(maze) * tile_size) // 2 
prev_player_pos = [0, 0]
visited = []
start_pos = 0
goal = (1, 49)
came_from = {}
path = []
path_drawn = False
# track collision
collision_prev = False

# 
def dfs(maze, row, col, visited, goal, came_from):
    start_pos = (row, col)
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if 0 < row < len(maze) and 0 < col < len(maze[row]) and start_pos not in visited and maze[row][col] == 0:
        visited.append((row, col))

        draw_maze(maze, visited, (row, col))
        #pygame.time.delay(100)

        if (row, col) == goal:
            print(f"Exit found at {row}, {col}")
            return True
        for dx, dy in direction:
            new_row = row + dx
            new_col = col + dy
            if (new_row, new_col) not in visited:
                came_from[(new_row, new_col)] = (row, col)
                if dfs(maze, new_row, new_col, visited, goal, came_from):
                    return True
    return False

def draw_maze(maze, visited, current):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * tile_size + maze_offset_x # Position on the X axis
            y = row * tile_size + maze_offset_y # Position on the Y axis
            
        
            # Draw visited cells (green)
            if (row, col) in visited:
                pygame.draw.rect(screen, GREEN, (x, y, tile_size, tile_size))
            # Draw the current path (blue)
            if (row, col) == current:
                pygame.draw.rect(screen, BLUE, (x, y, tile_size, tile_size))
            # Draw the goal (red)
            if (row, col) == goal:
                pygame.draw.rect(screen, RED, (x, y, tile_size, tile_size))
    pygame.display.update()

def recons_path(came_from, start_pos, goal):
    current = goal
    path = [current]
    while current != start_pos:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def draw_path(path):
    for pos in path:
        row, col = pos
        path_x = col * tile_size + maze_offset_x
        path_y = row * tile_size + maze_offset_y
        pygame.draw.rect(screen, WHITE, (path_x, path_y, tile_size, tile_size))
        pygame.display.update()
        #pygame.time.delay(50)

# Game Loop

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()

    # Store prev player position
    if not collision_prev:
        prev_player_pos = player_pos[:]

    # Player movement

    player_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    player_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    # reset position
    if keys[pygame.K_ESCAPE]:
        player_pos = reset_player_pos[:]
 
    # search
    if keys[pygame.K_k]:
        dfs(maze, 49, 49, visited, goal, came_from)
        path = recons_path(came_from, (49, 49), goal)
        


    # Keep player within screen bounds

    player_pos[0] = max(0, min(WIDTH - PLAYER_WIDTH, player_pos[0]))
    player_pos[1] = max(0, min(HEIGHT - PLAYER_HEIGHT, player_pos[1]))

    # Clear the screen
    screen.fill(BLACK)

    # Finish
    pygame.draw.rect(
        screen,
        RED,
        (753, 138, 10, 10)
    )
    finish_rect = pygame.Rect(753, 138, 10, 10)

    # Draw the player
    pygame.draw.rect(
        screen,
        WHITE,
        (int(player_pos[0]), int(player_pos[1]), PLAYER_WIDTH, PLAYER_HEIGHT),
    )

    # Draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            tile = maze[row][col]
            maze_x = col*tile_size + maze_offset_x
            maze_y = row*tile_size + maze_offset_y

            if tile == 1:
                maze_rect = pygame.Rect(maze_x, maze_y, tile_size, tile_size)
                pygame.draw.rect(
                    screen,
                    L_BLUE,
                    (maze_x, maze_y, tile_size, tile_size),
                )

    # collision 
    player_rect = pygame.Rect(player_pos[0],player_pos[1], PLAYER_WIDTH, PLAYER_HEIGHT)
    collision_det = False
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            tile = maze[row][col]
            maze_x = col*tile_size + maze_offset_x
            maze_y = row*tile_size + maze_offset_y

            if tile == 1:
                maze_rect = pygame.Rect(maze_x, maze_y, tile_size, tile_size)

            if player_rect.colliderect(maze_rect):
                collision_det = True
                '''coldet = font.render(f"Collision detected!", True, RED)
                colrect = coldet.get_rect(topleft=(y_rect.topright[0] + 75, 10))
                pygame.draw.rect(screen, BLACK, colrect.inflate(10, 5))
                screen.blit(coldet, colrect)'''
                break
        if collision_det:
            break

    # Check if player is in finish rect
    if player_rect.colliderect(finish_rect):
        finish_text = font.render(f"Finish!", True, ORANGE)
        finish_rect = finish_text.get_rect(topleft=(WIDTH//2 - 50, HEIGHT//2))
        pygame.draw.rect(screen, BLACK, finish_rect.inflate(10, 5))
        screen.blit(finish_text, finish_rect)

    # Collision True
    if collision_det:
        if collision_prev:
            player_pos = prev_player_pos[:]
            #print(f"last position: {prev_player_pos}, Current position: {player_pos}")
            collision_prev = False
        else:
            collision_prev = True
    else:
        collision_prev = False

    # Display information
    info_line_y = 10  # Adjust the vertical position as needed
    info_spacing = 75  # Adjust the spacing as needed

    # Draw cordinates
    x_cord = font.render(f"X: {int(player_pos[0])}", True, WHITE)
    y_cord = font.render(f"Y: {int(player_pos[1])}", True, WHITE)
    x_rect = x_cord.get_rect(topleft=(10, info_line_y))
    y_rect = y_cord.get_rect(topleft=(x_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, BLACK, x_rect.inflate(10, 5))
    pygame.draw.rect(screen, BLACK, y_rect.inflate(10, 5))
    screen.blit(x_cord, x_rect)
    screen.blit(y_cord, y_rect)

    draw_maze(maze, visited, start_pos)
    if path and not path_drawn:
        draw_path(path)
        path_drawn = True


    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
