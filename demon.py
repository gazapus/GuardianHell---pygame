import pygame
from threading import Timer
from itertools import cycle

class Demon(pygame.sprite.Sprite):
     def __init__(self, _widthScreen, _heightScreen, images, demonFallImagePath, speedX, speedY, startingPosition, _resistance, _fallToHit, _points):
          pygame.sprite.Sprite.__init__(self)
          #cordenada x desde donde puede moverse el personaje
          self.startScreen = 0
          #coordenada y hasta donde puede moverse el personaje
          self.widthScreen = _widthScreen  
          #coordenada y ....
          self.heightScreen = _heightScreen
          self.originalSpeedX = speedX  #velocidad en el eje x
          self.originalSpeedY = speedY  #velocidad en el eje y
          self.speed = [speedX, speedY]
          #cantidad de golpes normales necesarios para caer definitivamente
          self.resistance = _resistance 
          #condición que describe  que si recibe un ataque y aun tiene resistencia caerá o sigue avanzando
          self.fallToHit = _fallToHit
          #cantidad de puntos que devuelve al caer definitivamente
          self.points = _points    
          #condición que describe si está el demonio cayendo
          self.isFalling = False
          #imagen usada al ser atacado
          self.hitImage = self.fill(pygame.image.load(images[0]))    
          self.fallingImage = pygame.image.load(demonFallImagePath).convert_alpha()  #imagen usada al estar ceayendo
          #ultima posicion en el eje y donde cambió de imagen
          self.lastYPosition  = _heightScreen

          imageList = []
          for imageURL in images:
               imageList.append(pygame.image.load(imageURL).convert_alpha())
          self.images = cycle(imageList)
          self.image = pygame.image.load(images[0])
          self.rect = self.image.get_rect()
          self.rect = self.rect.inflate(-20, -20)
          self.rect.center = startingPosition




     def update(self):
          if(self.rect.left <= 0 or self.rect.right >= 800):
               self.speed[0] = -self.speed[0]
          self.rect.move_ip(self.speed)
          if(not self.isFalling):
               if(self.rect.y < self.lastYPosition - 50):
                    if(self.imageA):
                         self.image = self.flyImage2
                         self.imageA = False
                    else:
                         self.image = self.flyImage
                         self.imageA = True
                    self.lastYPosition = self.rect.y
    

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
          if(self.resistance > 0 and not self.isFalling):
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
          self.isFalling = False
          self.speed[1] = self.originalSpeedY
          self.speed[0] = self.originalSpeedX
          self.image = self.flyImage

     def fall(self):
          self.isFalling = True
          self.speed = [0, 5]
          self.image = self.fallingImage
          