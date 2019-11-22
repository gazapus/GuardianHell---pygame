import pygame, time
from threading import Timer

class Treasure(pygame.sprite.Sprite):
          def __init__(self, startingPosition, imagePath, speedX, speedY, points):
               pygame.sprite.Sprite.__init__(self)
               self.image = pygame.image.load(imagePath)
               self.shineImage = self.fill(imagePath)
               self.rect = self.image.get_rect()
               self.rect.center = startingPosition
               self.speed = [speedX, speedY]
               self.points = points

          def update(self):
               self.rect.move_ip(self.speed)

          def fill(self, imagePath):
               image = pygame.image.load(imagePath).convert_alpha()
               w, h = image.get_size()
               for x in range(w):
                    for y in range(h):
                         a = image.get_at((x, y))[3]
                         image.set_at((x, y), pygame.Color(250,250,250,a))
               return image
          
          def beTaken(self):
               self.image = self.shineImage
               self.speed = [0,0]
               dissapearTime = Timer(0.1, self.dissapear)
               dissapearTime.start()
               self.points = 0
          
          def dissapear(self):
               self.kill()