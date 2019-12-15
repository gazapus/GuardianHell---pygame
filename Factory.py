import pygame, random
from Enemy import Demon
from Item import Item
from sources import soulPaths, soundPaths, fireballPaths, coinPaths, diamondPaths, livePaths

class Factory(pygame.sprite.Group):
     def __init__(self, _widthScreen, _heightScreen):
          pygame.sprite.Group.__init__(self)
          self.widthScreen = _widthScreen
          self.heightScreen = _heightScreen

     def addSoulBasic(self):
          newSoul = Demon(soulPaths['grey']['up-images'], [0, -4], [0,0] , 25, soulPaths['grey']['down-images'], 1,
                     10, 1, 0, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)

     def addSoulBounce(self):
          newSoul = Demon(soulPaths['green']['up-images'], [4, -4], [0,0] , 25, soulPaths['green']['down-images'], 1, 15, 1, 0 , soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerang(self):
          newSoul = Demon(soulPaths['blue']['up-images'], [0, -5], [0,0] , 25, soulPaths['blue']['down-images'], 2, 20, 1, 3 , soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulStrong(self):
          newSoul = Demon(soulPaths['orange']['up-images'], [0, -4], [0,0] , 25, soulPaths['orange']['down-images'], 2, 25, 2, 1, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerangStrong(self):
          newSoul = Demon(soulPaths['yellow']['up-images'], [0, -4], [0,0] , 25, soulPaths['yellow']['down-images'], 3, 40, 2, 2, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBonceBoomerang(self):
          newSoul = Demon(soulPaths['white']['up-images'], [random.randint(-4, 4), -3], [0,0] , 25, soulPaths['white']['down-images'], 3, 60, 1, 3, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)

     def addFireball(self):
          xSpeed = random.randint(-3,3)
          ySpeed = random.randint(-4,-2)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newFireball = Item(fireballPaths["fireball"], [xSpeed, ySpeed], [xPosition, yPosition], 25, 1, soundPaths['explosion'])
          self.add(newFireball)
     
     def addSuperFireball(self):
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newFireball = Item(fireballPaths["superfireball"], [0, -7], [xPosition, yPosition], 25, 1, soundPaths['explosion2'])
          self.add(newFireball)

     def addCoin(self):
          xSpeed = random.randint(-2,2)
          ySpeed = abs(xSpeed) - 5
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newCoin = Item(coinPaths, [xSpeed, ySpeed], [xPosition, yPosition], 25, 5, soundPaths['treasure'])
          self.add(newCoin)

     def addDiamond(self):
          xSpeed = random.randint(-5, 5)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newDiamond = Item(diamondPaths, [xSpeed, -7], [xPosition, yPosition], 25, 10, soundPaths['treasure'])
          self.add(newDiamond)

     def addLive(self):
          xSpeed = random.randint(-5, 5)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newLive = Item(livePaths, [xSpeed, -5], [xPosition, yPosition], 25, 1, soundPaths['live'])
          self.add(newLive)