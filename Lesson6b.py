import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Element:   
    def __init__(self, filename, left=0, top=0):
        self.surface = pygame.image.load(filename)
        self.left = left
        self.top = top

    @property
    def width(self):
        return self.surface.get_width()

    @property
    def height(self):
        return self.surface.get_height()

    @property
    def right(self):
        return self.left + self.width
    
    @property
    def bottom(self):
        return self.top + self.height
    
    def update(self):
        self.left += 1

    def blit(self):
        rect = pygame.Rect((self.left, self.top), (self.width, self.height))
        screen.blit(self.surface, rect)

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

background = Element("Maidan600.jpg")
egg = Element("pysanka-60.png")

while True: 
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)
    egg.update()

    background.blit()
    egg.blit()
    pygame.display.flip()
