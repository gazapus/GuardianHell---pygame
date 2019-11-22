import pygame, random
from Demon import Demon

class DemonFactory(pygame.sprite.Group):
     def __init__(self, _widthScreen, _heightScreen):
          pygame.sprite.Group.__init__(self)
          self.widthScreen = _widthScreen
          self.heightScreen = _heightScreen

     def addDemon(self, startingPosition, demonFlyImagePath, demonFallImagePath, speedX, speedY, _resistance, _fallToHit, _points):
          newDemon = Demon( startingPosition, demonFlyImagePath, demonFallImagePath, speedX, speedY, _resistance, _fallToHit, _points)
          newDemon.rect.x = random.randint(round(newDemon.rect.width/2), self.widthScreen - newDemon.rect.width)
          newDemon.rect.y = self.heightScreen + newDemon.rect.height
          self.add(newDemon)