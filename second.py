import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
color = (255, 100, 0)
x = 30
y = 30
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True  
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        pygame.display.flip()

