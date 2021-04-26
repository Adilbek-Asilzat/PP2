import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FOOD = (230,29,194)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()

radius = 10
body = [[100, 100], [0, 0], [0, 0]]
body2 = [[300, 300], [0, 0], [0, 0]]

block = 15
dx, dy = block, 0
dx2, dy2 = block, 0

def own_round(value, base=10):
  return base * round(value / 10)

def set_random_position():
  return own_round(random.randint(0, WINDOW_WIDTH)), own_round(random.randint(0, WINDOW_HEIGHT))

food_x, food_y = set_random_position()
food_x2, food_y2 = set_random_position()

game_over = False
speed = True

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        dx = block
        dy = 0
      if event.key == pygame.K_LEFT:
        dx = -block
        dy = 0
      if event.key == pygame.K_UP:
        dx = 0
        dy = -block
      if event.key == pygame.K_DOWN:
        dx = 0
        dy = block
      if event.key == pygame.K_SPACE:
        body.append([0, 0])
        food_x, food_y = set_random_position()
      if event.key == pygame.K_d:
        dx2 = block
        dy2 = 0
      if event.key == pygame.K_a:
        dx2 = -block
        dy2 = 0
      if event.key == pygame.K_w:
        dx2 = 0
        dy2 = -block
      if event.key == pygame.K_s:
        dx2 = 0
        dy2 = block
      if event.key == pygame.K_x:
        body2.append([0, 0])
      if event.key == pygame.K_p:
         speed = False
    
  
  for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0]
    body[i][1] = body[i - 1][1]
  
  body[0][0] += dx
  body[0][1] += dy

  for i in range(len(body2) - 1, 0, -1):
    body2[i][0] = body2[i - 1][0]
    body2[i][1] = body2[i - 1][1]

  body2[0][0] += dx2
  body2[0][1] += dy2

  screen.fill(BLACK)

  pygame.draw.circle(screen, FOOD, (food_x, food_y), radius)
  
  pygame.draw.rect(screen, WHITE, (0,200,100,20))
  pygame.draw.rect(screen, WHITE, (200,300,400,20))
  pygame.draw.rect(screen, WHITE, (200,100,20,200))
  pygame.draw.rect(screen, WHITE, (100,400,20,100))

  for i, (x, y) in enumerate(body):
    color = RED if i == 0 else GREEN
    pygame.draw.circle(screen, color, (x, y), radius)

  for i2, (x2, y2) in enumerate(body2):
    color2 = BLUE if i2 == 0 else GREEN
    pygame.draw.circle(screen, color2, (x2, y2), radius)

  pygame.display.flip()

  if speed:
    clock.tick(4)
  else:
    clock.tick(8)


pygame.quit()