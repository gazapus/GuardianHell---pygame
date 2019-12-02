import pygame
from threading import Timer
from ClimbingObject import ClimbingObject

class Demon(ClimbingObject):
     def __init__(
               self, ascendingimagesPath, speeds, startingPosition, _pxChange,
               descedingImagesPath, _hp, _points, _damageNecessaryToFall, _timeFalling 
               ):
          """
               Parameters
               ----------
               ascendingimagesPath : list
                    list of paths of ascent images
               speeds : list
                    list of two values containing the velocity on the x-axis and on the y-axis
               startingPosition : list
                    list of two values containing the starting position in the x-axis and y-axis
               _pxChange: int
                    define how many pixels of the "y axis" will change the image
               descedingImagesPath: list
                    list of paths of desendent images
               _hp: int
                    number of health points, that is, resistance to attacks
               _points: int
                    number of points returned when hp reaches zero
               _damageNecessaryToFall: int
                    amount of damage (hp reduction) it supports until it falls
               _timeFalling: int
                    number of seconds that will fall when it reaches its maximum damage to fall and still have hp
               ----------
          """
          super().__init__(ascendingimagesPath, speeds, startingPosition, _pxChange)
          self.descedingImages = self.setImages(descedingImagesPath)
          self.hitImage = self.fill(ascendingimagesPath[0], 250, 250, 250)  
          self.originalSpeeds = [speeds[0], speeds[1]] #PARCHE ?
          self.points = _points
          self.hp = _hp
          self.timeFalling = _timeFalling
          self.damageNecessaryToFall = _damageNecessaryToFall
          self.currentDamageReceived = 0
          self.isFalling = False

     def updateImage(self):
          """@override: Update image object"""
          # if the object isn't falling
          # the position is compared with the last position where there has been an ascending image change
          # if it has moved far enough, it changes its image
          if(not self.isFalling and self.rect.y < self.lastYPosition - self.pxChange):
               self.image = next(self.ascendingimages)
               self.lastYPosition = self.rect.y
          # the position is compared with the last position where there has been an falling image change
          elif(self.rect.y > self.lastYPosition + self.pxChange):
               self.image = next(self.descedingImages)
               self.lastYPosition = self.rect.y

     def getAttack(self, hitDamage):
          """
          the object is attacked: the hp is reduced and maybe falls
          :params int hitDamage: quantity of hp to be reduced
          """
          #amount of points that will be retuned if the object dies (hp = 0)
          pointsToReturn = 0
          if(not self.isFalling):
               self.hp -= hitDamage
               self.currentDamageReceived += hitDamage
               if(self.hp <= 0):
                    pointsToReturn = self.points
                    self.fall()
               #if the object is falls but still lives, its return flight is scheduled
               elif(self.currentDamageReceived >= self.damageNecessaryToFall):
                    self.fall()
                    self.currentDamageReceived = 0
                    Timer(self.timeFalling, self.turnBackFly).start()
               #if the object not falls, this one continues its way
               else:
                    self.speed[1] = self.originalSpeeds[1] - round(self.originalSpeeds[1]/2)
                    self.image = self.hitImage
                    Timer(0.1, self.resumeNormalSpeed).start()
          return pointsToReturn

     def resumeNormalSpeed(self):
          """The object back to normal fly"""
          if(not self.isFalling):
               self.speed = self.originalSpeeds
               self.image = next(self.ascendingimages)

     def turnBackFly(self):
          """The object back to normal fly"""
          self.isFalling = False
          self.speed = self.originalSpeeds
          self.image = next(self.ascendingimages)
               
     def fall(self):
          """The object falls"""
          self.isFalling = True
          self.speed = [0, 3]
          self.image = next(self.descedingImages)