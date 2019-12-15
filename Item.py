import pygame
from threading import Timer
from ClimbingObject import ClimbingObject

class Item(ClimbingObject):
     def __init__(self, ascendingimagesPath, speeds, startingPosition, _pxChange, _points, soundPath ):
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
               _points: int
                    number of points returned when this item is reached
               ----------
          """
          super().__init__(ascendingimagesPath, speeds, startingPosition, _pxChange)
          self.points = _points
          #image that will be played when the treasure is taken
          self.takenImage = self.fill(ascendingimagesPath[0], 250, 250, 250)
          self.isTaken = False
          #add sound
          self.takeSound = pygame.mixer.Sound(soundPath)
          self.rect.inflate_ip(-10, -10)

     def beTaken(self):
          """ the object is taken: its points are returned """
          pointsToReturn = 0
          if(not self.isTaken):
               self.isTaken = True
               self.takeSound.play()
               self.image = self.takenImage
               self.speed = [0,0]
               Timer(0.1, self.dissapear).start()
               #the points are moved to other temporal variable to prevent multiple assignments
               pointsToReturn = self.points
          return pointsToReturn

     def dissapear(self):
          self.kill()