import pygame
import math 

pygame.init()

screen = pygame.display.set_mode((820,600))

pygame.display.set_caption('Graphs')

Black = (0,0,0)
New_Black = (25,25,25)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)

running = True

while running:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False

     screen.fill(White)
     
     for step in range(20,600,70):
         pygame.draw.line(screen, New_Black, (0,step), (800,step), 1)
    
     for step in range(20,820,130):
         pygame.draw.line(screen, New_Black, (step,0), (step,600), 1)
    
     pygame.draw.line(screen, Black, (0,300), (820,300), 4)

     pygame.draw.line(screen, Black, (410,0), (410,600), 4)

     plotPoints = []
     plotPoints2 = []
     
     for x in range(20, 800):
     
         y = int(math.sin(x/820.0 * 6 * math.pi) * 280 + 300)
     
         plotPoints.append([x, y])
    
     for a in range(20, 800):
     
         b = int(math.cos(a/820.0 * 6 * math.pi) * 280 + 300)
     
         plotPoints2.append([a, b])
     
     pygame.draw.lines(screen, Red, False, plotPoints, 2)
     pygame.draw.lines(screen, Blue, False, plotPoints2, 2)

     pygame.display.flip()


pygame.quit()