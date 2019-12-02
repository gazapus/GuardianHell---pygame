import pygame, os, sys, time
from Enemy import Demon
from sources import guardianPaths
from Factory import Factory
from Line import Line
from Guardian import Guardian
from sources import guardianPaths
from TextOnScreen import TextOnScreen

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
     factoryTreasure = Factory(width, height)  
     player = Guardian(guardianPaths['run-images'], guardianPaths['stop-image'], guardianPaths['jump-image'], 
          guardianPaths['attack-image'], guardianPaths['attack-sound'], [400, 200], 1, 0)
     endingTopLine = Line(width, 0 )
     endingBottomLine = Line(width, height + 400)
     pointsCounter = TextOnScreen(40, 10, 20, (100, 100, 100), 'Arial', "puntos", 0)
     soulsGone = TextOnScreen(width - 100, 10, 20, (100, 100, 100), 'Arial', "escapados", 0)
     soulsGoneQuantify = 0
     window.blit(endingTopLine.image, endingTopLine.rect)
     window.blit(endingBottomLine.image, endingBottomLine.rect)
     while True: 
          clock.tick(60)  
          window.fill(green) 
          for event in pygame.event.get():  
               if event.type == pygame.QUIT: 
                    sys.exit()
               if event.type == NEW_SOUL:  
                    factorySoul.addSoulBasic()
                    factoryTreasure.addCoin()
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
          soulsGoneList = pygame.sprite.spritecollide(endingTopLine, factorySoul, True)    
          soulsGoneQuantify += len(soulsGoneList)           
          pygame.sprite.spritecollide(endingTopLine, factoryTreasure, True)
          dd = pygame.sprite.spritecollide(endingBottomLine, factorySoul, True)
          treasureTaken = pygame.sprite.spritecollide(player, factoryTreasure, False)
          if(treasureTaken):
               player.takeTreasure(treasureTaken)
          factoryTreasure.draw(window)
          factorySoul.draw(window)
          factorySoul.update(0, width, height, 0) #cambiar esto
          factoryTreasure.update(0, width, height, 0) 
          pointsCounter.setValue(player.points)
          soulsGone.setValue(soulsGoneQuantify)
          #pygame.draw.rect(window, (255, 0, 0), player.rect)
          player.update()
          window.blit(player.image, player.rect)
          window.blit(soulsGone.text, soulsGone.rect)
          window.blit(pointsCounter.text, pointsCounter.rect)
          pygame.display.flip() 

if __name__ == '__main__':
    main()