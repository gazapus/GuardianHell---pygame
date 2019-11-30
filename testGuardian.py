import pygame, os, sys, time
from ClimbingObject import ClimbingObject
from NewDemon import Demon
from Item import Item
from GuardianTest import Guardian
from sources import guardianPaths

size = width, height = 800, 650
window = pygame.display.set_mode(size)

def main():
     pygame.init()
     green = 0,50,100 
     clock = pygame.time.Clock()
     pygame.key.set_repeat(30)      
     player = Guardian(guardianPaths['run-images'], guardianPaths['stop-image'], guardianPaths['jump-image'], 
          guardianPaths['attack-image'], guardianPaths['attack-sound'], [400, 200], 1, 0)
     while True: 
          clock.tick(60)  
          window.fill(green) 
          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
          keysPressed = pygame.key.get_pressed()
          if(keysPressed[pygame.K_SPACE]):
               player.attack()
          if(keysPressed[pygame.K_UP]):
               player.jump()  
          if(keysPressed[pygame.K_LEFT]):
               player.moveLeft(0)
          elif(keysPressed[pygame.K_RIGHT]):
               player.moveRight(width)
          else:
               player.stopWalk() 
          player.update()
          window.blit(player.image, player.rect) 
          pygame.display.flip() 

if __name__ == '__main__':
    main()