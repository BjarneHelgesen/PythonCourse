import pygame

WIDTH = 600
HEIGHT = 400

#Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Element: 
    """Visual game element, such as background, obstacle or character (sprite/pixel image)"""
    def __init__(self, filename, left=0, top=0):
        self.image = pygame.image.load(filename)
        self.left = left 
        self.top = top 
        self.scale = 1
        self.angle = 0

    @property
    def width(self):
        return self.image.get_width()
    
    @property
    def height(self):
        return self.image.get_height()
    
    @property
    def right(self):
        return self.left + self.width
    
    @property
    def bottom(self):
        return self.top + self.height
    
    def blit(self):
        center_x  = self.left + self.width/2
        center_y = self.top + self.height/2 
        image = pygame.transform.smoothscale_by(self.image, self.scale)
        image = pygame.transform.rotate(image, self.angle)
        width = image.get_width()
        height = image.get_height()
        rect = pygame.Rect(center_x - width/2 , center_y - height/2, width, height)
        screen.blit(image, rect)

    def __str__(self):
        return f"({self.left}, {self.top})"

def movement(negative_key, postive_key, value):
    """Return -value if negative_key is pressed, value if positive_key is pressed, 0 if none of of them or both of them are pressed"""
    keys_pressed = pygame.key.get_pressed()
    return -keys_pressed[negative_key]*value + keys_pressed[postive_key]*value
 

red_square = Element("maidan600.jpg")
easter_egg = Element("pysanka-60.png", 100, 50)
easter_egg.dx = 3
easter_egg.dy = 0

trident = Element("trident60.png", 250, HEIGHT-70)

lost = False
while easter_egg.top <  HEIGHT: 
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    # easter egg movement
    easter_egg.left += easter_egg.dx
    easter_egg.dy += 0.2
    easter_egg.top += easter_egg.dy
    easter_egg.scale *= 0.999
    easter_egg.angle += 1


    # easter egg bouncing off side walls 
    if easter_egg.left < 0 or easter_egg.right > WIDTH:
        easter_egg.dx = -easter_egg.dx

    #Easter egg bouncing off trident. Trident will freeze when the game is lost. 
    if not lost:
        trident.left += movement(pygame.K_LEFT, pygame.K_RIGHT, 5)
        if easter_egg.bottom > trident.top + 5:
            if trident.left > easter_egg.right or trident.right < easter_egg.left:
                lost = True
            else:
                easter_egg.dy = -easter_egg.dy
                easter_egg.dx = (easter_egg.left - trident.left)/10
                easter_egg.top = trident.top - easter_egg.height + 5

    red_square.blit()
    easter_egg.blit()
    trident.blit()
    
    pygame.display.flip()

print("Game over")