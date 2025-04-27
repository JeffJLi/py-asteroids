import pygame

from constants import *
from player import *


def main():
  pygame.init()
  
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  Player.containers = (updatables, drawables)
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatables.update(dt)
    
    screen.fill("black")
    for sprite in drawables:
      sprite.draw(screen)
    
    dt = clock.tick(60) / 1000
    pygame.display.flip()

if __name__ == "__main__":
  main()
  