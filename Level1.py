import pygame, os, sys, time
from Guardian import Guardian
from Demon import Demon
from Factory import Factory
from EndingLine import EndingLine
from TextOnScreen import TextOnScreen

class Level(pygame.sprite.Sprite):
     def __init__(self, width, height, player):
          self.widthScreen = width
          self.heightScreen = height    # ver si lo uso
          self.background = pygame.image.load("./src/images/level1.jpg")
          self.player = player
          self.endingTopLine = EndingLine(width, -80)
          self.endingBottomLine = EndingLine(width, height + 300)
          self.demonFactory = Factory(width, height)
          self.treasureFactory = Factory(width, height)
          self.demonsGoneQuantity = TextOnScreen(100, 20, 15, (0,0,0), 'Arial', "Demons Gone: ", 0)
          self.pointsOnScreen = TextOnScreen(700, 20, 15, (0,0,0), 'Arial', "Points: ", 0)
          #DECLARACION DE EVENTOS (FABRICACIÓN DE DEMONIO)
          self.NEW_DEMON_RED = pygame.USEREVENT
          self.NEW_DEMON_BLUE = pygame.USEREVENT + 1
          self.NEW_DEMON_YELLOW = pygame.USEREVENT + 2
          self.NEW_COIN = pygame.USEREVENT + 3
          pygame.time.set_timer(self.NEW_DEMON_RED, 2000)
          pygame.time.set_timer(self.NEW_DEMON_BLUE, 4500)
          pygame.time.set_timer(self.NEW_DEMON_YELLOW, 5000)
          pygame.time.set_timer(self.NEW_COIN, 4000)
     
     def initialize(self, window):
          window.blit(self.background, (0,0))
          window.fill((50, 200, 100)) 
          window.blit(self.endingTopLine.image, self.endingTopLine.rect)

     def runEvents(self, events, keysPressed, window):
          window.blit(self.background, (0,0))
          window.blit(self.endingTopLine.image, self.endingTopLine.rect)
          for event in events:  
               if event.type == pygame.QUIT: 
                    sys.exit()
               if event.type == self.NEW_DEMON_RED:   
                    self.demonFactory.addDemon((0,0), "./src/images/ghost1a.png", "./src/images/ghos1b.png", "./src/images/ghost1f.png", 0, -2, 2, False, 1)
               if event.type == self.NEW_DEMON_BLUE:
                    self.demonFactory.addDemon((0,0), "./src/images/demon2.png", "./src/images/demon2.png", "./src/images/demon2fall.png", 0, -4, 2, True, 1)
               if event.type == self.NEW_DEMON_YELLOW:
                    self.demonFactory.addDemon((0,0), "./src/images/demon3.png", "./src/images/demon3.png", "./src/images/demon3fall.png", 2, -3, 1, True, 1)
               if event.type == self.NEW_COIN:
                    self.treasureFactory.addTreasure((0,0), "./src/images/goldcoin.png", 0, -3, 10)
               
               if(keysPressed[pygame.K_SPACE]):
                    demonsAttacked = pygame.sprite.spritecollide(self.player, self.demonFactory, False)
                    self.player.attack(demonsAttacked)
               if(keysPressed[pygame.K_LEFT]):
                    self.player.moveLeft(0)
               if(keysPressed[pygame.K_RIGHT]):
                    self.player.moveRight(self.width)
               if(keysPressed[pygame.K_UP]):
                    self.player.jump()

          self.player.update()
          window.blit(self.player.image, self.player.rect) 
          treasuresTaken = pygame.sprite.spritecollide(self.player, self.treasureFactory, False)
          self.player.takeTreasure(treasuresTaken)
          pygame.sprite.spritecollide(self.endingBottomLine, self.demonFactory, True)
          demonsGone = pygame.sprite.spritecollide(self.endingTopLine, self.demonFactory, True)
          self.demonsGoneQuantity.update(len(demonsGone))
          window.blit(self.demonsGoneQuantity.text, self.demonsGoneQuantity.rect)
          self.pointsOnScreen.setValue(self.player.points)
          window.blit(self.pointsOnScreen.text, self.pointsOnScreen.rect)
          self.demonFactory.draw(window)
          self.demonFactory.update()
          self.treasureFactory.draw(window)
          self.treasureFactory.update()
          pygame.display.flip() 

          return {}