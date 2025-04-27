import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
  pygame.init()
  
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  Player.containers = (updatables, drawables)
  Asteroid.containers = (asteroids, updatables, drawables)
  AsteroidField.containers = (updatables)
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_fields = AsteroidField()
  
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    updatables.update(dt)
    
    for asteroid in asteroids:
      if asteroid.is_colliding(player):
        raise SystemExit("Game over!")
    
    screen.fill("black")
    for sprite in drawables:
      sprite.draw(screen)
    
    dt = clock.tick(60) / 1000
    pygame.display.flip()

if __name__ == "__main__":
  main()
  