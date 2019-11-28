import pygame
from threading import Timer

class Demon(pygame.sprite.Sprite):
     def __init__(self, startingPosition, demonFlyImagePath, demonFlyImagePath2, demonFallImagePath, speedX, speedY, _resistance, _fallToHit, _points):
          pygame.sprite.Sprite.__init__(self)
          self.flyImage = pygame.image.load(demonFlyImagePath).convert_alpha()   #imagen de vuelo
          self.flyImage2 = pygame.image.load(demonFlyImagePath2).convert_alpha()   #imagen de vuelo
          self.image = self.flyImage
          self.flyImageHit = self.fill(demonFlyImagePath)
          self.fallingImage = pygame.image.load(demonFallImagePath).convert_alpha()   #imagen de caida
          self.rect = self.image.get_rect()
          self.rect = self.rect.inflate(-20, -20) #reoooooooooooooooocien agregado
          self.rect.center = startingPosition
          self.originalSpeedX = speedX  #velocidad en el eje x
          self.originalSpeedY = speedY  #velocidad en el eje y
          self.speed = [speedX, speedY]
          self.resistance = _resistance  #cantidad de golpes normales necesarios para morir
          self.fallToHit = _fallToHit
          self.falling = False
          self.points = _points     #cantidad de puntos que otorga al morir
          self.imageA = True

     def update(self):
          if(self.rect.left <= 0 or self.rect.right >= 800):
               self.speed[0] = -self.speed[0]
          self.rect.move_ip(self.speed)
          if(not self.falling):
               if(self.imageA):
                    self.image = self.flyImage2
                    self.image = self.flyImage2
                    self.image = self.flyImage2
                    self.imageA= False
               else:
                    self.image = self.flyImage
                    self.image = self.flyImage
                    self.image = self.flyImage
                    self.imageA= True



     def fill(self, imagePath):
          image = pygame.image.load(imagePath).convert_alpha()
          w, h = image.get_size()
          for x in range(w):
               for y in range(h):
                    a = image.get_at((x, y))[3]
                    image.set_at((x, y), pygame.Color(250,250,250,a))
          return image

     def getAttack(self, hitDamage):
          points = 0
          if(self.resistance > 0 and not self.falling):
               self.resistance -= hitDamage
               if(self.resistance <= 0):
                    self.fall()
                    points = self.points
               elif(self.fallToHit):
                    self.fall()
                    timerturnBackFly = Timer(1, self.turnBackFly)
                    timerturnBackFly.start()
               else:
                    self.speed[1] = self.originalSpeedY - round(self.originalSpeedY/2)
                    self.image = self.flyImageHit
                    delayTimer = Timer(0.1, self.delayByHit)
                    delayTimer.start()
          return points

     def delayByHit(self):
          self.speed[1] = self.originalSpeedY
          self.image = self.flyImage

     def turnBackFly(self):
          self.falling = False
          self.speed[1] = self.originalSpeedY
          self.speed[0] = self.originalSpeedX
          self.image = self.flyImage

     def fall(self):
          self.falling = True
          self.speed = [0, 5]
          self.image = self.fallingImage
          