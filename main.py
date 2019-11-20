import pygame
import pygame.gfxdraw
import maps
import towers
import enemys

#Main game init and screen Res setup
pygame.init()
size = WIDTH, Height = (960, 766)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zwink's Tower Defence")
mainicon = pygame.image.load("icons/medieval-tower.png")
pygame.display.set_icon(mainicon)

dead = False

#Global Vars

FPS = 15
FPSCLOCK = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255, 0)
GREEN = (0, 255, 0, 65)

gridwidth = 64
gridhight = 64
gridmargin = 0
gridsize = (gridwidth, gridhight)

    # --- Create grid of numbers
    # Create an empty list
grid = []
    # Loop for each row
for row in range(17):
        # For each row, create a list that will
        # represent an entire row
    grid.append([])
        # Loop for each column
    for column in range(15):
            # Add a the number zero to the current row
        grid[row].append(0)

#Main Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            dead = True

    maps.map_1()
    if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (gridwidth + gridmargin)
            row = pos[1] // (gridhight + gridmargin)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    for row in range(17):
        for column in range(15):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.gfxdraw.box(screen,
                              [(gridmargin + gridwidth) * column + gridmargin,
                              (gridmargin + gridhight) * row + gridmargin,
                              gridwidth, gridhight], color)
 
    # Limit to 60 frames per second
    FPSCLOCK.tick(FPS)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()