import pygame as pygame
import pygame.gfxdraw
import maps
import towers
import enemys

#Main game init and screen Res setup
pygame.init()
size = WIDTH, Height = (960, 704)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zwink's Tower Defence")
mainicon = pygame.image.load("icons/medieval-tower.png")
pygame.display.set_icon(mainicon)

dead = False

#code needed to turn the background of the image alpha on and set it transparent 
t1atktowers = pygame.image.load("sprites/atktowers/t1atktower/t1atktower.png").convert()
t1atktowers.set_colorkey((255,255,255)) # Turns anything in the background that is white(255,255,255)
#end of image manipulation 


#Global Vars
LEFT = 1
RIGHT = 3
FPS = 15
FPSCLOCK = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255, 0)
GREEN = (0, 255, 0, 65)
RED = (255, 0, 0, 65)

def redrawGameWindow():
   
    pass


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
            print ("Left = 1 Right = 3 button clicked: " , event.button)
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (gridwidth + gridmargin)
            row = pos[1] // (gridhight + gridmargin)
            # Set that location to one
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                grid[row][column] = 1 # Left click that will place the image/ sprite
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                grid[row][column] = 0 # Right click that will remove the image/ sprite

            print("Click ", pos, "Grid coordinates: ", row, column)
            
           

    for row in range(17):
        for column in range(15):
            #color = WHITE
            if grid[row][column] == 1:
                screen.blit(t1atktowers,[(gridmargin + gridwidth) * column + gridmargin,
                             (gridmargin + gridhight) * row + gridmargin,
                             gridwidth, gridhight])
           #      color = GREEN
           #pygame.gfxdraw.box(screen,
           #                   [(gridmargin + gridwidth) * column + gridmargin,
           #                  (gridmargin + gridhight) * row + gridmargin,
           #                  gridwidth, gridhight], color)
             
 
    # Limit frames per second
    FPSCLOCK.tick(FPS)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()