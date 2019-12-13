import pygame, random
from Enemy import Demon
from Item import Item
from sources import soulPaths, soundPaths, fireballPaths, superFireballPaths, coinPaths, diamondPaths, livePaths

class Factory(pygame.sprite.Group):
     def __init__(self, _widthScreen, _heightScreen):
          pygame.sprite.Group.__init__(self)
          self.widthScreen = _widthScreen
          self.heightScreen = _heightScreen

     def addSoulBasic(self):
          newSoul = Demon(soulPaths['new']['up-images'], [0, -5], [0,0] , 25, soulPaths['new']['down-images'], 1,
                     1, 1, 0, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)

     def addSoulBounce(self):
          newSoul = Demon(soulPaths['green']['up-images'], [10, -5], [0,0] , 25, soulPaths['green']['down-images'], 1, 1, 1, 0 , soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerang(self):
          newSoul = Demon(soulPaths['blue']['up-images'], [0, -5], [0,0] , 25, soulPaths['blue']['down-images'], 2, 1, 1, 2 , soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulStrong(self):
          newSoul = Demon(soulPaths['grey']['up-images'], [0, -5], [0,0] , 25, soulPaths['grey']['down-images'], 2, 0, 2, 1, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerangStrong(self):
          newSoul = Demon(soulPaths['grey']['up-images'], [random.randint(-9, 9), -5], [0,0] , 25, soulPaths['grey']['down-images'], 4, 0, 2, 2, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBounceBoomerangStrong(self):
          newSoul = Demon(soulPaths['grey']['up-images'], [random.randint(-9, 9), -5], [0,0] , 25, soulPaths['grey']['down-images'], 3, 0, 2, 2, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)

     def addCoin(self):
          xSpeed = random.randint(-2,2)
          ySpeed = abs(xSpeed) - 5
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newCoin = Item(coinPaths, [xSpeed, ySpeed], [xPosition, yPosition], 25, 10, soundPaths['treasure'])
          self.add(newCoin)

     def addAttack(self):
          xSpeed = random.randint(-2,2)
          ySpeed = abs(xSpeed) - 7
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newFireball = Item(fireballPaths, [xSpeed, ySpeed], [xPosition, yPosition], 25, 1, soundPaths['explosion'])
          self.add(newFireball)
     
     def addSuperAttack(self):
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newFireball = Item(superFireballPaths, [0, -7], [xPosition, yPosition], 25, 1, soundPaths['explosion'])
          self.add(newFireball)

     def addDiamond(self):
          xSpeed = random.randint(-5, 5)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newDiamond = Item(diamondPaths, [xSpeed, -7], [xPosition, yPosition], 25, 50, soundPaths['treasure'])
          self.add(newDiamond)

     def addLive(self):
          xSpeed = random.randint(-5, 5)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newLive = Item(livePaths, [xSpeed, -5], [xPosition, yPosition], 25, 1, soundPaths['live'])
          self.add(newLive)
#ascendingimagesPath, speeds, startingPosition, _pxChange, _points