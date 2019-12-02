import pygame
from Enemy import Demon
from sources import guardianPaths
from Factory import Factory
from Line import Line
from Guardian import Guardian
from sources import guardianPaths
from TextOnScreen import TextOnScreen

class Level():
     def __init__(self, width, height, player, backgroundPath, enemiesGoneQuantity=0):
          self.player = player
          self.background = pygame.image.load(backgroundPath)
          self.endingTopLine = Line(width, -400)
          self.endingBottomLine = Line(width, height + 400)
          self.enemiesFactory = Factory(width, height)
          self.treasureFactory = Factory(width, height)
          self.enemiesGoneCounter = TextOnScreen(40, 10, 20, (0,0,0), 'Arial', "Souls Gone", enemiesGoneQuantity)
          self.pointsCounter = TextOnScreen(700, 10, 20, (0,0,0), 'Arial', "Points", player.points)
     
     def initialize(self, window):
          window.blit(self.endingTopLine.image, self.endingTopLine.rect)

     def runBasicEvents(self, events, keysPressed, window, width, height):
          window.blit(self.background, (0,0))
          
          if(keysPressed[pygame.K_SPACE]):
               self.player.attack(pygame.sprite.spritecollide(self.player, self.enemiesFactory, False))
          if(keysPressed[pygame.K_UP]):
               self.player.jump()  
          if(keysPressed[pygame.K_LEFT]):
               self.player.moveLeft(0)
          elif(keysPressed[pygame.K_RIGHT]):
               self.player.moveRight(width)
          else:
               self.player.stopWalk() 

          enemiesGoneList = pygame.sprite.spritecollide(self.endingTopLine, self.enemiesFactory, True)  
          enemiesGoneQuantify = len(enemiesGoneList)           
          pygame.sprite.spritecollide(self.endingTopLine, self.treasureFactory, True)
          pygame.sprite.spritecollide(self.endingBottomLine, self.enemiesFactory, True)
          treasureTaken = pygame.sprite.spritecollide(self.player, self.treasureFactory, False)
          if(treasureTaken):
               self.player.takeTreasure(treasureTaken)
          self.treasureFactory.draw(window)
          self.enemiesFactory.draw(window)
          self.enemiesFactory.update(0, width, height, 0) #cambiar esto ? 
          self.treasureFactory.update(0, width, height, 0) 
          self.pointsCounter.setValue(self.player.points)
          self.enemiesGoneCounter.updateValue(enemiesGoneQuantify)
          self.player.update()
          window.blit(self.player.image, self.player.rect)
          window.blit(self.enemiesGoneCounter.text, self.enemiesGoneCounter.rect)
          window.blit(self.pointsCounter.text, self.pointsCounter.rect)
          pygame.display.flip() 