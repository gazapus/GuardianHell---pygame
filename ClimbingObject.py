import pygame
from itertools import cycle

class ClimbingObject(pygame.sprite.Sprite):
     """It models an object that rises from the screen bottom to the top"""
     def __init__(self, ascendingimagesPath, speeds, startingPosition, _pxChange):
          """
          Método inicializador de la clase ClimbingObject.
          :param list ascendingimagesPath: list of paths of ascent images
          :param list speeds: list of two values containing the velocity on the x-axis and on the y-axis
          :param list startingPosition: list of two values containing the starting position in the x-axis and y-axis
          :param int _pxChange: define how many pixels of the "y axis" will change the image
          """
          pygame.sprite.Sprite.__init__(self)
          self.speed = speeds
          self.lastYPosition  = startingPosition[1]
          self.ascendingimages = self.setImages(ascendingimagesPath)
          self.image = next(self.ascendingimages)
          self.rect = self.image.get_rect()
          self.rect = self.rect.inflate(-20, -20)
          self.rect.center = startingPosition
          self.pxChange = _pxChange

     def setImages(self, images):
          """
          Return a cyclic images list
          :param list images: list of paths of images
          """
          imagesList = []
          for imagePath in images:
               imagesList.append(pygame.image.load(imagePath).convert_alpha())
          return cycle(imagesList)

     def fill(self, imagePath, R, G, B):
          """Fill a image of white color and returned it"""
          image = pygame.image.load(imagePath).convert_alpha()
          w, h = image.get_size()
          for x in range(w):
               for y in range(h):
                    a = image.get_at((x, y))[3]
                    image.set_at((x, y), pygame.Color(R,G,B,a))
          return image


     def update(self, xMin, xMax, yMin, yMax):
          """
          Update position and image of the object
          :param int xMin: left object movement limit
          :param int xMax: right object movement limit
          :param int yMin: bottom object movement limit
          :param int yMin: top object movement limit
          """
          self.rect.move_ip(self.speed)
          #if the object is outside the y-axis limits be it will be removed       
          if(self.rect.y >= yMin + 400 or self.rect.y <= yMax - 400):
               print("muerto")
               self.kill()
          #if the object is outside the x-axis, its x-speed will be reversed      
          if(self.rect.left <= xMin or self.rect.right >= xMax):
               self.speed[0] = -self.speed[0]
          self.updateImage()

     def updateImage(self):
          """Update image object"""
          #the object position will be compared with the last position where have done an image change
          #if the object has gone far enough, the image will be changed
          if(self.rect.y < self.lastYPosition - self.pxChange):
               self.image = next(self.ascendingimages)
               #save the last position where have done an image change
               self.lastYPosition = self.rect.y