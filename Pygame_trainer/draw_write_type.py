import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, 'red', (40,40,30,30))

# write
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the world!', True, 'pink')
text_rect = text.get_rect()
text_rect.center=(250,250)

# Ending
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()