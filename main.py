import pygame
pygame.init()
width, height = 800, 600
display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Invaders")
pygame.display.update
open = True
timer = pygame.time.Clock()

def main():
    while open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open = False
        display.fill()
        timer.tick(60)
        pygame.display.update
    pygame.quit()   
    quit()