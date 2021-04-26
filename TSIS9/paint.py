import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

color = WHITE
radius = 3

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None
rectangle1, rectangle2 = None, None
screen.fill(BLACK)

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      game_over = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      prev = pygame.mouse.get_pos()
    if event.type == pygame.K_SPACE:
      if color != BLACK:
        color = BLACK
        radius = 5
    if event.type == pygame.K_r:
      color = RED
    if event.type == pygame.K_w:
      color = WHITE
    if event.type == pygame.K_b:
      color = BLUE
    if event.type == pygame.K_g:
      color = GREEN
    if event.type == pygame.MOUSEMOTION:
      cur = pygame.mouse.get_pos()
      if prev:
        pygame.draw.line(screen, color, prev, cur, radius)
        prev = cur
    if event.type == pygame.MOUSEBUTTONUP:
      prev = None
    if event.type == pygame.MOUSEBUTTONDOWN and event.type == pygame.K_c:
      pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 10)
    if event.type == pygame.MOUSEBUTTONDOWN and event.type == pygame.K_r:
      rectangle1 = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP and event.type == pygame.K_r:
      rectangle2 = pygame.mouse.get_pos()
      pygame.draw.rect(screen,color,[rectangle1[0], rectangle1[1], (rectangle2[0] - rectangle1[0]), (rectangle2[1] - rectangle1[1])])
    
    
  pygame.display.flip()

  clock.tick(30)


pygame.quit()