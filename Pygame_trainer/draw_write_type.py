import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, 'pink', (50,50,40,40))

# text
font = pygame.font.SysFont("Comic Sans Roman", 40)
text = font.render("Jesus is the light of the World!", True, 'blue')
text_rect = text.get_rect()
text_rect.center=(250,250)

while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()