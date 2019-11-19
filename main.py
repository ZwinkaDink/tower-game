import pygame
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

#Main Loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            dead = True

    maps.map_1()

    pygame.display.flip()
   