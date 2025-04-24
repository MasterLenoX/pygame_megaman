import pygame
from sys import exit ##terminate the game

#game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512

#initialize pygame
pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
#window title
pygame.display.set_caption("LENOX GAME: MEGAMAN - Pygame")
#used for the game loop
clock = pygame.time.Clock()


#left (x), top(y), width, height
player = pygame.Rect(125, 150, 20, 20)

def draw():
  # window.fill("blue") - fill color
  # window.fill("#54de9e") - HEX color
  # window.fill((84, 222, 158)) - RGB color
  window.fill((20, 18, 167))
  pygame.draw.rect(window, (2, 239, 238), player)


#using the loop for game
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: #user clicks the X button in pygame window
      pygame.quit()
      exit()

    #KEYDOWN Elements - Key was pressed, KEYUP - key was released
    '''
     if event.type == pygame.KEYDOWN:
       if event.key in (pygame.K_UP, pygame.K_w):
         player.y -= 5
       if event.key in (pygame.K_DOWN, pygame.K_s):
         player.y += 5        
       if event.key in (pygame.K_LEFT, pygame.K_a):
         player.x -= 5
       if event.key in (pygame.K_RIGHT, pygame.K_d):
         player.x += 5
    '''
  #allows to pressed the key hold
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP] or keys[pygame.K_w]:
    player.y -= 5
  if keys[pygame.K_DOWN] or keys[pygame.K_s]:
    player.y += 5
  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    player.x -= 5
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    player.x += 5

  draw()
  pygame.display.update()
  clock.tick(60) #60 frames per seconds 