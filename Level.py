import pygame
from Enemy import Demon
from Factory import Factory
from Line import Line
from Guardian import Guardian
from TextOnScreen import TextOnScreen
from threading import Timer
class Level():
     def __init__(self, width, height, player, backgroundPath, enemiesGoneQuantity=0):
          self.player = player
          self.bridge = pygame.image.load('./src/images/background/bridge.png')
          self.bridgeYPosition = player.rect.y + player.rect.height - 10
          self.background = pygame.image.load(backgroundPath)
          self.endingTopLine = Line(width, -400)
          self.endingBottomLine = Line(width, height + 400)
          self.enemiesFactory = Factory(width, height)
          self.treasureFactory = Factory(width, height)
          self.attacksFactory = Factory(width, height)
          self.livesFactory = Factory(width, height)
          self.enemiesGoneCounter = TextOnScreen(50, 10, 18, (250, 250, 250), 'rockwell', "Escaped", enemiesGoneQuantity)
          self.pointsCounter = TextOnScreen(700, 10, 18, (250, 250, 250), 'rockwell', "Points", player.points)
          self.livesCounter = TextOnScreen(400, 10, 18, (250, 250, 250), 'rockwell', "Lives", player.lives)          

     def initialize(self, *others):
          self.enemiesFactory.empty()
          self.treasureFactory.empty()
          self.attacksFactory.empty()
          self.livesFactory.empty()
          
     def runBasicEvents(self, events, keysPressed, window, width, height):
          window.blit(self.background, (0,0))
          window.blit(self.bridge, (0, self.bridgeYPosition))
          
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
          treasureTaken = pygame.sprite.spritecollide(self.player, self.treasureFactory, False)
          if(treasureTaken):
               self.player.getTreasure(treasureTaken)
          attacksTaken = pygame.sprite.spritecollide(self.player, self.attacksFactory, False)
          if(attacksTaken):
               self.player.getAttack(attacksTaken)
          livesTaken = pygame.sprite.spritecollide(self.player, self.livesFactory, False)
          if(livesTaken):
               self.player.getLives(livesTaken)
          self.treasureFactory.draw(window)
          self.enemiesFactory.draw(window)
          self.attacksFactory.draw(window)
          self.livesFactory.draw(window)
          self.enemiesFactory.update(0, width, height, 0) #cambiar esto ? 
          self.treasureFactory.update(0, width, height, 0) 
          self.attacksFactory.update(0, width, height, 0)
          self.livesFactory.update(0, width, height, 0)
          self.pointsCounter.setValue(self.player.points)
          self.enemiesGoneCounter.updateValue(enemiesGoneQuantify)
          self.livesCounter.setValue(self.player.lives)
          self.player.update()
          window.blit(self.player.image, self.player.rect)
          window.blit(self.enemiesGoneCounter.text, self.enemiesGoneCounter.rect)
          window.blit(self.pointsCounter.text, self.pointsCounter.rect)
          window.blit(self.livesCounter.text, self.livesCounter.rect)
          pygame.display.flip() 