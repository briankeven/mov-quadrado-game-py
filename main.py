import pygame
import random
import sys

pygame.init()

window = pygame.display.set_mode([800, 580])

spaceship = pygame.image.load('spaceship.png')

imgX = 350
imgY = 400
speedX = 0

alt=150
larg=100
quadX= random.randrange(0, 700)
quadY=0
speedY = 2

clock = pygame.time.Clock()
while True:
  
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        speedX = -10
      if event.key == pygame.K_RIGHT:
        speedX = 10

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        speedX = 0
      if event.key == pygame.K_RIGHT:
        speedX = 0

  window.fill((255, 255, 255))

  window.blit(spaceship, [imgX, imgY])

  pygame.draw.rect(window, (0,0,255),[quadX,quadY,larg,alt])

  imgX += speedX
  quadY +=speedY

  
  if quadY > 580:
    quadY=0
    quadX = random.randrange(0, 700)
    larg+=1
  
  if imgY < quadY + 100 and imgY + 128 > quadY:
    if imgX < quadX + 90 and imgX + 90 > quadX:
      sys.exit()

  pygame.display.update()
  clock.tick(30)