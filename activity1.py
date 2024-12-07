import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 250, 0), pygame.Rect(70, 70, 50, 50))
    pygame.display.flip()