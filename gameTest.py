import pygame, os, sys, time
from NewDemon import Demon
from sources import guardianPaths
from NewFactory import Factory
from NewLine import Line
from NewGuardian import Guardian
from sources import guardianPaths

size = width, height = 800, 650
window = pygame.display.set_mode(size)

def main():
     pygame.init()
     green = 0,50,100 
     clock = pygame.time.Clock()
     pygame.key.set_repeat(30)  
     NEW_SOUL = pygame.USEREVENT
     pygame.time.set_timer(NEW_SOUL, 2000)  
     factorySoul = Factory(width, height)  
     player = Guardian(guardianPaths['run-images'], guardianPaths['stop-image'], guardianPaths['jump-image'], 
          guardianPaths['attack-image'], guardianPaths['attack-sound'], [400, 200], 1, 0)
     endingLine = Line(width, 0 )
     window.blit(endingLine.image, endingLine.rect)
     while True: 
          clock.tick(60)  
          window.fill(green) 
          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
               if event.type == NEW_SOUL:  
                    factorySoul.addSoulBasic()
          keysPressed = pygame.key.get_pressed()
          if(keysPressed[pygame.K_SPACE]):
               player.attack(pygame.sprite.spritecollide(player, factorySoul, False))
          if(keysPressed[pygame.K_UP]):
               player.jump()  
          if(keysPressed[pygame.K_LEFT]):
               player.moveLeft(0)
          elif(keysPressed[pygame.K_RIGHT]):
               player.moveRight(width)
          else:
               player.stopWalk() 
          pygame.sprite.spritecollide(endingLine, factorySoul, True)
          factorySoul.draw(window)
          factorySoul.update(0, width, height, 0) #cambiar esto
          #pygame.draw.rect(window, (255, 0, 0), player.rect)
          player.update()
          window.blit(player.image, player.rect) 
          pygame.display.flip() 

if __name__ == '__main__':
    main()