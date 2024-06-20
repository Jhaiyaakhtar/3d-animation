import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D Rotating Cube')

# Define vertices of a cube (x, y, z)
vertices = [(-1, -1, -1),
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, 1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, 1, 1)]

# Define edges of the cube (vertex indices)
edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Initial rotation angles (in radians)
angle_x = 0
angle_y = 0
angle_z = 0

# Function to rotate a point around the x-axis
def rotate_x(point, angle):
    x, y, z = point
    new_y = y * math.cos(angle) - z * math.sin(angle)
    new_z = y * math.sin(angle) + z * math.cos(angle)
    return (x, new_y, new_z)

# Function to rotate a point around the y-axis
def rotate_y(point, angle):
    x, y, z = point
    new_x = x * math.cos(angle) + z * math.sin(angle)
    new_z = -x * math.sin(angle) + z * math.cos(angle)
    return (new_x, y, new_z)

# Function to rotate a point around the z-axis
def rotate_z(point, angle):
    x, y, z = point
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return (new_x, new_y, z)

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Rotate each vertex of the cube
    rotated_vertices = []
    for vertex in vertices:
        rotated = rotate_x(vertex, angle_x)
        rotated = rotate_y(rotated, angle_y)
        rotated = rotate_z(rotated, angle_z)
        rotated_vertices.append(rotated)
    
    # Draw the edges of the rotated cube
    for edge in edges:
        start = rotated_vertices[edge[0]]
        end = rotated_vertices[edge[1]]
        pygame.draw.line(screen, WHITE, (start[0]*100 + WIDTH//2, start[1]*100 + HEIGHT//2), 
                         (end[0]*100 + WIDTH//2, end[1]*100 + HEIGHT//2), 2)
    
    # Update rotation angles
    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.005
    
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()