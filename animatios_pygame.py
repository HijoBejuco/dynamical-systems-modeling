
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        # QUIT means closing the window at the up right x
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    # The second if condition, garantee we dont exit the window.
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        
    if not(isJump): 
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    # Fill again the window with black color.
    win.fill((0,0,0))
    """ 
    Here we draw the rectangle inside the win object.
    COORDENATES:
        The origin of the win, so we use (x,y) coordenates, is the upper left
        corner of the window. so, increasing y drives us towards down and increasing x
        drives us towards right. 
    """
    pygame.draw.rect(win, (255,0,0), (x, y, width, height)) 
    pygame.display.update() 
    
pygame.quit()