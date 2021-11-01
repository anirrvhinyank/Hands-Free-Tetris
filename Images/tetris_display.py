import numpy as np
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
def infinity():
    index=0
    while True:
        yield index
        index+=1 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
k=0
for k in infinity():
    file = open("C:\\Users\\ANIRRVHINYAN K\\Desktop\\My Files\\ACM\\My tasks\\Tetris Project\\Inputs\\input.txt","r")
    if k<13:
        all_lines = file.readlines()
        array=all_lines[k]
        bitstream=list(array)
        grid = np.reshape(bitstream,(22,10))

    if k>=13:
        all_lines = file.readlines()
        array=all_lines[12]
        bitstream=list(array)
        grid = np.reshape(bitstream,(22,10))
   
    # Initialize pygame
    pygame.init()
 
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [255, 550]
    screen = pygame.display.set_mode(WINDOW_SIZE)
 
    # Set title of screen
    pygame.display.set_caption("Tetris")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:

        done=True
 
        # Set the screen background
        screen.fill(BLACK)


        # Draw the grid
        for row in range(22):
            for column in range(10):
                color = WHITE
                if grid[row][column] == '1':
                    color = GREEN
                    pygame.draw.rect(screen,color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
    
    # Limit to 1.6 frames per second
    clock.tick(1.6)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()



# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()