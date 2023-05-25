import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()


rect = pygame.Rect((100, 100), (32, 32))

box = pygame.Surface((32, 32))
box.fill(BLACK)  


while True: 
    clock.tick(60)

    screen.fill(WHITE)
    screen.blit(box, rect)
    pygame.display.flip()
