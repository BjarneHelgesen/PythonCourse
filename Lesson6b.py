import pygame
pygame.init()

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
        ...

    def blit(self):
        rect = pygame.Rect((self.left, self.top), (self.width, self.height))
        screen.blit(self.surface, rect)

def overlap(element1, element2):
     if element1.bottom < element2.top or element2.bottom < element1.top:
         return False
     if element1.right < element2.left or element2.right < element1.left:
         return False
     return True 

def movement(negative_key, postive_key, value):  
    """Return -value if negative_key is pressed, value if positive_key is pressed, 0 if none of of them or both of them are pressed
    Keys could be pygame.K_LEFT, pygame.K_RIGHT, etc"""
    keys_pressed = pygame.key.get_pressed()
    return -keys_pressed[negative_key]*value + keys_pressed[postive_key]*value

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

background = Element("Maidan600.jpg")
egg = Element("pysanka-60.png", 0, 300)

while True: 
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)
    egg.update()
    egg.left += movement(pygame.K_LEFT, pygame.K_RIGHT, 1)

    background.blit()
    egg.blit()
    pygame.display.flip()
