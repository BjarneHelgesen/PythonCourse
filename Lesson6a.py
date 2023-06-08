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

    def collide(self, other):
        if self.bottom < other.top or other.bottom < self.top: #overlap vertically? 
            return False
        if self.right < other.left or other.right < self.left: #overlap horzontally? 
            return False
        return True 

    def __str__(self):
        return f"({self.left}, {self.top})"

def movement(negative_key, postive_key, value):
    """Return -value if negative_key is pressed, value if positive_key is pressed, 0 if none of of them or both of them are pressed"""
    keys_pressed = pygame.key.get_pressed()
    return -keys_pressed[negative_key]*value + keys_pressed[postive_key]*value
 

class MovingElement(Element):
    def __init__(self, filename, left=0, top=0):
        super().__init__(filename, left, top)
        self.dx = 0
        self.dy =0

    def update(self):
        self.left += self.dx
        self.top += self.dy

background = Element("maidan600.jpg")
egg = MovingElement("pysanka-60.png", 100, 50)
egg.dx = 3

egg_list = []
for i in range(10):
    egg = MovingElement(left=i*10, top=i*10)
    egg.dx = i*5
    egg_list.append(egg)

trident = Element("trident60.png", 250, HEIGHT-70)

lost = False
while egg.top <  HEIGHT: 
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    # easter egg movement
    egg.dy += 0.2
    egg.update()    
    egg.angle += 1


    # easter egg bouncing off side walls 
    if egg.left < 0 or egg.right > WIDTH:
        egg.dx = -egg.dx

    #Easter egg bouncing off trident. Trident will stop moving when the game is lost. 
    if not lost:
        trident.left += movement(pygame.K_LEFT, pygame.K_RIGHT, 5)
        if trident.collide(egg):
            egg.dy = -egg.dy
            egg.dx = (egg.left - trident.left)/10
            egg.top = trident.top - egg.height + 5

        if egg.bottom > trident.top + 10:
            lost = True
    else: 
        trident.scale *= 0.9

    background.blit()
    egg.blit()
    trident.blit()
    
    pygame.display.flip()
pygame.quit()
print("Game over")