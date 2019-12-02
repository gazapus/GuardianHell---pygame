import pygame, os, sys, time
from Enemy import Demon
from sources import guardianPaths
from Factory import Factory
from Line import Line
from Guardian import Guardian
from sources import guardianPaths
from TextOnScreen import TextOnScreen
from Level import Level

class Level1(Level):
     def __init__(self, width, height, player):
          super().__init__(width, height, player, "./src/images/hell.jpg")
          self.NEW_SOUL = pygame.USEREVENT
          self.NEW_COIN = pygame.USEREVENT + 1
          pygame.time.set_timer(self.NEW_SOUL, 2000)
          pygame.time.set_timer(self.NEW_COIN, 4500)

     def runEvents(self, events, keysPressed, window, width, height):
          super().runBasicEvents(events, keysPressed, window, width, height)
          for event in events:  
               if event.type == self.NEW_SOUL:  
                    self.enemiesFactory.addSoulBasic()
               if event.type == self.NEW_COIN:
                    self.treasureFactory.addCoin()
          return {}

         