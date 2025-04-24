import pygame
from sys import exit ##terminate the game

#game variables
GAME_WIDTH = 624
GAME_HEIGHT = 624

#initialize pygame
pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

#window title
pygame.display.set_caption("LENOX GAME: MEGAMAN - Pygame")
clock = pygame.time.Clock()


#left (x), top(y), width, height
player = pygame.Rect(200, 150, 150, 50)


#using the loop for game
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()


  pygame.display.update()
  clock.tick(60) #60 frames per seconds 