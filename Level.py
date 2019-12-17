import pygame
from Enemy import Demon
from Factory import Factory
from Line import Line
from Guardian import Guardian
from TextOnScreen import TextOnScreen
from threading import Timer
class Level():
     """
     This class allows the user to generate the levels from instantiating classes that inherit it
     """
     def __init__(self, width, height, player, backgroundPath):
          """
          :param width: width of the screen
          :param height: height of the screen
          :param player: instance of the player class
          :param backgroundPath: background image path of the level           
          """
          self.player = player
          self.bridge = pygame.image.load('./src/images/background/bridge.png')
          #bridge position where the player will stand
          self.bridgeYPosition = 190
          self.background = pygame.image.load(backgroundPath)
          #the lines are the limits where the objects that reach it will be removed
          self.endingTopLine = Line(width, -400)
          self.endingBottomLine = Line(width, height + 400)
          #the factories are the generators of the objects on the screen
          self.enemiesFactory = Factory(width, height)
          self.treasureFactory = Factory(width, height)
          self.attacksFactory = Factory(width, height)
          self.livesFactory = Factory(width, height)
          #this will be the counter of the escaping enemies
          self.enemiesGoneCounter = TextOnScreen(50, 10, 18, (250, 250, 250), 'rockwell', "Escaped", 0)
          #Player points counter that will be visible on the screen level 
          self.pointsCounter = TextOnScreen(700, 10, 18, (250, 250, 250), 'rockwell', "Points", player.points)
          #Player lives counter that will be visible on the screen level 
          self.livesCounter = TextOnScreen(400, 10, 18, (250, 250, 250), 'rockwell', "Lives", player.lives)          

     def initialize(self, *others):
          """
          initialize the factories by emptying them in case there are any left objects from the previous game
          """
          self.enemiesFactory.empty()
          self.treasureFactory.empty()
          self.attacksFactory.empty()
          self.livesFactory.empty()
          
     def runBasicEvents(self, events, keysPressed, window, width, height):
          """
          runs the basic behavior that every level has
          params:
          :param events: events list ocurred
          :param keysPressed: keys pressed
          :param window: game window
          :param width: width of the screen
          :param height: height of the screen      
          """
          window.blit(self.background, (0,0))
          window.blit(self.bridge, (0, self.bridgeYPosition))
          
          if(keysPressed[pygame.K_SPACE]):
               #Run the player attack event and send as parameter the list of enemies that he hits, if any
               self.player.attack(pygame.sprite.spritecollide(self.player, self.enemiesFactory, False))
          if(keysPressed[pygame.K_UP]):
               self.player.jump()  
          if(keysPressed[pygame.K_LEFT]):
               self.player.moveLeft(0)
          elif(keysPressed[pygame.K_RIGHT]):
               self.player.moveRight(width)
          else:
               self.player.stopWalk() 
          #Count the number of enemies that escaped upon reaching the upper limit line
          enemiesGoneList = pygame.sprite.spritecollide(self.endingTopLine, self.enemiesFactory, True)  
          enemiesGoneQuantify = len(enemiesGoneList)  
          #Load the treasures the player has reached        
          treasureTaken = pygame.sprite.spritecollide(self.player, self.treasureFactory, False)
          if(treasureTaken):
               self.player.getTreasure(treasureTaken)
          #subtracts lives from the player in case of being hit by an attacking object
          attacksTaken = pygame.sprite.spritecollide(self.player, self.attacksFactory, False)
          if(attacksTaken):
               self.player.getAttack(attacksTaken)
          #add lives to the player in case of reaching any life object
          livesTaken = pygame.sprite.spritecollide(self.player, self.livesFactory, False)
          if(livesTaken):
               self.player.getLives(livesTaken)
          #update and rendering of screen objects
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