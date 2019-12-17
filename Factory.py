import pygame, random
from Enemy import Demon
from Item import Item
from sources import soulPaths, soundPaths, fireballPaths, coinPaths, diamondPaths, livePaths

class Factory(pygame.sprite.Group):
     """
     this class groups the objects that are generated in the levels
     """
     def __init__(self, _widthScreen, _heightScreen):
          pygame.sprite.Group.__init__(self)
          self.widthScreen = _widthScreen
          self.heightScreen = _heightScreen

     def addSoulBasic(self):
          """
          add a soul-like enemy that ascends vertically and dies at once
          """
          newSoul = Demon(soulPaths['grey']['up-images'], [0, -4], [0,0] , 25, soulPaths['grey']['down-images'], 1,
                     10, 1, 0, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)

     def addSoulBounce(self):
          """
          add a soul-like enemy that ascends diagonally and dies at once
          """
          newSoul = Demon(soulPaths['green']['up-images'], [4, -3], [0,0] , 25, soulPaths['green']['down-images'], 1, 15, 1, 0 , soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerang(self):
          """
          add a soul-like enemy that ascends vertically, falls with one blow and dies with two blows
          """
          newSoul = Demon(soulPaths['blue']['up-images'], [0, -5], [0,0] , 25, soulPaths['blue']['down-images'], 2, 20, 1, 3 , soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulStrong(self):
          """
          add a soul-like enemy that ascends vertically and dies of two blows
          """
          newSoul = Demon(soulPaths['orange']['up-images'], [0, -3], [0,0] , 25, soulPaths['orange']['down-images'], 2, 25, 2, 1, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBoomerangStrong(self):
          """
          add a soul-like enemy that ascends vertically, falls from two strokes and dies from three strokes
          """
          newSoul = Demon(soulPaths['yellow']['up-images'], [0, -3], [0,0] , 25, soulPaths['yellow']['down-images'], 3, 40, 2, 2, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)
     
     def addSoulBonceBoomerang(self):
          """
          add a soul-like enemy that ascends diagonally, falls from one blow and dies from three blows
          """
          newSoul = Demon(soulPaths['white']['up-images'], [random.randint(-3, 4), -3], [0,0] , 25, soulPaths['white']['down-images'], 3, 60, 1, 3, soundPaths)
          newSoul.rect.x = random.randint(round(newSoul.rect.width/2), self.widthScreen - newSoul.rect.width)
          newSoul.rect.y = self.heightScreen + newSoul.rect.height
          self.add(newSoul)

     def addFireball(self):
          """
          add a fireball attack that ascends slowly diagonally
          """
          xSpeed = random.randint(-2,2)
          ySpeed = random.randint(-4,-2)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newFireball = Item(fireballPaths["fireball"], [xSpeed, ySpeed], [xPosition, yPosition], 25, 1, soundPaths['explosion'])
          self.add(newFireball)
     
     def addSuperFireball(self):
          """
          add a large fireball attack that ascends quickly vertically
          """
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newFireball = Item(fireballPaths["superfireball"], [0, -8], [xPosition, yPosition], 25, 1, soundPaths['explosion2'])
          self.add(newFireball)

     def addCoin(self):
          """
          add a treasure coin that ascens diagnoally and let 5 points
          """
          xSpeed = random.randint(-2,2)
          ySpeed = abs(xSpeed) - 5
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newCoin = Item(coinPaths, [xSpeed, ySpeed], [xPosition, yPosition], 25, 5, soundPaths['treasure'])
          self.add(newCoin)

     def addDiamond(self):
          """
          add a treasure diamond that ascends quickly diagonally and let 10 points
          """
          xSpeed = random.randint(-5, 5)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newDiamond = Item(diamondPaths, [xSpeed, -7], [xPosition, yPosition], 25, 10, soundPaths['treasure'])
          self.add(newDiamond)

     def addLive(self):
          """
          add a life that ascends diagonally   
          """
          xSpeed = random.randint(-5, 5)
          xPosition = random.randint(50, self.widthScreen - 50)
          yPosition = self.heightScreen +  50
          newLive = Item(livePaths, [xSpeed, -4], [xPosition, yPosition], 25, 1, soundPaths['live'])
          self.add(newLive)