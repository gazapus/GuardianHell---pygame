import pygame, random
from demon import Demon

class DemonFactory(pygame.sprite.Group):
     def __init__(self, demonsQuantity, demonsInterval, widthScreen, heightScreen,
               demonPathImage, demonFallPathImage, speedX, speedY, resistance, fallToHit, points):
          
          pygame.sprite.Group.__init__(self)
          pos_x = widthScreen/2    #todos los primeros demonios partiran de la mitad de la coordenada x
          pos_y = heightScreen + 200    #todos los primeros demonios partiran 200px mas abajos de la cordenada y
          for i in range(demonsQuantity):
               demon = Demon((pos_x, pos_y), demonPathImage, demonFallPathImage, speedX, speedY, resistance, fallToHit, points)  
               self.add(demon)
               pos_x = random.randint(round(demon.rect.width/2), widthScreen - round(demon.rect.width/2))
               pos_y = random.randint(pos_y, pos_y + demonsInterval)
               
                