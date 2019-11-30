import pygame, random
from NewDemon import Demon
from sources import soulPaths

class Factory(pygame.sprite.Group):
     def __init__(self, _widthScreen, _heightScreen):
          pygame.sprite.Group.__init__(self)
          self.widthScreen = _widthScreen
          self.heightScreen = _heightScreen

     def addSoulBasic(self):
          newSoul = Demon(soulPaths['up-images'], [0, -5], [0,0] , 25, soulPaths['down-images'], 1,
                     1, 1, 0 )
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)

     def addSoulBounce(self):
          newSoul = Demon(soulPaths['up-images'], [10, -5], [0,0] , 25, soulPaths['down-images'], 1, 1, 1, 0 )
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerang(self):
          newSoul = Demon(soulPaths['up-images'], [0, -5], [0,0] , 25, soulPaths['down-images'], 2, 1, 1, 2 )
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulStrong(self):
          newSoul = Demon(soulPaths['up-images'], [0, -5], [0,0] , 25, soulPaths['down-images'], 2, 0, 2, 1)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerangStrong(self):
          newSoul = Demon(soulPaths['up-images'], [random.randint(-9, 9), -5], [0,0] , 25, soulPaths['down-images'], 4, 0, 2, 2)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBounceBoomerangStrong(self):
          newSoul = Demon(soulPaths['up-images'], [random.randint(-9, 9), -5], [0,0] , 25, soulPaths['down-images'], 3, 0, 2, 2)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
"""
images, speeds, posotion, _pxChange, images, _hp, _points, _damageNecessaryToFall, _timeFalling"""