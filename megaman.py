import pygame
from sys import exit ##terminate the game
import os

#game variables
TILE_SIZE = 32
GAME_WIDTH = 512
GAME_HEIGHT = 512

PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 42
PLAYER_HEIGHT = 48
PLAYER_JUMP_WIDTH = 52
PLAYER_JUMP_HEIGHT = 60
PLAYER_DISTANCE = 5

GRAVITY = 0.5
FRICTION = 0.4
PLAYER_VELOCITY_X = 5
PLAYER_VELOCITY_Y = -12
# FLOOR_Y = GAME_HEIGHT * 3/4

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
floor_tile_image = load_image("floor-tile.png", (TILE_SIZE, TILE_SIZE))

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
    self.velocity_x = 0
    self.velocity_y = 0
    self.direction = "right"
    self.jumping = False

  def update_image(self):
    if self.jumping:
      # self.width = PLAYER_JUMP_WIDTH
      # self.height = PLAYER_JUMP_HEIGHT      
      if self.direction == "right":
        self.image = player_image_jump_right
      elif self.direction == "left":
        self.image = player_image_jump_left
    else:
      # self.width = PLAYER_WIDTH
      # self.height = PLAYER_HEIGHT
      if self.direction == "right":
        self.image = player_image_right
      elif self.direction == "left":
        self.image = player_image_left

class Tile(pygame.Rect):
  def __init__(self, x, y, image):
    pygame.Rect.__init__(self, x, y, TILE_SIZE, TILE_SIZE)
    self.image = image

def create_map():
  for i in range(4):
    tile = Tile(player.x + i*TILE_SIZE, player.y + TILE_SIZE*2, floor_tile_image)
    tiles.append(tile)

  for i in range(16):
    tile = Tile(i*TILE_SIZE, player.y + TILE_SIZE*5, floor_tile_image)
    tiles.append(tile)

  for i in range(3):
    tile = Tile(TILE_SIZE*3, (i+10)*TILE_SIZE, floor_tile_image)
    tiles.append(tile)

def check_tile_collision():
  for tile in tiles:
    if player.colliderect(tile):
      return tile
  return None

def check_tile_collision_x():
  tile = check_tile_collision()
  if tile is not None:
    if player.velocity_x < 0:
      player.x = tile.x + tile.width
    elif player.velocity_x > 0:
      player.x = tile.x - player.width
    player.velocity_x = 0

def check_tile_collision_y():
  tile = check_tile_collision()
  if tile is not None:
    if player.velocity_y < 0:
      player.y = tile.y + tile.height
    elif player.velocity_y > 0:
      player.y = tile.y - player.height
      player.jumping = False
    player.velocity_y = 0

def move():
  if player.direction == "left" and player.velocity_x < 0:
    player.velocity_x += FRICTION
  elif player.direction == "right" and player.velocity_x > 0:
    player.velocity_x -= FRICTION
  else:
    player.velocity_x = 0

  player.x += player.velocity_x
  if player.x < 0:
      player.x = 0
  elif player.x + player.width > GAME_WIDTH:
      player.x = GAME_WIDTH - player.width

  check_tile_collision_x()

  player.velocity_y += GRAVITY
  player.y += player.velocity_y

  check_tile_collision_y()

def draw():
  window.fill((20, 18, 167))
  window.blit(background_image, (0, 70))

  for tile in tiles:
    window.blit(tile.image, tile)

  player.update_image()
  window.blit(player.image, player)

#left (x), top(y), width, height
player = Player()
tiles = []
create_map()

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
     
  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    player.velocity_x = -PLAYER_VELOCITY_X
    player.direction = "left"
  
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    player.velocity_x = PLAYER_VELOCITY_X
    player.direction = "right"

  move()
  draw()
  pygame.display.update()
  clock.tick(60) #60 frames per seconds 