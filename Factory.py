import pygame, random
from Demon import Demon
from Treasure import Treasure

class Factory(pygame.sprite.Group):
     def __init__(self, _widthScreen, _heightScreen):
          pygame.sprite.Group.__init__(self)
          self.widthScreen = _widthScreen
          self.heightScreen = _heightScreen

     def addDemon(self, startingPosition, demonFlyImagePath, demonFlyImagePath2,  demonFallImagePath, speedX, speedY, _resistance, _fallToHit, _points):
          newDemon = Demon( startingPosition, demonFlyImagePath, demonFlyImagePath2, demonFallImagePath, speedX, speedY, _resistance, _fallToHit, _points)
          newDemon.rect.x = random.randint(round(newDemon.rect.width/2), self.widthScreen - newDemon.rect.width)
          newDemon.rect.y = self.heightScreen + newDemon.rect.height
          self.add(newDemon)

     def addTreasure(self, startingPosition, imagePath, speedX, speedY, points):
          newCoin = Treasure(startingPosition, imagePath, speedX, speedY, points)
          newCoin.rect.x = random.randint(round(newCoin.rect.width/2), self.widthScreen - newCoin.rect.width)
          newCoin.rect.y = self.heightScreen + newCoin.rect.height
          self.add(newCoin)
