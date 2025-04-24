import pygame
from sys import exit ##terminate the game
import os

#game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512

PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 42
PLAYER_HEIGHT = 48
PLAYER_DISTANCE = 5
PLAYER_JUMP_WIDTH = 52
PLAYER_JUMP_HEIGHT = 65

GRAVITY = 0.5
PLAYER_VELOCITY_Y = -10
FLOOR_Y = GAME_HEIGHT * 3/4

#images
def load_image(image_name, scale = None):
  image = pygame.image.load(os.path.join("images", image_name))
  if scale is not None:
    image = pygame.transform.scale(image, scale)
  return image

background_image = load_image("background.png")
player_image_right = load_image("megaman-right.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_left = load_image("megaman-left.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_jump_right = load_image("megaman-right-jump.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_jump_left = load_image("megaman-left-jump.png", (PLAYER_WIDTH, PLAYER_HEIGHT))

#initialize pygame
pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
#window title
pygame.display.set_caption("LENOX GAME: MEGAMAN - Pygame")
#pygame megaman logo
pygame.display.set_icon(player_image_right)
#used for the game loop
clock = pygame.time.Clock()


class Player(pygame.Rect):
  def __init__(self):
    pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    self.image = player_image_right
    self.velocity_y = 0
    self.direction = "right"
    self.jumping = False

  def update_image(self):
    if self.jumping:
      self.width = PLAYER_JUMP_WIDTH
      self.height = PLAYER_JUMP_HEIGHT      
      if self.direction == "right":
        self.image = player_image_jump_right
      elif self.direction == "left":
        self.image = player_image_jump_left
    else:
      self.width = PLAYER_WIDTH
      self.height = PLAYER_HEIGHT
      if self.direction == "right":
        self.image = player_image_right
      elif self.direction == "left":
        self.image = player_image_left

#left (x), top(y), width, height
player = Player()

def move():
  player.velocity_y += GRAVITY
  player.y += player.velocity_y

  if player.y + player.height > FLOOR_Y:
    player.y = FLOOR_Y - player.height
    player.jumping = False

def draw():
  window.fill((20, 18, 167))
  window.blit(background_image, (0, 70))
  player.update_image()
  window.blit(player.image, player)


#using the loop for game
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: #user clicks the X button in pygame window
      pygame.quit()
      exit()


  #allows to pressed the key hold
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP] or keys[pygame.K_w] and not player.jumping:
    player.velocity_y = PLAYER_VELOCITY_Y
    player.jumping = True
     
  if keys[pygame.K_LEFT] or keys[pygame.K_a] :
    player.x = max(player.x - PLAYER_DISTANCE, 0)
    player.direction = "left"
  
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    player.x = min(player.x + PLAYER_DISTANCE, GAME_WIDTH - player.width)
    player.direction = "right"

  move()
  draw()
  pygame.display.update()
  clock.tick(60) #60 frames per seconds 